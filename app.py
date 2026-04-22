import csv
import requests
from bs4 import BeautifulSoup

def obtener_html(url):
    """
    Obtiene el contenido HTML de una URL

    Args:
        url: La URL de la página web a descargar

    Returns:
        str: El contenido HTML de la página, o None si hay un error
    """
    try:
        # Configurar el User-Agent para evitar bloqueos
        # Se completa el string para que sea un User-Agent válido
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        # Realizar la petición GET
        respuesta = requests.get(url, headers=headers, timeout=10)

        # Verificar si la petición fue exitosa
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            print(f"Error al obtener la página: Código de estado {respuesta.status_code}")
            return None

    except Exception as e:
        print(f"Error al obtener la página: {e}")
        return None

def extraer_titulos_noticias(html):
    """
    Extrae los títulos de noticias de una página HTML

    Args:
        html: El contenido HTML de la página

    Returns:
        list: Lista de títulos de noticias encontrados
    """