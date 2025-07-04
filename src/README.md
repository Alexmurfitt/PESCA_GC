# 🐟 PESCA_GC – Análisis y Modelado de Redes Tróficas en Canarias

📍 **Ubicación del proyecto:** `~/code/labs/PESCA_GC`  
📁 **Carpeta principal de scripts:** `src/`  
🧪 **Entorno virtual:** `venv/`  

---

## 🎯 OBJETIVOS CLAVE DEL PROYECTO

El proyecto tiene como meta general **obtener, analizar, modelar y visualizar redes tróficas marinas** en el litoral de Canarias, con el más alto nivel de precisión, trazabilidad y resolución espacio-temporal.

### 1. Modelar relaciones tróficas y patrones espaciales de distribución  
- Inferir relaciones **presa-depredador** usando datos biológicos, coocurrencia y hábitos alimenticios.  
- Detectar zonas óptimas de pesca por especie y periodo.

### 2. Construir informes y mapas tróficos trazables  
- Generar informes visuales y mapas con trazabilidad espacio-temporal.

### 3. Obtener datos de abundancia por especie, zona y periodo  
- Recoger datos cuantificables, verificables y con base real de campo o base científica (como FishBase).

### 4. Identificar las especies más abundantes por zona y periodo  
- Estimar dominancia relativa por contexto espaciotemporal.

### 5. Determinar relaciones tróficas por zona y periodo  
- Verificar qué especies depredan o son depredadas y cómo varía la red por época y localización.

### 6. Modelar zonas óptimas de pesca por especie y época del año  
- Aplicar inferencias tróficas + datos de abundancia para localizar mejores momentos y lugares para pesca.

### 7. Visualizar la cadena trófica real  
- Mostrar gráficamente la red de interacciones por especie, zona y periodo.

---

## ✅ FASES COMPLETADAS

### 📌 1. Preparación y limpieza del entorno
- ✅ Estructura de carpetas organizada (`src`, `data`, `notebooks`, etc.)
- ✅ Activación del entorno virtual con dependencias correctas.

### 📌 2. Carga y procesamiento de datos
- ✅ `data/fishbase_data.csv` cargado correctamente.
- ✅ Limpieza del dataset y filtrado por especies relevantes.
- ✅ Normalización de campos clave (`Nombre_común`, `Dieta`, `Hábitat`, etc.)

### 📌 3. Inferencia de relaciones tróficas
- ✅ Script `modelar_red_trofica.py` funcional.
- ✅ Se han inferido correctamente 6 relaciones tróficas.
- ✅ Archivo generado: `red_trofica_inferida.csv`.

### 📌 4. Visualización inicial de red trófica
- ✅ Script `visualizar_red_trofica.py` funcionando (pendiente de refinar diseño).
- ✅ Se genera red trófica con `networkx` y `matplotlib`.

---

## 🔧 TAREAS PENDIENTES

### 🛠️ Mejora de scripts y visualizaciones
- [ ] Mejorar la representación visual del grafo trófico con:
  - Colores por nivel trófico o grupo funcional.
  - Exportación automática como imagen (`.png` o `.svg`).
- [ ] Añadir leyendas, etiquetas y estadísticas básicas del grafo.

### 📊 Análisis espaciotemporal real
- [ ] Integrar datos de **zonas geográficas** y **periodos mensuales/estacionales**.
- [ ] Filtrar abundancia relativa por zona y periodo (a partir de un dataset externo).

### 🧠 Modelado predictivo
- [ ] Construir modelos para predecir:
  - Abundancia probable según zona/época.
  - Probabilidad de interacción trófica nueva.

### 📋 Informes automáticos
- [ ] Generar informes PDF o HTML por zona y periodo.
- [ ] Incluir red trófica + lista de especies + datos de abundancia.

### 🗺️ Mapas geográficos (opcional)
- [ ] Usar `geopandas` o `folium` para mapear zonas óptimas de pesca por especie.

---

## 📦 ESTRUCTURA DEL PROYECTO

```

PESCA\_GC/
├── data/
│   ├── fishbase\_data.csv
│   └── red\_trofica\_inferida.csv
├── src/
│   ├── modelar\_red\_trofica.py
│   ├── visualizar\_red\_trofica.py
│   └── utils.py (futuro módulo de funciones comunes)
├── notebooks/ (opcional)
│   └── exploracion\_datos.ipynb
├── venv/ (entorno virtual)
├── README.md
└── requirements.txt

```

---

## 🧠 PRINCIPIO FUNDAMENTAL DEL PROYECTO

Todo el sistema se fundamenta en el **uso de datos reales, verificables y trazables** sobre especies, zonas y periodos. El rigor ecológico y la fidelidad a la evidencia biológica son prioritarios.

---

## ✍️ Autor y contacto

**Alexander Murfitt Santana**  
📍 Gran Canaria  
📬 [Email / contacto opcional aquí]  
```

