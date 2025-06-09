import json
import datetime
import logging

import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def set_Register(chamber, partNum, serie, leak, user=7172, state=0, retries=3, timeout=3):
    """
    Envía un registro a la API.

    :param chamber: Número de cabina
    :param partNum: Código de la pieza
    :param serie: Número de serie
    :param leak: Valor de fuga
    :param user: ID del operador (por defecto 7172)
    :param state: Estado del registro (por defecto 0)
    :param retries: Número de reintentos en caso de error (por defecto 3)
    :param timeout: Tiempo máximo de espera para la respuesta (segundos)
    :return: True si el registro fue exitoso, False en caso de error
    """
    url = 'http://10.1.0.187:8086/registros'
    data = {
        "proveedor": "ZAR",
        "cabina": chamber,
        "codigo": str(partNum),
        "serie": str(serie),
        "fuga": leak,
        "operador": user,
        "estado": state
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=timeout)

            # Si la respuesta es exitosa
            if response.status_code == 201:
                logging.info(f"Registro exitoso: {response.json()}")
                return True
            else:
                logging.warning(f"Intento {attempt}/{retries} - Error {response.status_code}: {response.text}")

        except Timeout:
            logging.error(f"Intento {attempt}/{retries} - Error: Tiempo de espera agotado (timeout={timeout}s)")
        except ConnectionError:
            logging.error(f"Intento {attempt}/{retries} - Error: No se pudo conectar con la API. Verificar red/WIFI")
        except RequestException as e:
            logging.error(f"Intento {attempt}/{retries} - Error inesperado en la solicitud: {e}")

    logging.error("Fallaron todos los intentos, no se pudo registrar el dato")
    return False

def Get_totalCores(partNum):
    try:
        url = f"http://10.1.0.187:8086/registros/{partNum}/?consulta=total"

        # Encabezados de la solicitud
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Envío de la solicitud GET
        response = requests.get(url, headers=headers)

        # Verifica la respuesta
        if response.status_code == 201:  # Código 200 indica éxito en GET
            data = response.json()  # Convertir la respuesta a JSON
            # print(data.get("data"))
            return data.get("data")  # Devolver solo el contenido de "data"

        else:
            # print(f"Error {response.status_code}: {response.text}")
            return 0
    except Exception as e:
        print("Error en la connexion con la API, Verificar WIFI")