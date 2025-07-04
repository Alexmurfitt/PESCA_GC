import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Cargar relaciones inferidas
df = pd.read_csv("../red_trofica_inferida.csv")

# Crear grafo dirigido
G = nx.DiGraph()

for _, row in df.iterrows():
    depredador = row["Depredador"]
    presa = row["Presa"]
    G.add_edge(depredador, presa)

# Visualizar
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=0.5, iterations=50)
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1200)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10)
plt.title("Red Trófica Inferida", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()
