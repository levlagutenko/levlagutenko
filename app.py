from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy import text

server = 'tehpod'
database = 'Carts'
username = 'sa'
password = 'Qq123456'
driver = 'ODBC Driver 17 for SQL Server'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.Text(100), nullable=False)
    cards = db.Column(db.Integer, nullable=False)


@app.route('/index')
@app.route('/')
def index():

    regusers = Users.query.all()

    return render_template("index.html", regusers=regusers)


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        cards = request.form['cards']
        names = 'Маркс Карл'

        users = Users(names=names, cards=cards)

        try:
            db.session.add(users)
            db.session.commit()
            return redirect('/')
        except:
            return '<h3>При добавлении статьи произошла ошибка!</h3>'
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)