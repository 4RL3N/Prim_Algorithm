import random
import csv
import os.path

# Codigo responsavel pela adicao de conexoes e pesos à base de dados original
# derivando uma nova base com essas informacoes chamada "grafo"

csv_filename = 'topCidadesBrasil.csv'
csv_path = os.path.join(os.path.dirname(__file__), csv_filename)

with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    cities = [row for row in reader]

graph = {}
for city in cities:
    num_edges = random.randint(1, 6)
    connected_cities = random.sample(cities, num_edges)
    edges = []

    for connected_city in connected_cities:
        if connected_city != city:
            distance = random.randint(1, 100)
            edges.append((connected_city['city'], distance))

    graph[city['city']] = edges

# Salva os dados do grafo em um arquivo CSV
with open('grafo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['source', 'target', 'weight'])

    for city, edges in graph.items():
        for edge in edges:
            writer.writerow([city, edge[0], edge[1]])