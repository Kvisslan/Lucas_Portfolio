#Här ska vi lägga alla mallan från saker som vi vill spara från tillexempel ett formulär. Så typ en plats för alla "blueprints" för en klass User om man vill lagra info om användare.

from . import db
from faker import Faker
import random
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True)
    country = db.Column(db.String(50))

    street_name = db.Column(db.String(100))
    street_number = db.Column(db.Integer)
    postal_code = db.Column(db.String(20))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))

    img = db.relationship("UserImages", back_populates="user")

class UserImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="img")

class SignUpUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))


def create_img_table():
    i = 0
    while UserImages.query.count() < 100:
        i += 1
        size = "500x500"
        img_format = "jpg"

        new_img_url = f"https://robohash.org/{i}.{img_format}?size={size}"

        new_user_img = UserImages(img_url=new_img_url)
        db.session.add(new_user_img)
        db.session.commit()

def create_fake_users():
    faker = Faker()
    while User.query.count() < 100:
        new_name = faker.name()
        new_age = random.randint(18, 65)
        new_email = faker.email()
        new_phone = faker.phone_number()
        new_country = random.choice(["Sverige", "Norge", "Danmark", "Finland", "Island", "Grönland", "Färöarna", "Estland", "Lettland", "Litauen"])

        new_street_name = faker.street_name()
        new_street_number = faker.building_number()
        new_postal_code = faker.postcode()
        new_city = faker.city()
        new_state = faker.state()

        new_user = User(name=new_name, age=new_age, email=new_email, phone=new_phone, country=new_country,
        street_name=new_street_name, street_number=new_street_number, postal_code=new_postal_code, city=new_city, state=new_state)
        db.session.add(new_user)
        db.session.commit()

def create_admin():
    while SignUpUser.query.count() < 1:
        new_email = "admin@admin.se"
        new_password = generate_password_hash("admin123")

        new_user = SignUpUser(email=new_email, password=new_password)
        db.session.add(new_user)
        db.session.commit()