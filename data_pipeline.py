import os
import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# ---- Configuración ----
SPECIES = [
    "Scomber scombrus", "Thunnus alalunga", "Seriola dumerili"
    # … añade tus 35 especies científicas aquí
]

OUTPUT_DIR = "downloads"
os.makedirs(OUTPUT_DIR, exist_ok=True)
CSV_FILE = "fish_species_full_data.csv"

# ---- Inicializar Selenium ----
chrome_opts = Options()
chrome_opts.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_opts)

# ---- Función para scrapear FishBase ----
def scrape_fishbase(species_name):
    base_url = "https://www.fishbase.de/summary/"
    url = base_url + species_name.replace(" ", "-") + ".html"
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data = {"scientific_name": species_name, "fishbase_url": url}

    def get_text(css):
        el = soup.select_one(css)
        return el.text.strip() if el else ""

    data.update({
        "common_name": get_text("font.BigChar"),
        "length_cm": get_text("td:contains('Max length') + td"),
        "habitat": get_text("td:contains('Habitat') + td"),
        "distribution": get_text("td:contains('Distribution') + td"),
        "diet": get_text("td:contains('Diet') + td")
    })
    return data

# ---- Función para consulta WoRMS (API pública simulada) ----
def query_worms(species_name):
    url = f"http://www.marinespecies.org/rest/AphiaRecordsByName/{species_name}?like=false&marine_only=true"
    r = requests.get(url)
    if r.ok and r.json():
        rec = r.json()[0]
        return {
            "aphia_id": rec.get("AphiaID", ""),
            "classification": rec.get("classification", "")
        }
    return {"aphia_id": "", "classification": ""}

# ---- Función ejemplo para descargar datos oceanográficos (Copernicus simulado) ----
def download_copernicus(species_name):
    # Simula descarga basada en especie
    fname = os.path.join(OUTPUT_DIR, f"{species_name}_copernicus.json")
    dummy = {"species": species_name, "sst": 23.5, "salinity": 35}
    with open(fname, "w") as f:
        import json
        json.dump(dummy, f)
    return fname

# ---- Función ejemplo para datos IEO DEMERSALES (simulado) ----
def query_ieo(species_name):
    # Simula extracción de abundancia
    return {"catch_kg_per_km2": round(100 * (0.5 + hash(species_name) % 50 / 100), 2)}

# ---- Pipeline principal ----
rows = []
for sp in SPECIES:
    print("Procesando:", sp)
    fb = scrape_fishbase(sp)
    wr = query_worms(sp)
    cop_fn = download_copernicus(sp)
    ieo = query_ieo(sp)

    row = {**fb, **wr, **ieo, "copernicus_file": cop_fn}
    rows.append(row)

driver.quit()

# ---- Exportar CSV ----
df = pd.DataFrame(rows)
df.to_csv(CSV_FILE, index=False)
print("CSV generado:", CSV_FILE)
