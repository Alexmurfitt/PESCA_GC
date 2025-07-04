import os
import csv
from bs4 import BeautifulSoup

# Carpeta donde están los HTML guardados
input_dir = "fishbase_species"
output_csv = "fishbase_data.csv"
log_csv = "fishbase_scraper_log.csv"  # Donde tenemos nombres comunes + científicos + URL

# Leer el log para mapear nombre común <-> científico <-> URL
species_info = {}
with open(log_csv, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        common = row["Nombre común"]
        scientific = row["Nombre científico"]
        url = row["URL"]
        filename = os.path.basename(row["Archivo HTML"])
        species_info[filename] = {
            "Nombre común": common,
            "Nombre científico": scientific,
            "URL": url
        }

# Cabeceras del CSV final
headers = ["Nombre común", "Nombre científico", "Longitud máxima", "Peso máximo", "Distribución", "Alimentación", "IUCN", "URL"]

# Función de extracción desde HTML
def extract_info_from_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    def get_text(label):
        row = soup.find("td", string=label)
        if row:
            value = row.find_next_sibling("td")
            return value.get_text(strip=True) if value else ""
        return ""

    return {
        "Longitud máxima": get_text("Max length :"),
        "Peso máximo": get_text("Max. weight :"),
        "Distribución": get_text("Distribution"),
        "Alimentación": get_text("Feeding"),
        "IUCN": get_text("IUCN Red List Status")
    }

# Escritura del CSV final
with open(output_csv, mode="w", newline="", encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=headers)
    writer.writeheader()

    for filename in os.listdir(input_dir):
        if not filename.endswith(".html"):
            continue
        filepath = os.path.join(input_dir, filename)
        base_info = species_info.get(filename, {})
        extracted = extract_info_from_html(filepath)
        row = {
            **base_info,
            **extracted
        }
        writer.writerow(row)
        print(f"✅ Procesado: {base_info.get('Nombre común', filename)}")

print(f"\n📁 Datos guardados en: {output_csv}")
