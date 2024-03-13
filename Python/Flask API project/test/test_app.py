import pytest
import sqlite3
import app.app as project #notera att jag ändrat namn för importen till project istället för app.
import json
from unittest.mock import patch

# Det här testet "mockar" funktionen get_con() i "app.py" med hjälp av monkeypatch det funkar så att man säger vilket biblotek och vilken funktion man vill mocka, samt vad man vill använda istället.
@pytest.fixture
def mock_get_con(monkeypatch):
    def mock_con_object(*args, **kwargs):
        return sqlite3.Connection
    
    monkeypatch.setattr(project, "get_con", mock_con_object)

# Det här testet kollar att mocken av get_con fungerar.
def test_get_con_mocked(mock_get_con):
    actual = project.get_con()
    expected = sqlite3.Connection
    assert actual == expected

# Det här är en funktion som skapar en test-client som används för att jag ska kunna testa alla mina endpoints genom mitt "mockade" resultat. Det här är ett flask-verktyg för testning.
@pytest.fixture
def client():
    project.app.config["TESTING"] = True
    with project.app.test_client() as client:
        yield client

# Klar, denna testar både add_books() och get_specific_book()
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_get_books(client):
    response = client.get("/books")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert res[0]["titel"] == "Mitt i natten"

# Klar, detta test kontrollerar att det går att lägga till en bok i databasen.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_add_books(client):
    response = client.post("/books", json=[{"titel": "Harry Potter", "authorname": "JK.Rowling", "shortsummary": "You're a lizzard Harry", "genre": "Fantasy"}])
    res = response.data.decode("utf-8")

    assert response.status_code == 200
    assert res == "The book/books have been added to the database."

# Klar, detta test kontrollerar att det går att plocka ut en specifik bok ur databasen.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_get_specific_book(client):

    response = client.get("/books/6")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert res == [{
        "author_id": 6,
        "titel": "Försvinnande",
        "authorname": "Gillian Flynn",
        "shortsummary": "En psykologisk thriller där en kvinna plötsligt försvinner och hennes man blir huvudmisstänkt.",
        "genre": "Thriller"
    }]

# Klar, detta test kontrollerar att man kan uppdatera en bok.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.    
def test_update_book(client):
    response = client.put("/books/7", json={
        "author_id": 7,
        "titel": "Harry Potter",
        "authorname": "Gabriel García Márquez",
        "shortsummary": "En familjesaga om Buendía-klanen och den magiska staden Macondo.",
        "genre": "Magisk realism"
        })
    res = response.data.decode("utf-8")

    assert response.status_code == 200
    assert res == "Your changes has been applied to the database."

# Klar, Det här testet kontrollerar att det går att ta bort en bok ur databasen.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_delete_book(client):
    response = client.delete("books/8", json={
        "author_id": 8,
        "titel": "Den fantastiska historien om Benjamin Button",
        "authorname": "F. Scott Fitzgerald",
        "shortsummary": "En kortroman om en man som åldras baklänges och de konsekvenser det medför.",
        "genre": "Novell"
        })
    res = response.data.decode("utf-8")

    assert response.status_code == 200
    assert res == "You have succeeded in deleting a book from the database."

# Klar, det här testet kontrollerar att det går att hämta ut alla reviews ur databasen.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_get_reviews(client):
    response = client.get("/reviews")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert res[0] == {
        "review_id": 1,
        "score": 4,
        "username": "StarlightDreamer",
        "reviewsummary": "Bra",
        "author_id": 2
    }

# Klar, här kollar testet så att det går att få ut reviews för en specifik bok.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_get_reviews_for_book(client):
    response = client.get("/reviews/9")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert res == [{
        "review_id": 3,
        "score": 3,
        "username": "VelvetPenguin",
        "reviewsummary": "Över förväntan",
        "author_id": 9
    }]

# Klar, det här testet kollar så att listan med toppböcker är "fem böcker lång", att den bara innehåller 5 böcker inte mer eller mindre.
# Testet kollar också så att response.status_code == 200, alltså att uppkopplingen lyckades.
def test_get_avg_score(client):
    response = client.get("/books/top")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert len(res) == 5

# Klar, mocktest av de externa APIerna. använder unittests patch för detta. Vi kollar så att vi får tillbaka det rätta svaret på vår mockade indata.
# Har även en fixtur för att dessa funktioner är asyncrona.
@pytest.mark.asyncio
async def test_async_fetch():
    # Mockar session.get med patch
    with patch('app.app.aiohttp.ClientSession.get') as mock_get:
        mock_get.return_value.__aenter__.return_value.json.return_value = {'extract': 'Astrid Anna Emilia', "docs":[{"top_work":"Pippi Långstrump"}]}
        response = await project.fetch_both_apis("https://en.wikipedia.org/api/rest_v1/page/summary/Astrid_Lindgren")

        assert response == {'best_works': ["Pippi Långstrump"], 'shortsummary': 'Astrid Anna Emilia'}