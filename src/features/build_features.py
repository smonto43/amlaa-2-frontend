import requests
import json
from pathlib import Path

def save_store_items_to_file(api_url):
    """
    Función para realizar una solicitud GET al endpoint de FastAPI que devuelve store_id e item_id,
    y guardar el resultado como un archivo JSON en la ruta ../../data/processed/store_items_ids.json.
    
    Parámetros:
    - api_url (str): La URL del endpoint de FastAPI (/list_store_items).
    
    Acción:
    - Guarda el archivo JSON en la ruta ../../data/processed/store_items_ids.json.
    """
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(api_url)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear la respuesta JSON
            result = response.json()
            
            # Guardar el JSON como archivo en la ruta ../../data/processed/store_items_ids.json
            json_file_path = Path("data/processed/store_items_ids.json")
            
            # Crear el directorio si no existe
            json_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Guardar el JSON en el archivo
            with open(json_file_path, "w") as json_file:
                json.dump(result, json_file, indent=4)
            

        
        else:
            # Si hubo un error, mostrar el código de error
            print(f"Error {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión u otras excepciones de solicitud
        print(f"Error de conexión: {str(e)}")


import json

# Cargar el JSON desde un archivo o variable
def load_data():
    save_store_items_to_file("https://assignment-2-qj7c.onrender.com/list_store_items/")

    with open('../../data/processed/store_items_ids.json') as f:  # Asumiendo que tienes un archivo data.json
        data = json.load(f)
    return data
