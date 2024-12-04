import json
import random
from datetime import datetime, timedelta
from test_data.valid_requests import REQUEST_JSON

def get_base_request():
    return json.loads(REQUEST_JSON)

def generate_address():
    """Genera una dirección aleatoria válida"""
    calle = random.randint(1, 100)
    numero = random.randint(1, 50)
    apto = random.randint(1, 20)
    return f"Calle {calle} # {numero} - {apto}"

def generate_valid_date():
    """Genera una fecha válida (2 días en el futuro)"""
    return (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")

def modify_request(modification_type: str):
    """modificar request dependiendo del escenario"""
    request = get_base_request()

    if modification_type == "successful":
        # Caso exitoso con datos válidos
        request["direccion"] = generate_address()
        request["fechaRecogida"] = generate_valid_date()
        
    elif modification_type == "future_date":
        # Fecha inválida (10 días futuro) pero dirección válida
        request["direccion"] = generate_address()
        request["fechaRecogida"] = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
        
    elif modification_type == "missing_fields":
        # Dirección y fecha válidas pero apellidos vacíos
        request["direccion"] = generate_address()
        request["fechaRecogida"] = generate_valid_date()
        request["apellidosEntrega"] = ""
        
    elif modification_type == "invalid_date":
        # Dirección válida pero fecha inválida
        request["direccion"] = generate_address()
        request["fechaRecogida"] = "fecha-invalida"
        
    return request