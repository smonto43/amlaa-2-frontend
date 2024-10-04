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
status_api = "Project Description"




def render_home():
    
    st.image('images/UTS-Logo-Syd.jpg')
    st.header("Santiago Montoya - App Assigment 2")
    st.subheader("36120 Advanced Machine Learning Application")
    st.write("**Student Id:** 24898381")
    st.write('Wait for the welcome message to start using the app (dont try to use this app using UTS wifi, given that it blocks the render app)')


    try:
        response = requests.get("https://assignment-2-qj7c.onrender.com/health/")
        st.write(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            st.success(f"{response.json()['message']}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
    st.write("Go to the Project description page (at your left), to understand this app")

    

def render_data():
    st.image('images/machine-learning.jpg', width=200)
    st.subheader("Predictive Model")
    st.write("Predicts sales of a specific item in a specific shop for a given date.")
    
    date_input = st.date_input('date formar: YYYY-MM-DD: ')

    with open('data/processed/store_items_ids.json') as f:  
        data = json.load(f)
    stores, item = data['store_id'], data['item_id']

    store_id = st.selectbox("Select a store",stores)
    item_id = st.selectbox("Select a item",item)


    year, month, day_of_month,day_of_week, is_weekend = extract_info_date(date_input)

    if st.button('Predict'):
        st.write(get_sales_prediction("https://assignment-2-qj7c.onrender.com/sales/stores/items", store_id, item_id, day_of_week, month, year, day_of_month, is_weekend))
        
    


def forecasting():
    st.image('images/OIP.jpeg', width=200)
    st.subheader("Forecasting Model")
    st.write("Predicts national sales for the whole company for the next 7 days.")

    date_input = st.date_input('Initial date forecasting: ')

    if st.button('Predict'):
        st.write(get_forecast("https://assignment-2-qj7c.onrender.com/sales/national", date_input))


def api_check():
 
    st.image('images/reading-fastapi.jpg', width=200)

    st.subheader("Project Overview")
    st.write("This is the response from the root endpoint (‘/’). Below is the project description, its various endpoints, and the expected responses.")


    response = requests.get("https://assignment-2-qj7c.onrender.com/")
    

    if response.status_code == 200:
  
        data = response.json()
        
        project_description = data.get('project_description', 'Not available')
        endpoints = data.get('endpoints', {})
        github_repo_backend = data.get('github_repo_backend', 'Not available')
        github_repo_frontend = data.get('github_repo_frontend', 'Not available')
        render_app_link = data.get('render_app_link', 'Not available')
        streamlit_link = data.get('streamlit_link', 'Not available')
        
        st.subheader("Project Description")
        st.write(project_description)
        

        st.write("**Backend GitHub Repo:** [Link](" + github_repo_backend + ")")
        st.write("**Frontend GitHub Repo:** [Link](" + github_repo_frontend + ")")
        st.write("**Render App Link:** [Link](" + render_app_link + ")")
        st.write("**Streamlit Link:** [Link](" + streamlit_link + ")")

        st.subheader("Available Endpoints")
        for endpoint, details in endpoints.items():
            st.markdown(f"### Endpoint: `{endpoint}`")

            if isinstance(details, str):
                st.markdown(f"**Description**: {details}")
            else:

                st.markdown(f"**Description**: {details.get('description', 'Not available')}")
                st.markdown(f"**Method**: {details.get('method', 'Not available')}")
    
                input_params = details.get('input_parameters', None)
                if input_params:
                    st.markdown("**Input Parameters**:")
                    for param, description in input_params.items():
                        st.markdown(f"- **{param}**: {description}")

                output_format = details.get('output_format', None)
                if output_format:
                    st.markdown("**Expected Output Format**:")
                    st.json(output_format) 
            
            st.markdown("---")
    
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



