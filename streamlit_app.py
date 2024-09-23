from collections import defaultdict
import streamlit as st
from pathlib import Path
from src.models.predict_model import get_sales_prediction, get_forecast
from src.features.dates import extract_info_date
import pandas as pd
import os

home = "Home"
data = "Prective Model"
forecast = "Forecast"



def render_home():
    
    st.image('images/UTS-Logo-Syd.jpg')
    st.header("Santiago Montoya - App Assigment 2")
    st.subheader("36120 Advanced Machine Learning Application")
    st.write("**Student Id:** 24898381")




def render_data_directory(dir: Path):
    st.subheader('Predictive Model')




def render_data():
    st.image('images/machine-learning.jpg', width=200)
    st.subheader("Predictive Model")
    st.write("El siguiente modelo les permite predecir las ventas de una tienda y un item en especifico para la fecha dada:")
    date_input = st.date_input('date formar: YYYY-MM-DD: ')
    stores = ['CA_1', 'CA_2', 'CA_3', 'CA_4', 'TX_1', 'TX_2', 'TX_3', 'WI_1',
            'WI_2', 'WI_3']
    item = ['HOBBIES_1_001', 'HOBBIES_1_002', 'HOBBIES_1_003',
       'FOODS_3_825', 'FOODS_3_826', 'FOODS_3_827']
    store_id = st.selectbox("Select a store",stores)
    item_id = st.selectbox("Select a item",item)


    year, month, day_of_month,day_of_week, is_weekend = extract_info_date(date_input)

    if st.button('Predict'):
        st.write(get_sales_prediction("https://assignment-2-qj7c.onrender.com/predict", store_id, item_id, day_of_week, month, year, day_of_month, is_weekend))
        
    


def forecasting():
    st.image('images/OIP.jpeg', width=200)
    st.subheader("Forecasting Model")
    st.write("El siguiente modelo les permite predecir las ventas de una tienda y un item en especifico para la fecha dada:")

    date_input = st.date_input('Initial date forecasting: ')

    if st.button('Predict'):
        st.write(get_forecast("https://assignment-2-qj7c.onrender.com/sales/national", date_input))

display_page = st.sidebar.radio("View Page:", (home, data, forecast))


if display_page == home:
    render_home()
elif display_page == data:
    render_data()
elif display_page == forecast:
    forecasting()


