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
    # Crear el objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Buscar todos los elementos que podrían contener títulos de noticias
    # Nota: Estos selectores son genéricos y pueden necesitar ajustes según el sitio web
    titulos = []

    # Buscar en elementos h1, h2, h3 que podrían contener títulos
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        # Filtrar solo los que parecen ser títulos de noticias (por ejemplo, con cierta longitud)
        if heading.text.strip() and len(heading.text.strip()) > 15:
            titulos.append(heading.text.strip())

    # Buscar también en elementos con clases comunes para títulos de noticias
    for elemento in soup.select('.title, .headline, .article-title, .news-title'):
        if elemento.text.strip() and elemento.text.strip() not in titulos:
            titulos.append(elemento.text.strip())

    return titulos

html = obtener_html("https://www.emol.com/")
print(extraer_titulos_noticias(html))