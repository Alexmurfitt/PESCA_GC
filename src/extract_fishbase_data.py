import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Lista de nombres comunes
peces = [
    "Vieja", "Sama", "Sama roquera", "Cherne", "Bocinegro", "Atún", "Rabil",
    "Bonito", "Melva", "Listado", "Caballa", "Sardina", "Jurel", "Chicharro",
    "Abade", "Mero", "Sargo", "Breca", "Morena", "Serrano", "Cabrilla", "Bicuda",
    "Pejerrey", "Boga", "Dorado", "Sierra", "Anchete", "Palometa roja",
    "Fula colorada", "Pámpano", "Rufo", "Bocanegra", "Cabracho", "Medregal"
]

BASE_URL = "https://www.fishbase.se/search.php"

def obtener_datos(nombre_comun):
    params = {"lang": "English", "Search": "commonname", "commonname": nombre_comun}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar enlace a la página de especie
        link = soup.find('a', string="Species Summary")
        if not link:
            return None
        
        species_url = "https://www.fishbase.se/" + link['href']
        species_response = requests.get(species_url, timeout=10)
        species_response.raise_for_status()
        species_soup = BeautifulSoup(species_response.text, 'html.parser')

        # Extraer información relevante
        nombre_cientifico = species_soup.find("font", string="Scientific Name").find_next("b").text.strip()
        longitud = species_soup.find("td", string="Max length :")
        peso = species_soup.find("td", string="Max weight :")
        distribucion = species_soup.find("td", string="Distribution").find_next("td").text.strip()
        dieta = species_soup.find("td", string="Feeds on").find_next("td").text.strip()
        
        return {
            "Nombre común": nombre_comun,
            "Nombre científico": nombre_cientifico,
            "Longitud máxima": longitud.find_next("td").text.strip() if longitud else "",
            "Peso máximo": peso.find_next("td").text.strip() if peso else "",
            "Distribución": distribucion,
            "Alimentación": dieta,
            "URL": species_url
        }
    except Exception as e:
        print(f"❌ Error con {nombre_comun}: {e}")
        return None

# Extraer datos
datos = []
for nombre in peces:
    resultado = obtener_datos(nombre)
    if resultado:
        datos.append(resultado)
        print(f"✅ Extraído: {nombre}")
    else:
        print(f"⚠️ Sin datos: {nombre}")
    time.sleep(2)  # para no saturar el servidor

# Guardar en CSV
df = pd.DataFrame(datos)
df.to_csv("fishbase_data.csv", index=False)
print("\n✅ Datos guardados en fishbase_data.csv")
