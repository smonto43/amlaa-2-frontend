import requests
import json
import pandas as pd

def get_sales_prediction(api_url, store_id, item_id, day_of_week, month, year, day_of_month, is_weekend):
    """
    Function to make a POST request to the FastAPI sales prediction API.
    
    Parameters:
    - api_url (str): The URL of the FastAPI /predict endpoint.
    - store_id (str): Store ID for which the prediction is to be made.
    - item_id (str): Item ID for which the prediction is to be made.
    - day_of_week (int): Day of the week (0=Monday, 6=Sunday).
    - month (int): Month of the year (1-12).
    - year (int): Year of the date.
    - day_of_month (int): Day of the month (1-31).
    - is_weekend (int): Whether it's a weekend (0=No, 1=Yes).
    
    Returns:
    - Predicted sales (float) or an error message.
    """
    params = {
        "store_id": store_id,
        "item_id": item_id,
        "day_of_week": day_of_week,
        "month": month,
        "year": year,
        "day_of_month": day_of_month,
        "is_weekend": is_weekend
    }

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
           
            result = response.json()
            return result
        else:
            return f"Error {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"
    


def get_forecast(api_url, date):
    """
    Function to make a GET request to the FastAPI sales prediction API.
    
    Parameters:
    - api_url (str): The URL of the FastAPI /sales/national endpoint.
    - date (str or pd.Timestamp): Date string in the format 'YYYY-MM-DD'.
    
    Returns:
    - Predicted sales (float) or an error message.
    """
    date = date.strftime('%Y-%m-%d')
    try:

        response = requests.get(api_url, params={"date": date})

        if response.status_code == 200:

            result = response.json()
            return result
        else:
            return f"Error {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:

        return f"Connection error: {str(e)}"