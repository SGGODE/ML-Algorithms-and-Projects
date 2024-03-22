# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from gevent.pywsgi import WSGIServer

# Load the Random Forest CLassifier model
model = pickle.load(open('heart-disease-prediction-LogisticRegression-model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    sex = int(request.form.get('sex'))
    cp = int(request.form.get('cp'))
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form.get('fbs'))
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form.get('exang'))
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form.get('slope'))
    ca = int(request.form['ca'])
    thal = int(request.form.get('thal'))
    prediction = model.predict(np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]))   
    return render_template('result.html', prediction=prediction)
        
        

if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    app.run()