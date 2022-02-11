import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = pickle.load(open('./ModelSaving/model.pkl', 'rb'))
print("Inside model")
scalar = pickle.load(open('./DataScaling/scaler.pkl', 'rb'))
print("inside scalar")


@cross_origin()
@app.route('/', methods=['GET'])
def home():
    print("Inside home page")
    return render_template('./home.html')


@cross_origin()
@app.route('/info', methods=['GET'])
def info():
    print("Inside info page")
    return render_template('./info.html')


@cross_origin()
@app.route('/developer', methods=['GET'])
def developer():
    print("Inside home page")
    return render_template('./developer.html')


@cross_origin()
@app.route('/contact', methods=['GET'])
def contact():
    print("Inside contact page")
    return render_template('./contact.html')


@cross_origin()
@app.route('/app', methods=['GET'])
def index_page():
    print("Inside app")
    return render_template('./index.html')


@cross_origin()
@app.route('/predict', methods=['POST','GET'])
def predict():
    print("Inside Predict")
    if request.method == 'POST':
        gen = (request.form['gen'])
        if gen == 'Male':
            gen = 1
        else:
            gen = 0

        age = int(request.form['age'])

        wt = float(request.form['weight'])

        dur = float(request.form['dur'])

        hrt = float(request.form['hrt'])

        cols = ([[gen, age, wt, dur, hrt]])
        print(cols)
        scl = scalar.transform(cols)
        print(scl)
        pred = model.predict(scl)
        print(pred)
        return render_template('./result.html', Prediction_text=f'The amount of calories burnt are :- {round(pred[0],2)} KCal')
    else:
        return render_template('./home.html')


if __name__ == "__main__":
    app.run(debug=True)
