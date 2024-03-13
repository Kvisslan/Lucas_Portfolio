from flask import Flask, request, g, json, current_app, jsonify
import sqlite3
import asyncio
import aiohttp

app = Flask(__name__)
app.config["DATABASE"] = "Databas.sqlite"
app.json.sort_keys = False

# Klar, den här skapar en uppkoppling mot databasen (cursor), och hanterar den sen som en dictionary istället för tuples.
def get_con():
    #if "con" not in g:
    con = sqlite3.connect(
        current_app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    con.row_factory = sqlite3.Row
    return con

# Klar, den här ser till att stänga ner den pågående uppkopplingen när inget mer finns att "hämta"
def close_con():
    con = g.pop("con", None)
    if con is not None:
        con.close()

# Klar, kör ett script med SQL-kod för att skapa en databas från "databas_script.sql" till databas.sqlite. (utf8) används för svenskatecken.
@app.cli.command('init-db') # Klar, den här Decoratorn gör att man kan köra flask init-db i terminalen för att köra funktionen init_db, som då skapar databasen.
def init_db():
    con = get_con()
    with current_app.open_resource("databas_script.sql") as file:
        con.executescript(file.read().decode("utf8"))

    print("Databas hämtad")

# Klar, denna använder olika funktioner beroende på metoden "POST" eller "GET"
@app.route("/books", methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
        return add_books()
    else:
        return get_books()

# Klar, denna hämtar alla böcker.
#@app.route("/books") Denna hanteras av funktionen handle_books() därav kommenterat ut rutten.
def get_books():
    con = get_con()
    
    filters = {
        "titel": request.args.get("titel"),
        "authorname": request.args.get("authorname"),
        "genre": request.args.get("genre"),
            }
    
    conditions = [f"{key} LIKE ?" for key, value in filters.items() if value is not None]

    sql_query = "SELECT * FROM Authorsinfo"

    if conditions:
        sql_query += " WHERE " + " AND ".join(conditions)

    with con as conn:
        cur = conn.cursor()
        cur.execute(sql_query, tuple(f"%{value}%" for value in filters.values() if value is not None))
        data = [dict(row) for row in cur.fetchall()]

    return jsonify(data)

# Klar, denna lägger till en eller flera böcker.
#@app.route("/books", methods= ["POST"]) Denna hanteras av funktionen handle_books() därav kommenterat ut rutten.
def add_books():
    con = get_con()

    with con as conn:
        cur = conn.cursor()
        book_data = request.json
        for book in book_data:
            titel = book["titel"]
            authorname = book["authorname"]
            shortsummary = book["shortsummary"]
            genre = book["genre"]

            cur.execute("INSERT INTO Authorsinfo (titel, authorname, shortsummary, genre) VALUES (?, ?, ?, ?)", (titel, authorname, shortsummary, genre))
        conn.commit()

    return "The book/books have been added to the database."

# Klar, denna hämtar specifik bok för ett author_id.
@app.route("/books/<author_id>")
def get_specific_book(author_id):
    con = get_con()
    
    with con as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Authorsinfo WHERE author_id = {author_id}")
        data = [dict(row) for row in cur.fetchall()]

    return jsonify(data)

# Klar, denna updaterar en bok med en specifikt author_id.
@app.route("/books/<author_id>", methods = ["PUT"])
def update_book(author_id):
    con = get_con()
    book = request.json

    titel = book["titel"]
    authorname = book["authorname"]
    shortsummary = book["shortsummary"]
    genre = book["genre"]
    
    with con as conn:
        cur = conn.cursor()
        cur.execute(f"UPDATE Authorsinfo SET titel = ?, authorname = ?, shortsummary = ?, genre = ? WHERE author_id = {author_id}", (titel, authorname, shortsummary, genre))
        conn.commit()

    return "Your changes has been applied to the database."

# Klar, denna tar bort boken med angivna author_id ur databasen.
@app.route("/books/<author_id>", methods = ["DELETE"])
def delete_book(author_id):
    con = get_con()
    
    with con as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM Authorsinfo WHERE author_id = {author_id}")
        conn.commit()

    return "You have succeeded in deleting a book from the database."

# Klar, denna lägger till ett betyg för det "author_id" som man skriver in.
@app.route("/reviews", methods = ["POST"])
def add_reviews_to_book():
    con = get_con()

    with con as conn:
        cur = conn.cursor()
        review_data = request.json
        for review in review_data:
            score = review["score"]
            username = review["username"]
            reviewsummary = review["reviewsummary"]
            author_id = review["author_id"]

            cur.execute("INSERT INTO Reviews (score, username, reviewsummary, author_id) VALUES (?, ?, ?, ?)", (score, username, reviewsummary, author_id))
        conn.commit()

    return "The review have been saved to the database."

# Klar, denna hämtar alla reviews
@app.route("/reviews")
def get_reviews():
    con = get_con()
    
    with con as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Reviews")
        data = [dict(row) for row in cur.fetchall()]


    return jsonify(data)

# Klar, denna hämtar reviews för specifk bok
@app.route("/reviews/<author_id>")
def get_reviews_for_book(author_id):
    con = get_con()
    
    with con as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Reviews WHERE author_id = {author_id}")
        data = [dict(row) for row in cur.fetchall()]

    return jsonify(data)

# Klar, denna hämtar dem fem böckerna som har högst avg_score.
@app.route("/books/top")
def get_avg_score():
    con = get_con()

    query=  """SELECT Authorsinfo.*, AVG(Reviews.score) as avg_score
            FROM Reviews JOIN Authorsinfo
            ON Reviews.author_id = Authorsinfo.author_id
            GROUP BY Reviews.author_id, Authorsinfo.authorname
            ORDER BY avg_score DESC
            LIMIT 5
            ;"""

    with con as conn:
        cur = conn.cursor()
        cur.execute(query)
        data = [dict(row) for row in cur.fetchall()]

    return jsonify(data)

# Klar dessa funktioner gör att hämtningen av de externa apierna kan hända asyncront istället för koden ovan.
async def async_fetch(session, url):
    async with session.get(url) as response:
        return await response.json()
    
@app.route("/author/<apiauthor>")
async def fetch_both_apis(apiauthor):

    apiauthor = apiauthor.lower().title()
    url_summary = f"https://en.wikipedia.org/api/rest_v1/page/summary/{apiauthor}"
    url_best_work = f"https://openlibrary.org/search/authors.json?q={apiauthor}"

    async with aiohttp.ClientSession() as session:
        task_summary = asyncio.create_task(async_fetch(session, url_summary))
        task_best_work = asyncio.create_task(async_fetch(session, url_best_work))

        extract = await task_summary
        top_work = await task_best_work

        shortsummary = extract.get("extract")
        best_work = top_work.get("docs")

        list_with_best_work = []

        for item in best_work:
            if item.get("top_work"):
                list_with_best_work.append(item.get("top_work"))
            else:
                continue

    return {"shortsummary": shortsummary, "best_works": list_with_best_work}

if __name__ == "__main__":
    init_db()
    app.run()