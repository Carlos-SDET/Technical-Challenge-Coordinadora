import json

REQUEST_JSON = '''
{
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
    "ciudadDetalle": {
        "nombre_terminal_operativa": "Medellin",
        "tipo_servicio": "A",
        "dane_ciudad": "05266",
        "dane_actual": "05266000",
        "ciudad_tarifa": "05266000",
        "sms": true,
        "cubre_mqp": true,
        "codigo_postal": "055428",
        "terminal_operativa": 2,
        "cubre_me": true,
        "area_telefono": 4,
        "observaciones2": "FCE - RD - FD - RCE",
        "codigo": "05266000",
        "tipo_poblacion": "D",
        "activo": true,
        "codigo_terminal": 2,
        "codigo_interno": 204,
        "mensajeria": true,
        "cubre_mm": false,
        "departamento": "05",
        "cubre_cm": false,
        "nombre": "Envigado (Ant)",
        "abreviado": "ENVIGADO",
        "nombre_terminal": "Medellin",
        "observaciones": ""
    },
    "direccion": "Cr 80 # 82-62",
    "fechaRecogida": "2024-12-05",
    "nombreEntrega": "Carlos",
    "apellidosEntrega": "Posada",
    "celularEntrega": "3001234567",
    "emailUsuario": "carlos.posada@gmail.com",
    "descripcionTipoVia": "Calle",
    "aplicativo": "envios"
}
'''