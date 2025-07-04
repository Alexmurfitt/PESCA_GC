import os
import csv
from bs4 import BeautifulSoup

input_dir = "fishbase_species"
output_file = "fishbase_data.csv"

# Campos a extraer (pueden variar según el HTML)
FIELDS = [
    "Species", "Family", "Max length", "Max weight",
    "Environment", "Climate", "Depth range", "Distribution"
]

def extract_info_from_html(html):
    soup = BeautifulSoup(html, "lxml")
    data = {field: "" for field in FIELDS}

    # Extraer la tabla general donde aparecen los datos clave
    rows = soup.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 2:
            key = cells[0].get_text(strip=True)
            val = cells[1].get_text(strip=True)
            for field in FIELDS:
                if field in key:
                    data[field] = val
    return data

# Leer todos los archivos HTML
with open(output_file, mode="w", newline="", encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=["Common Name"] + FIELDS)
    writer.writeheader()

    for filename in os.listdir(input_dir):
        if filename.endswith(".html"):
            common_name = filename.replace(".html", "").replace("_", " ").title()
            with open(os.path.join(input_dir, filename), encoding="utf-8") as f:
                html = f.read()
                fish_data = extract_info_from_html(html)
                fish_data["Common Name"] = common_name
                writer.writerow(fish_data)
                print(f"✅ Procesado: {common_name}")

print(f"\n📁 Datos guardados en: {output_file}")
