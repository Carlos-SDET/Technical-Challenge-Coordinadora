import pytest
import requests
from datetime import datetime, timedelta

# URL del servicio
BASE_URL = "https://apiv2-test.coordinadora.com/recogidas/cm-solicitud-recogidas-ms/solicitud-recogida"

# Datos base para las pruebas
def get_base_request():
    return {    
        "tipoEnvio": "1",
        "tipoProducto": "4",
        "indicativo": "57",
        "tipoDocumento": "13",
        "email": "ana@gmail.com",
        "personaEntrega": "1",
        "indicativoEntrega": "57",
        "medidasAproximadas": [
            {
                "id": 2,
                "tipoPaq": "Par de zapatos",
                "nombrePaq": "Par de za...",
                "cantidad": 1
            }
        ],
        "ciudad": "Envigado (Ant)",
        "via": "",
        "numero": "",
        "detalle": "PARQUE SAN JOSE BOD 14",
        "tipoVia": 16,
        "nombres": "prueba",
        "apellidos": "prueba1",
        "documento": "1036149000",
        "celular": "3005777777",
        "direccion": "Calle 50 # 40-20",
        "fechaRecogida": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
        "nombreEntrega": "carlos",
        "apellidosEntrega": "posada",
        "celularEntrega": "3001234567",
        "emailUsuario": "carlos.posada@gmail.com",
        "descripcionTipoVia": "Calle",
        "aplicativo": "envios",
        "ciudadDetalle": {
            "nombre_terminal_operativa": "Medellin",
            "tipo_servicio": "A",
            "dane_ciudad": "05266",
            "dane_actual": "05266000",
            "ciudad_tarifa": "05266000",
            "sms": True,
            "cubre_mqp": True,
            "codigo_postal": "055428",
            "terminal_operativa": 2,
            "cubre_me": True,
            "area_telefono": 4,
            "observaciones2": "FCE - RD - FD - RCE",
            "codigo": "05266000",
            "tipo_poblacion": "D",
            "activo": True,
            "codigo_terminal": 2,
            "codigo_interno": 204,
            "mensajeria": True,
            "cubre_mm": False,
            "departamento": "05",
            "cubre_cm": False,
            "nombre": "Envigado (Ant)",
            "abreviado": "ENVIGADO",
            "nombre_terminal": "Medellin",
            "observaciones": ""
        }
    }

def test_successful_request():
    """Test Case 1: Creación exitosa de recogida"""

    request_data = get_base_request()
    response = requests.post(BASE_URL, json=request_data)
    response_data = response.json()
    
    # validations
    assert response.status_code == 200
    assert response_data["isError"] == False
    assert "id_recogida" in response_data["data"]
    assert "Solicitud recogida programada exitosamente" in response_data["data"]["id_recogida"]["message"]

def test_duplicate_request():
    request_data = get_base_request()
    first_response = requests.post(BASE_URL, json=request_data)
    duplicate_response = requests.post(BASE_URL, json=request_data)
    response_data = duplicate_response.json()
    
    # validations
    assert duplicate_response.status_code == 200
    assert response_data["isError"] == True
    assert "Ya existe una recogida programada para hoy" in response_data["data"]["message"]

def test_future_date_request():
    request_data = get_base_request()
    request_data["fechaRecogida"] = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
    response = requests.post(BASE_URL, json=request_data)
    response_data = response.json()
    
    # validations
    assert response.status_code == 200
    assert response_data["isError"] == True
    assert "no debe ser mayor a la fecha" in response_data["data"]["message"]

def test_missing_required_fields():
    request_data = get_base_request()
    request_data["apellidosEntrega"] = ""
    response = requests.post(BASE_URL, json=request_data)
    response_data = response.json()
    
    # validations
    assert response.status_code == 400
    assert response_data["isError"] == True
    assert "apellidosEntrega" in response_data["cause"]
    assert "is not allowed to be empty" in response_data["cause"]

def test_invalid_date_format():
    request_data = get_base_request()
    request_data["fechaRecogida"] = "fecha-invalida"
    response = requests.post(BASE_URL, json=request_data)
    response_data = response.json()
    
    # validations
    assert response.status_code == 200
    assert response_data["isError"] == True
    assert "debe tener un formato valido" in response_data["data"]["message"]

if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",
        "--html=./reports/html_reports/report.html",
        "--self-contained-html",
        "--capture=tee-sys"
    ])