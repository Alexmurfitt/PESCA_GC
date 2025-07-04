import pandas as pd

# Cargar datos
df = pd.read_csv("../data/fishbase_data.csv")

# Normalizar columnas clave
df["Nombre común"] = df["Nombre común"].astype(str).str.strip().str.lower()
df["Alimentación"] = df["Alimentación"].astype(str).fillna("").str.lower()

# Clasificación trófica estimada
def clasificar_nivel_trofico(alimentacion):
    if any(p in alimentacion for p in ["peces", "crustáceos", "moluscos", "ictiófago", "depredador"]):
        return "carnívoro"
    elif any(p in alimentacion for p in ["algas", "detritos", "fitoplancton"]):
        return "herbívoro"
    elif any(p in alimentacion for p in ["invertebrados", "larvas", "anfípodos", "zooplancton"]):
        return "omnívoro"
    else:
        return "desconocido"

df["Nivel_trófico"] = df["Alimentación"].apply(clasificar_nivel_trofico)

# Crear relaciones tróficas inferidas
relaciones = []
for i, depredador in df.iterrows():
    for j, presa in df.iterrows():
        if i == j:
            continue
        if depredador["Nivel_trófico"] == "carnívoro" and presa["Nivel_trófico"] in ["herbívoro", "omnívoro"]:
            relaciones.append({"Depredador": depredador["Nombre común"], "Presa": presa["Nombre común"]})
        elif depredador["Nivel_trófico"] == "omnívoro" and presa["Nivel_trófico"] == "herbívoro":
            relaciones.append({"Depredador": depredador["Nombre común"], "Presa": presa["Nombre común"]})

# Guardar CSV
df_relaciones = pd.DataFrame(relaciones)
df_relaciones.to_csv("../red_trofica_inferida.csv", index=False)

print(f"🔎 Relaciones posibles evaluadas: {len(df) ** 2}")
print(f"✅ Relaciones inferidas: {len(df_relaciones)}")
