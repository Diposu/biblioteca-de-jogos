from flask import Flask     #micro framework
from flask_sqlalchemy import SQLAlchemy     #BD
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.py')     #configuracaoes do BD

db = SQLAlchemy(app)

csrf = CSRFProtect(app)

from views import *     #importacao dos viwes

if __name__ == '__main__':
    app.run(debug=True)     #rerun auto

