import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання ребер (міста) і їх ваги (відстані)
edges = {
    ('Харків', 'Київ'): 477,
    ('Київ', 'Вінниця'): 268,
    ('Вінниця', 'Львів'): 380,
    ('Харків', 'Дніпро'): 232,
    ('Дніпро', 'Одеса'): 518,
    ('Одеса', 'Львів'): 872,
    ('Дніпро', 'Вінниця'): 260,
    ('Харків', 'Вінниця'): 580
}

for edge, weight in edges.items():
    G.add_edge(edge[0], edge[1], weight=weight)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:")
for node in G.nodes():
    print(f"{node}: {G.degree[node]}")
