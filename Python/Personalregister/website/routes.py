# Här lägger vi alla routes för att samla dem på ett och samma ställe.
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, UserImages, SignUpUser
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

routes = Blueprint("routes", __name__)

@routes.route("/")
@login_required
def homepage():
    return render_template("homepage.html", user=current_user)

@routes.route("/all_users", methods=["GET"])
def all_users():
    page = request.args.get('page', 1, type=int)
    per_page = 30 # Antal användare som visas per sida
    get_users = request.args.get("get_users", "")
    sort_column_id = request.args.get("sort_column_id", "id")
    sort_by_order = request.args.get("sort_by_order", "desc")
    
    users = User.query.filter(
        User.name.like("%" + get_users + "%") |
        User.age.like("%" + get_users + "%") |
        User.phone.like("%" + get_users + "%") |
        User.country.like("%" + get_users + "%")
    )
    
    if sort_column_id == 'name':
        sort_by_order = User.name
    elif sort_column_id == 'age':
        sort_by_order = User.age
    elif sort_column_id == 'phone':
        sort_by_order = User.phone
    elif sort_column_id == 'country':
        sort_by_order = User.country
    else:
        sort_by_order = User.id

    if sort_by_order == 'asc':
        users = users.order_by(sort_by_order.asc())
    elif sort_by_order == 'desc':
        users = users.order_by(sort_by_order.desc())

    users = users.paginate(page=page, per_page=per_page)

    num_pages = (users.total +  per_page - 1) // per_page
    
    return render_template(
        "all_users.html",
        user=current_user,
        page=page,
        get_users=get_users,
        num_pages=num_pages,
        users=users, 
        sort_by_order=sort_by_order,
        sort_column_id=sort_column_id
        )

@routes.route("/single_user_page/<int:user_id>")
def single_user_page(user_id):
    user = User.query.filter_by(id=user_id).first()
    user_img = UserImages.query.filter_by(id=user_id).first()
    return render_template("single_user_page.html", user=user, user_img=user_img)

@routes.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")
        phone = request.form.get("phone")
        country = request.form.get("country")
        street_name = request.form.get("street_name")
        street_number = request.form.get("street_number")
        postal_code = request.form.get("postal_code")
        city = request.form.get("city")
        state = request.form.get("state")

        user_email = User.query.filter_by(email=email).first()
        user_phone = User.query.filter_by(phone=phone).first()
        if user_email:
            flash('Email-adressen är redan registrerad', category="error")
        elif user_phone:
            flash('Telefonnummret är redan registrerat', category="error")
        else:
            new_user = User(name=name, age=age, email=email, phone=phone, country=country, street_name= street_name, street_number=street_number, postal_code=postal_code, city=city, state=state)

            db.session.add(new_user)
            db.session.commit()
            flash('Ny personal registrerad! Välkommen till FramtidsRytm AB!')

    return render_template("register_user.html", user=current_user)

@routes.route("/sign_up_user", methods=["GET", "POST"])
def sign_up_user():
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = SignUpUser.query.filter_by(email=email).first()
        if user:
            flash('Email-adressen är redan registrerad', category="error")
        elif len(email) < 5:
            flash('Email-adressen måste vara mer än 4tecken.', category="error")
        elif password1 != password2:
            flash('Lösenorden matchar inte', category="error")
        elif len(password1) < 7:
            flash('Lösenordet måste var mer än 6tecken.', category="error")
        else:
            new_sign_up = SignUpUser(email=email, password=generate_password_hash(
                password1))
            db.session.add(new_sign_up)
            db.session.commit()
            login_user(new_sign_up, remember=True)
            flash("Tack för att du registrerat dig! Du är nu inloggad!", category="success")
            return redirect(url_for("routes.homepage"))
    
    return render_template("sign_up_user.html", user=current_user)

@routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = SignUpUser.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Du är inloggad!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("routes.homepage"))
            else:
                flash("Fel lösenord.", category="error")
        else:
            flash("Email-adressen kunde inte hittas.", category="error")

    return render_template("login.html", user=current_user)

@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("routes.login"))