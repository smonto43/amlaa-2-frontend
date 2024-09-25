from collections import defaultdict
import streamlit as st
from pathlib import Path
from src.models.predict_model import get_sales_prediction, get_forecast
from src.features.build_features import load_data
from src.features.dates import extract_info_date
import pandas as pd
import os
import json
import requests



home = "Home"
data = "Prective Model"
forecast = "Forecast"
status_api = "API_status"




def render_home():
    
    st.image('images/UTS-Logo-Syd.jpg')
    st.header("Santiago Montoya - App Assigment 2")
    st.subheader("36120 Advanced Machine Learning Application")
    st.write("**Student Id:** 24898381")
    

def render_data():
    st.image('images/machine-learning.jpg', width=200)
    st.subheader("Predictive Model")
    st.write("El siguiente modelo les permite predecir las ventas de una tienda y un item en especifico para la fecha dada:")
    
    date_input = st.date_input('date formar: YYYY-MM-DD: ')
    data = load_data()
    stores, item = data['store_id'], data['item_id']

    store_id = st.selectbox("Select a store",stores)
    item_id = st.selectbox("Select a item",item)


    year, month, day_of_month,day_of_week, is_weekend = extract_info_date(date_input)

    if st.button('Predict'):
        st.write(get_sales_prediction("https://assignment-2-qj7c.onrender.com/sales/stores/items", store_id, item_id, day_of_week, month, year, day_of_month, is_weekend))
        
    


def forecasting():
    st.image('images/OIP.jpeg', width=200)
    st.subheader("Forecasting Model")
    st.write("El siguiente modelo les permite predecir las ventas de una tienda y un item en especifico para la fecha dada:")

    date_input = st.date_input('Initial date forecasting: ')

    if st.button('Predict'):
        st.write(get_forecast("https://assignment-2-qj7c.onrender.com/sales/national", date_input))


def api_check():
    st.image('images/reading-fastapi.jpg', width=200)
    st.subheader("API endpoints")
    
    st.write("El siguiente modelo les permite predecir las ventas de una tienda y un item en especifico para la fecha dada:")


    if st.button("Probar endpoint /"):
        response = requests.get("https://assignment-2-qj7c.onrender.com/")
        if response.status_code == 200:
            st.success(f"Respuesta: {response.text}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    # Botón para probar el endpoint "/health/"
    if st.button("Probar endpoint /health/"):
        response = requests.get(f"{"https://assignment-2-qj7c.onrender.com"}/health/")
        if response.status_code == 200:
            st.success(f"Respuesta: {response.text}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")




display_page = st.sidebar.radio("View Page:", (home, status_api, data, forecast ))


if display_page == home:
    render_home()
elif display_page == status_api:
    api_check()
elif display_page == data:
    render_data()
elif display_page == forecast:
    forecasting()



