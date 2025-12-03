import joblib
import pandas as pd

model = joblib.load("model/LR_final_run.pkl")

def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return int(prediction)