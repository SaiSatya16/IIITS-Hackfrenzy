from flask import Flask,render_template,redirect,request
from model import *

#creating the app
app=Flask(__name__)

#configuring the app
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///agriculturedata.sqlite3"

@app.route('/',methods=['GET',"POST"])
def index_page():
    return render_template('index.html')

@app.route('/crop_rec',methods=['GET','POST'])
def crop_recommendation():
    return render_template('recommendation.html')

@app.route('/foreign_crop',methods=['GET','POST'])
def foreign_crop():
    return render_template('foreign.html')

@app.route('/price',methods=['GET','POST'])
def price_prediction():
    return render_template('price_prediction.html')

