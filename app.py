import pickle
from flask import Flask,request,jsonify,render_template,app,redirect,url_for
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb

app=Flask(__name__)

# Load the pre-trained model uisng Pickle files "But version mismatch give errors"
#xgbmodel = pickle.load(open('xgb_hy.pkl', 'rb'))

#Loading model by importing as json file
xgbmodel = xgb.XGBRegressor()
xgbmodel.load_model("xgb_hy.json")



@app.route('/')
def home():
    return render_template('home.html')

#to run our model in Postman API 
@app.route('/predict',methods=['POST'])
def predict():
    try:
        # This function will receive data in JSON format. if we use Postman, we can send data in JSON format
        #data=request.json['data']
        #print("Data received for prediction:", data)
        
        # Get the data from the request
        # Extract all 8 form inputs
        features = [
            float(request.form['median_income']),
            float(request.form['house_age']),
            float(request.form['avg_rooms']),
            float(request.form['avg_bedrooms']),
            float(request.form['population']),
            float(request.form['avg_occupancy']),
            float(request.form['latitude']),
            float(request.form['longitude'])
        ]
        print("Received features:", features)

        new_data = np.array([features]) # shape (1,8)
        print("Test prediction small values:", xgbmodel.predict(np.array([[1, 5666, 3, 1, 100, 2, 34, -118]])))
        print("Test prediction large values:", xgbmodel.predict(np.array([[10, 50, 203625, 10, 10000, 5, 40, -120]])))
            
        # Make prediction
        prediction=xgbmodel.predict(new_data)
        print("Prediction result:", prediction[0])
        

        
        #if we want to return the prediction as a JSON response in Postman
        #return jsonify({'prediction': round(prediction[0],2)})
        
        return render_template('home.html', prediction_text=f'Predicted House Price: ${round(float(prediction[0]), 2):,}')

    
    except Exception as e:
        print("Error during prediction:", str(e))
        return jsonify({'error': str(e)})



if __name__=="__main__":
    app.run(debug=True)