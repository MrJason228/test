from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shop.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)


    def __repr__(self):
        return  f"User {self.name} has email: {self.email}"



class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_title = db.Column(db.String(64), nullable=False)
    name1 = db.Column(db.String(64), nullable=False)
    items_quantity = db.Column(db.Integer, nullable=False)



@app.route("/catalog")
def catalog():
    catalog1 = Catalog(shop_title='Назва магазину')
    catalog2 = Catalog( name1='Тут повинна бути кнопка з переходом у каталог', items_quantity='А тут цифра загальної кількості товарів')
    db.session.add(catalog1, catalog2)
    db.session.commit()


def catalogs():
    catalogss = Catalog.query.all()
    return redirect(url_for("catalog"))


@app.route("/users")
def users():
    users = User.query.all()
    return f"{users}"


@app.route("/create_user")
def create_user():
    user = User(name="Ivan", email="neveroyatno@gmail.com", password="qwerty1234")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("users"))

with app.app_context():
    db.create_all()
        
app.run(debug=True)