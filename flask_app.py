from flask import Flask, request
import pandas as pd
import os
import pickle
from flasgger import Swagger

file = open("model.pkl",'rb')
model = pickle.load(file)
file.close()


app = Flask(__name__)


@app.route('/')
def home_page():
    return "Hello"


@app.route('/predict')
def prediction_page():


    gender = request.args.get("Gender")
    if gender == "male" or gender == "Male":
        gender = 1
    else:
        gender = 0

    age = request.args.get("Age")
    salary = request.args.get("AnnualSalary")
    prediction = model.predict([[age,salary,gender]])
    if int(prediction) == 1:
        return "Customer will buy the car"
    else:
        return "Customer will not buy the car"


@app.route('/predict_file',methods=['POST'])
def predict_file():
    file = pd.read_csv(request.files.get("file"))
    prediction = model.predict(file)

    return "result is : \n" + str(list(prediction))

if __name__ == "__main__":
   app.run()