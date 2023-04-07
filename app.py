from flask import Flask,render_template,redirect,request
from model import *
import numpy as np
import pandas as pd
import pickle
from ml_model import *
crop_recommendation_model_path = 'knn_pipeline.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))
#creating the app
app=Flask(__name__)

#configuring the app
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///agriculturedata.sqlite3"

@app.route('/',methods=['GET',"POST"])
def index_page():
    return render_template('index.html')

@app.route('/recommendation')
def rec_page():
    return render_template('recommendation.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        f = [float(x) for x in request.form.values()]
        data = [np.array(f)]
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        final_prediction = label_dict[final_prediction]

        return render_template('recommendation.html', prediction_text=final_prediction)


@app.route('/foreign_crop',methods=['GET','POST'])
def foreign_crop():
    return render_template('foreign.html',data=[{'name':'HopShoots'}, {'name':'green'}, {'name':'blue'}])

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    if select == 'HopShoots':
        return render_template('HopShoots.html')

@app.route('/price',methods=['GET','POST'])
def price_prediction():
    return render_template('price_prediction.html')

if __name__ == "__main__":
    app.run(debug=True)

