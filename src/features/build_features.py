import requests
import json
from pathlib import Path

def save_store_items_to_file(api_url):

    try:

        response = requests.get(api_url)
        

        if response.status_code == 200:
            result = response.json()
            
            json_file_path = Path("data/processed/store_items_ids.json")
            
            json_file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(json_file_path, "w") as json_file:
                json.dump(result, json_file, indent=4)
            

        
        else:
            print(f"Error {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {str(e)}")


import json

def load_data():
    save_store_items_to_file("https://assignment-2-qj7c.onrender.com/list_store_items/")

    with open('../../data/processed/store_items_ids.json') as f: 
        data = json.load(f)
    return data
