import csv
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

# Codigo principal
# Aqui a base de dados é lida e o grafo é colocado no dicionario para manipulacao

def load_graph_from_csv(file_path):
    graph = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                source = row[0]
                target = row[1]
                weight = int(row[2])

                if source not in graph:
                    graph[source] = []
                if target not in graph:
                    graph[target] = []

                graph[source].append((target, weight))
                graph[target].append((source, weight))
    return graph

# Aplicacao do Prim

def prim(graph, start_vertex):
    mst = []
    visited = set([start_vertex])
    edges = graph[start_vertex]
    while edges:
        edges.sort(key=lambda x: x[1])
        min_edge = edges.pop(0)
        if min_edge[0] not in visited:
            visited.add(min_edge[0])
            mst.append(min_edge)
            edges.extend(graph[min_edge[0]])
    return mst

def calculate_and_show_result():
    start_vertex = start_vertex_var.get()

    if not start_vertex:
        messagebox.showerror("Erro", "Digite um ponto inicial válido.")
        return

    csv_file_path = os.path.join(os.path.dirname(__file__), "grafo.csv")
    graph = load_graph_from_csv(csv_file_path)

    if start_vertex not in graph:
        messagebox.showerror("Erro", "Ponto inicial não encontrado no grafo.")
        return

    calculate_button.config(state=tk.DISABLED)

    minimum_spanning_tree = prim(graph, start_vertex)
    total_weight = sum(edge[1] for edge in minimum_spanning_tree)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Trajeto do algoritmo de Prim a partir de {start_vertex}:\n")
    for edge in minimum_spanning_tree:
        result_text.insert(tk.END, f"{edge[0]} - Peso: {edge[1]}\n")
    result_text.insert(tk.END, f"Peso total do trajeto: {total_weight}")

    new_query_button.config(state=tk.NORMAL)

def start_new_query():
    calculate_button.config(state=tk.NORMAL)
    new_query_button.config(state=tk.DISABLED)
    start_vertex_var.set("")
    result_text.delete(1.0, tk.END)

# Criacao da interface grafica abaixo

root = tk.Tk()
root.title("Calcule o trajeto mais econômico!")

frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

label = ttk.Label(frame, text="Digite o ponto inicial (sem acentuação):")
label.grid(column=0, row=0)

start_vertex_var = tk.StringVar()
start_vertex_entry = ttk.Entry(frame, textvariable=start_vertex_var)
start_vertex_entry.grid(column=1, row=0)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_and_show_result)
calculate_button.grid(column=2, row=0)

new_query_button = ttk.Button(frame, text="Nova consulta", command=start_new_query, state=tk.DISABLED)
new_query_button.grid(column=3, row=0)

result_text = ScrolledText(root, wrap=tk.WORD, height=10, width=60)
result_text.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

root.mainloop()
