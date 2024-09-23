from collections import defaultdict
import streamlit as st
from pathlib import Path
from src.models.predict_model import get_sales_prediction
from src.features.build_features import add_answer
from src.features.dates import extract_info_date
import pandas as pd
import os

home = "Home"
data = "Prective Model"



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
        st.write(get_sales_prediction(os.getenv("API_URL"), store_id, item_id, day_of_week, month, year, day_of_month, is_weekend))
    
    


def render_features():
    st.subheader("Feature Engineering Process")
    st.write("The following transformations were applied to the following datasets:")
    st.subheader("Adding Answer to Universe Feature example:")
    df = pd.DataFrame(
        [
            {"name": "alice", "favorite_animal": "dog"},
            {"name": "bob", "favorite_animal": "cat"},
        ]
    )
    st.write("Initial data")
    st.write(df)
    df = add_answer(df)
    st.write("Transformed data")
    st.write(df)


def render_training():
    st.subheader("Model Training Overview")
    st.write("The following models and hyperparameters were tested:")
    for sub_path in (
        x
        for x in Path("models").iterdir()
        if x.is_file() and not x.name.startswith(".")
    ):
        st.subheader(sub_path.name)
        st.write("Size in bytes: ", len(sub_path.read_bytes()))

display_page = st.sidebar.radio("View Page:", (home, data))


if display_page == home:
    render_home()
elif display_page == data:
    render_data()


