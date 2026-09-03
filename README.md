# California Housing Price Prediction

An end-to-end machine learning project that predicts California housing prices using housing, demographic, and geographic features.

## Project Overview

Built a regression pipeline covering data preprocessing, feature engineering, model training, evaluation, model selection, and deployment integration.

Two ensemble regression models were developed and compared:

* **Random Forest Regressor**
* **XGBoost Regressor**

The models were evaluated using **MAE, MSE, RMSE, R², and Adjusted R²**.

## Model Results

| Model         |   Test MAE |  Test RMSE |    Test R² |
| ------------- | ---------: | ---------: | ---------: |
| Random Forest |     0.3281 |     0.5037 |     0.8064 |
| **XGBoost**   | **0.2974** | **0.4508** | **0.8449** |

**XGBoost was selected as the final model** because it achieved better performance on the test dataset, with lower MAE/RMSE and higher R² than Random Forest.

## Key Features

* Data preprocessing and feature engineering
* Regression model development
* Random Forest and XGBoost model comparison
* Evaluation using multiple regression metrics
* XGBoost model selection based on test performance
* Trained model serialization for inference
* Flask-based prediction application
* REST prediction endpoint
* Docker containerization
* Gunicorn-based application serving

## Technology Stack

**Python · Scikit-learn · XGBoost · Pandas · NumPy · Flask · HTML/CSS/JavaScript · Docker · Gunicorn · Git/GitHub**

## Project Structure

```text
CaliforniaHousingPricingP/
│
├── static/
├── templates/
├── CaliforniaHousingPricing_ML_Project.ipynb
├── app.py
├── Dockerfile
├── Procfile
├── requirements.txt
├── scaler_params.json
├── xgb_hy.pkl
├── xgb_hy.json
└── README.md
```
