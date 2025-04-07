# create flask app

from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

#import ridge-regressor and scaler-model
ridge_model = pickle.load(open('models/ridgeForest.pkl','rb'))
standard_scaler = pickle.load(open('models/scalerForest.pkl','rb'))

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes'))
        region = float(request.form.get('Region'))


        new_scaled_data = standard_scaler.transform([[temperature,RH,WS,rain,FFMC,DMC,ISI,classes,region]])
        result = ridge_model.predict(new_scaled_data)

        return render_template('index.html',result=result[0])
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)