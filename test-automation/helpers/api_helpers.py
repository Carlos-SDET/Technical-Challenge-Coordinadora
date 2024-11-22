import json
from datetime import datetime, timedelta
from test_data.valid_requests import REQUEST_JSON

def get_base_request():
    return json.loads(REQUEST_JSON)

def modify_request(modification_type: str):
    request = get_base_request()

    if modification_type == "future_date":
        future_date = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
        request["fechaRecogida"] = future_date
    elif modification_type == "missing_fields":
        request["apellidosEntrega"] = ""
    elif modification_type == "invalid_date":
        request["fechaRecogida"] = "fecha-invalida"
        
    return request