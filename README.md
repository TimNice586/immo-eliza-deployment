# 🏡 Immo Eliza — Property Price Predictor (Streamlit Web App)

## 📊 Project Overview
This project is a web application built with **Streamlit** that predicts property prices in Belgium using a machine learning model trained in a previous phase.  
The goal is to provide a **user-friendly interface** for non-technical employees and clients to estimate property prices based on key property features.

The web app allows users to:

- Input property details (location, type, size, amenities, etc.)
- Automatically resolve postal codes, municipalities, provinces, and regions
- Predict estimated prices using a trained **Linear Regression model**
- Visualize results instantly in a clean interface  

---

## 🎯 Key Objectives
- **User Interaction**: Provide a clean, intuitive web app for property price prediction.  
- **Data Handling**: Map postal codes and municipalities to regions and provinces, normalize user input, and handle optional/required features.  
- **Prediction**: Use a pre-trained Linear Regression model with feature preprocessing to predict property prices.  
- **Reproducibility**: Ensure the pipeline works reliably for any property input.  

---

## 🤖 Model Implemented
The model used in this project is:

- **Linear Regression (LR)**  
  - Trained on Belgian property data
  - Uses feature preprocessing including imputation, scaling, and transformation
  - Model saved as `LR_final_run.pkl` and loaded in `predict.py`

---

## 🔍 Technical Highlights

### 🔧 Data & Feature Handling
- Mapping of **municipalities ↔ postal codes**
- Mapping of **provinces ↔ regions**
- Property type and subtype management with auto-correction
- Normalization of user input (lowercasing, accent removal, aliases)
- Handling optional features like terrace, swimming pool, garden, etc.

### 📈 Prediction Pipeline
- Input is collected from Streamlit UI widgets
- Features are processed to match the model requirements
- Predictions are generated using `predict.py` which:
  - Loads the trained model
  - Applies inverse transformations (from log scale)
  - Returns the estimated price  

### 📦 File Structure
├── model
│ └── LR_final_run.pkl # Trained Linear Regression model
│
├── streamlit_app.py # Main Streamlit app
├── predict.py # Model prediction script
├── pipeline.py # Preprocessing & ML pipelines
├── message.txt # Municipality to postal code mapping
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 How to Run
1. **Install dependencies**:
```bash
pip install -r requirements.txt
Start the Streamlit app:

bash
streamlit run streamlit_app.py
Use the app:

Enter a postal code or municipality

Select property type, subtype, and details

Click Predict Price

View the estimated price

🗓 Timeline
Duration: 5 days

Focus: Building a fully functional web application for property price prediction

Outcome: A deployed Streamlit app ready for Belgian property data

👤 Author
Tim De Nijs
Data Science & AI — BeCode Ghent (2025–2026)