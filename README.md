                              🏥 Medical Insurance Cost Prediction App

This project uses a machine learning model to predict medical insurance costs based on user inputs like age, BMI, smoking status, and region. It’s designed to help individuals and insurance providers make data-informed decisions and is deployed as an interactive web app using Streamlit.

 ## 🔗 Live App: [Click here to use the app]
 https://medical-cost-prediction-app-pdiaewrtyknc5hapnvw7mb.streamlit.app/

## 📌 Table of Contents

- Overview
- Features
- Dataset
- Tech Stack
- Project Structure
- Installation
- How to Use


## 📊 Overview

Healthcare costs vary greatly across individuals. By leveraging historical data and regression techniques, this app predicts insurance charges using features like:

- Age  
- Gender  
- Body Mass Index (BMI)  
- Number of children  
- Smoking status  
- Geographic region

The goal is to provide a quick, interactive, and intuitive prediction tool using machine learning.

## 🚀 Features

- 📈 Predict insurance costs based on input attributes  
- 🧠 Trained ML model using RandomForestRegressor  
- 📊 EDA and feature correlation visualizations in Jupyter Notebook  
- 💻 Streamlit web interface for ease of use  
- ✅ Deployed via Streamlit Cloud


## 📂 Dataset
The dataset used is the **Medical Cost Personal Dataset**, which is included in this repository


## 🛠 Tech Stack

- Python
- Pandas, NumPy – Data processing
- Matplotlib, Seaborn – Data visualization
- Scikit-learn – Machine learning model
- Streamlit – Web app deployment


## 🗂 Project Structure

├── Medical_Cost_App.py # Streamlit app script
├── medical_model.pkl # Trained ML model
├── Medical cost analysis.ipynb # Exploratory data analysis and model training
├── Medical cost Dataset.csv # Dataset (Medical Cost Dataset)
├── requirements.txt # Required packages for the app
└── README.md # Project documentation

## Install dependencies
pip install -r requirements.txt

## Run the Streamlit app
streamlit run Medical_Cost_App.py


## 🧪 How to Use
Enter user details in the sidebar:

Age
Gender
BMI
Children
Smoking status
Region
Click Predict to view the estimated medical insurance cost.
The app will display the predicted cost using the trained ML model
