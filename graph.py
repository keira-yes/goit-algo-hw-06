import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra

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
start_vertex = 'Харків'

print("Шлях, знайдений за допомогою BFS:")
bfs(graph, start_vertex)
print()
print("Шлях, знайдений за допомогою DFS:")
dfs(graph, start_vertex)
print()

# Представлення графа з вагами за допомогою списку суміжності
graph_weight = {
    'Харків': {'Київ': 477, 'Дніпро': 232, 'Вінниця': 580},
    'Київ': {'Харків': 477, 'Вінниця': 268},
    'Вінниця': {'Київ': 268, 'Львів': 380, 'Дніпро': 260, 'Харків': 580},
    'Дніпро': {'Харків': 232, 'Одеса': 518, 'Вінниця': 260},
    'Одеса': {'Дніпро': 518, 'Львів': 872},
    'Львів': {'Вінниця': 380, 'Одеса': 872}
}

# Знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
shortest_paths = dijkstra(graph_weight, start_vertex)
print(f"Найкоротші шляхи з вершини {start_vertex}:", shortest_paths)