from flask import Flask,render_template,redirect
from model import *
from model1 import *


app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///agriculturedata.sqlite3"

db.init_app(app)
app.app_context().push()
