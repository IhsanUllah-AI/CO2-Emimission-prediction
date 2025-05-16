# CO2 Emissions Prediction - Canada Dataset
This project uses a Linear Regression model to predict vehicle CO2 emissions based on five key features. It includes a FastAPI backend (main.py) and a Streamlit frontend (app.py).
## Overview
- *Goal:* Predict CO2 emissions using vehicle characteristics.
- *Model:* Linear Regression
- *Tech Stack:* Python, Scikit-learn, FastAPI, Streamlit, Pandas, NumPy, Matplotlib
## Features Used for Prediction
The model uses the following five variables:
1. Engine Size (L)
2. Number of Cylinders
3. Fuel Consumption City (L/100 km)
4. Fuel Consumption Hwy (L/100 km)
5. Fuel Consumption Comb (L/100 km)
## Project Files
├── main.py  # FastAPI backend for handling predictions
├── app.py   # Streamlit frontend interface 
├── model.joblib    # Trained Linear Regression model
├── requirements.txt  # Project dependencies ├── README.md           
# Project documentation └── data/ └── CO2_emissions.csv   # Dataset used for training

## How to Use
### 1. Install Dependencies
```bash
pip install -r requirements.txt
2. Start FastAPI Backend
uvicorn main:app --reload
3. Launch Streamlit App
streamlit run app.py
Author
Ihsan Ullah
GitHub: IhsanUllah-AI
