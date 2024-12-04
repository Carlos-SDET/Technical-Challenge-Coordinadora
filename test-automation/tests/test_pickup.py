from playwright.sync_api import Page
from helpers.api_helpers import get_base_request, modify_request

API_URL = "https://apiv2-test.coordinadora.com/recogidas/cm-solicitud-recogidas-ms/solicitud-recogida"

def test_successful_creation(page: Page):
    """E1: Creación exitosa de solicitud"""
    request_data = modify_request("successful")
    
    response = page.request.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        data=request_data
    )

    # Validaciones específicas
    assert response.status == 200, "Código de respuesta debe ser 200"
    response_data = response.json()
    assert not response_data["isError"], "isError debe ser false"
    assert "id_recogida" in response_data["data"], "Debe contener id_recogida"
    assert response_data["data"]["id_recogida"]["error"] == False, "error debe ser false"
    assert response_data["data"]["id_recogida"]["message"] == "Solicitud recogida programada exitosamente"

def test_duplicate_request(page: Page):
    """E2: Detección de duplicados"""
    request_data = modify_request("successful")
    
    # Primera solicitud
    response = page.request.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        data=request_data
    )
    
    # Segunda solicitud (duplicada)
    response = page.request.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        data=request_data
    )
    
    # Validaciones específicas
    assert response.status == 200, "Código de respuesta debe ser 200"
    response_data = response.json()
    assert response_data["isError"], "isError debe ser true"
    assert "Ya existe una recogida programada para hoy" in response_data["data"]["message"]
    assert "idRecogidaAnterior" in response_data["data"], "Debe contener idRecogidaAnterior"
    assert response_data["data"]["recogida_anterior"] == True

def test_invalid_date_format(page: Page):
    """E3: Formato de fecha inválido"""
    request_data = modify_request("invalid_date")
    
    response = page.request.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        data=request_data
    )
    
    # Validaciones específicas
    assert response.status == 200, "Código de respuesta debe ser 200"
    response_data = response.json()
    assert response_data["isError"], "isError debe ser true"
    assert response_data["data"]["message"] == "El campo fecha debe ser diferente de vacio y debe tener un formato valido."
    assert response_data["data"]["recogida_anterior"] == True

def test_future_date(page: Page):
    """E4: Fecha fuera de rango (> 5 días hábiles)"""
    request_data = modify_request("future_date")
    
    response = page.evaluate('''async (data) => {
        const response = await fetch('%s', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const responseData = await response.json();
        return {
            status: response.status,
            data: responseData
        };
    }''' % API_URL, request_data)
    
    # Validaciones específicas
    assert response["status"] == 200, "Código de respuesta debe ser 200"
    assert response["data"]["isError"], "isError debe ser true"
    assert "no debe ser mayor a la fecha" in response["data"]["data"]["message"]
    assert "idRecogidaAnterior" in response["data"]["data"]
    assert response["data"]["data"]["recogida_anterior"] == True

def test_missing_fields(page: Page):
    """E5: Campos obligatorios faltantes"""
    request_data = modify_request("missing_fields")
    
    response = page.evaluate('''async (data) => {
        const response = await fetch('%s', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const responseData = await response.json();
        return {
            status: response.status,
            data: responseData
        };
    }''' % API_URL, request_data)
    
    # Validaciones específicas
    assert response["status"] == 400, "Código de respuesta debe ser 400"
    assert response["data"]["isError"], "isError debe ser true"
    assert response["data"]["message"] == "Los valores de entrada no son correctos."
    assert response["data"]["code"] == "BAD_MESSAGE"
    assert "apellidosEntrega" in response["data"]["cause"]
    assert "is not allowed to be empty" in response["data"]["cause"]
    assert response["data"]["statusCode"] == 400

if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",
        "--html=./reports/html_reports/report.html",
        "--self-contained-html",
        "--capture=tee-sys"
    ])