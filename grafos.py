import os
import csv
import networkx as nx
import matplotlib.pyplot as plt

# Codigo responsavel pelo visualizador de grafos
# Execute caso queira ver o grafo desenhado
# Grafo denso, para melhor visualizacao, utilize o zoom da interface

csv_file_path = os.path.join(os.path.dirname(__file__), "grafo.csv")

G = nx.Graph()

with open(csv_file_path, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        source = row["source"]
        target = row["target"]
        weight = int(row["weight"])
        G.add_edge(source, target, weight=weight)

pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()