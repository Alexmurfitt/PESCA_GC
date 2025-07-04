import os
import csv
import requests
from time import sleep

# Directorio de salida
output_dir = "fishbase_species"
log_file = "fishbase_scraper_log.csv"
os.makedirs(output_dir, exist_ok=True)

# Diccionario de especies
species_dict = {
    "Vieja": "Sparisoma cretense",
    "Sama": "Dentex gibbosus",
    "Sama roquera": "Pagrus auriga",
    "Cherne": "Polyprion americanus",
    "Bocinegro": "Pagrus pagrus",
    "Atún": "Thunnus thynnus",
    "Rabil": "Thunnus albacares",
    "Bonito": "Sarda sarda",
    "Melva": "Auxis rochei",
    "Listado": "Katsuwonus pelamis",
    "Caballa": "Scomber scombrus",
    "Sardina": "Sardina pilchardus",
    "Jurel": "Trachurus trachurus",
    "Chicharro": "Caranx crysos",
    "Abade": "Mycteroperca fusca",
    "Mero": "Epinephelus marginatus",
    "Sargo": "Diplodus sargus",
    "Breca": "Pagellus erythrinus",
    "Morena": "Muraena helena",
    "Serrano": "Serranus cabrilla",
    "Cabrilla": "Epinephelus costae",
    "Bicuda": "Sphyraena viridensis",
    "Pejerrey": "Atherina presbyter",
    "Boga": "Boops boops",
    "Dorado": "Coryphaena hippurus",
    "Sierra": "Scomberomorus cavalla",
    "Anchete": "Balistes capriscus",
    "Palometa roja": "Lobotes surinamensis",
    "Fula colorada": "Anthias anthias",
    "Pámpano": "Trachinotus ovatus",
    "Rufo": "Scorpaena scrofa",
    "Bocanegra": "Acanthocybium solandri",
    "Cabracho": "Scorpaena porcus",
    "Medregal": "Seriola dumerili"
}

# Crear archivo CSV con cabecera
with open(log_file, mode="w", newline="", encoding="utf-8") as log:
    writer = csv.writer(log)
    writer.writerow(["Nombre común", "Nombre científico", "Estado", "Archivo HTML", "URL"])

# Headers para evitar bloqueo
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Función para descargar HTML directamente por URL de resumen
def download_fishbase_page(common_name, scientific_name):
    genus, species = scientific_name.split()
    url = f"https://www.fishbase.se/summary/{genus}-{species}.html"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200 and "summary" in response.url.lower():
            filename = os.path.join(output_dir, f"{common_name.replace(' ', '_')}.html")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"✅ {common_name}: encontrado")
            return ("Encontrado", filename, url)
        else:
            print(f"⚠️ No encontrado: {common_name}")
            return ("No encontrado", "", url)
    except Exception as e:
        print(f"❌ Error con {common_name}: {e}")
        return ("Error", "", url)

# Ejecución
with open(log_file, mode="a", newline="", encoding="utf-8") as log:
    writer = csv.writer(log)
    for common_name, scientific_name in species_dict.items():
        status, file_path, url = download_fishbase_page(common_name, scientific_name)
        writer.writerow([common_name, scientific_name, status, file_path, url])
        sleep(1.2)  # pausa entre peticiones para evitar bloqueo
