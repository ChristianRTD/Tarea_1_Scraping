import requests
from bs4 import BeautifulSoup

def obtener_html(url):
    """
    Obtiene el contenido HTML de una URL configurando un User-Agent
    para evitar bloqueos básicos.
    """
    try:
        # User-Agent completo para simular un navegador real
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        # Realizar la petición GET con un tiempo de espera de 10 segundos
        respuesta = requests.get(url, headers=headers, timeout=10)

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
    Analiza el HTML y extrae textos que coincidan con estructuras de titulares.
    """
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    titulos = []

    # 1. Buscar en etiquetas de encabezado (h1, h2, h3)
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        texto = heading.text.strip()
        # Filtro de longitud mínima para evitar capturar menús o botones cortos
        if texto and len(texto) > 15:
            titulos.append(texto)

    # 2. Buscar en elementos con clases CSS comúnmente usadas en sitios de noticias
    selectores_comunes = '.title, .headline, .article-title, .news-title'
    for elemento in soup.select(selectores_comunes):
        texto = elemento.text.strip()
        if texto and texto not in titulos:  # Evitar duplicados
            titulos.append(texto)

    return titulos

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    url_objetivo = "https://www.emol.com/"
    
    print(f"Iniciando extracción en: {url_objetivo}...")
    
    contenido = obtener_html(url_objetivo)
    
    if contenido:
        lista_titulares = extraer_titulos_noticias(contenido)
        
        if lista_titulares:
            print(f"\nSe han encontrado {len(lista_titulares)} posibles titulares:\n")
            for i, titulo in enumerate(lista_titulares, 1):
                print(f"{i}. {titulo}")
        else:
            print("No se encontraron titulares con los selectores actuales.")
    else:
        print("No se pudo procesar la página.")