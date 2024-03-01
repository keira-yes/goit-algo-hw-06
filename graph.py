import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs

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

# Запуск алгоритмів BFS та DFS
start = 'Харків'   
bfs_path = bfs(graph, start)
dfs_path = dfs(graph, start)

print("Шлях, знайдений за допомогою BFS:", bfs_path)
print("Шлях, знайдений за допомогою DFS:", dfs_path)