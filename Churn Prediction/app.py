import numpy as np
from flask import Flask, request, render_template
import pickle
from gevent.pywsgi import WSGIServer
 
model = pickle.load(open('LogRegression.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    international_plan = float(request.form.get('international_plan'))
    voice_mail_plan = float(request.form.get('voice_mail_plan'))
    number_vmail_messages = float(request.form.get('number_vmail_messages'))
    total_day_minutes = float(request.form.get('total_day_minutes'))                   
    total_day_calls = float(request.form.get('total_day_calls'))
    total_day_charge = float(request.form.get('total_day_charge'))
    total_eve_minutes = float(request.form.get('total_eve_minutes'))                   
    total_eve_calls = float(request.form.get('total_eve_calls'))                       
    total_eve_charge = float(request.form.get('total_eve_charge'))                     
    total_night_minutes = float(request.form.get('total_night_minutes'))               
    total_night_calls = float(request.form.get('total_night_calls'))                   
    total_night_charges = float(request.form.get('total_night_charges'))               
    total_intl_minutes = float(request.form.get('total_intl_minutes'))                 
    total_intl_calls = float(request.form.get('total_intl_calls'))                     
    total_intl_charge = float(request.form.get('total_intl_charge'))                   
    number_customer_service_calls = float(request.form.get('number_customer_service_calls')) 
    result = model.predict(np.array([international_plan,voice_mail_plan,number_vmail_messages,total_day_minutes,total_day_calls,total_day_charge,total_eve_minutes,total_eve_calls,total_eve_charge,total_night_minutes,total_night_calls,total_night_charges,total_intl_minutes,total_intl_calls,total_intl_charge,number_customer_service_calls]).reshape(1,16))  
    if result[0] == 1:
       result = 'Will leave'
    else:
       result = 'Will Stay'   
                  
    return render_template('new.html',result=result)


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    app.run()
