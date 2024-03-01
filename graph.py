import networkx as nx
import matplotlib.pyplot as plt

# Представлення графа за допомогою списку суміжності
graph = {
    'Харків': ['Київ', 'Дніпро', 'Вінниця'],
    'Київ': ['Харків', 'Вінниця'],
    'Вінниця': ['Київ', 'Львів', 'Дніпро', 'Харків'],
    'Дніпро': ['Харків', 'Одеса', 'Вінниця'],
    'Одеса': ['Дніпро', 'Львів'],
    'Львів': ['Вінниця', 'Одеса']
}

# Створення графа
G = nx.Graph(graph)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2500, node_color="skyblue", font_size=10)
plt.title("Транспортна мережа")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:")
for node in G.nodes():
    print(f"{node}: {G.degree[node]}")