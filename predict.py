import joblib
import pandas as pd
import numpy as np

def exp_transform(Y):
    """exp transformer to get original feature/target back"""
    return np.expm1(Y)

model = joblib.load("model/LR_final_run.pkl")

def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction_log = model.predict(df)[0]
    prediction = exp_transform(prediction_log)
    return int(prediction)