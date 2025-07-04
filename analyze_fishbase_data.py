import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV
df = pd.read_csv("fishbase_data.csv")

# Limpiar columnas numéricas
def extract_number(value):
    if pd.isna(value):
        return None
    value = str(value).split()[0].replace(",", ".")
    try:
        return float(value)
    except:
        return None

df["Longitud_max_cm"] = df["Longitud máx."].apply(extract_number)
df["Peso_max_kg"] = df["Peso máx."].apply(extract_number)

# 1. Histograma de longitudes
plt.figure()
df["Longitud_max_cm"].dropna().hist(bins=10)
plt.title("Distribución de Longitud Máxima (cm)")
plt.xlabel("Longitud (cm)")
plt.ylabel("Número de especies")
plt.tight_layout()
plt.savefig("histograma_longitud.png")
plt.close()

# 2. Histograma de pesos
plt.figure()
df["Peso_max_kg"].dropna().hist(bins=10)
plt.title("Distribución de Peso Máximo (kg)")
plt.xlabel("Peso (kg)")
plt.ylabel("Número de especies")
plt.tight_layout()
plt.savefig("histograma_peso.png")
plt.close()

# 3. Gráfico circular de tipos de alimentación
plt.figure()
df["Alimentación"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Distribución por Tipo de Alimentación")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_alimentacion.png")
plt.close()

# 4. Estado de conservación (IUCN)
plt.figure()
df["Estado IUCN"].value_counts().plot(kind="bar")
plt.title("Especies por Estado de Conservación (IUCN)")
plt.xlabel("Estado")
plt.ylabel("Número de especies")
plt.tight_layout()
plt.savefig("barras_iucn.png")
plt.close()

print("✅ Gráficos generados: histograma_longitud.png, histograma_peso.png, pie_alimentacion.png, barras_iucn.png")
