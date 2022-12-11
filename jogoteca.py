from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')     #configuracaoes do BD

db = SQLAlchemy(app)

csrf = CSRFProtect(app)

bcrypt = Bcrypt(app)

from views_game import *
from views_user import *                               #importacao dos viwes

if __name__ == '__main__':
    app.run(debug=True)     #rerun auto

