import heapq
import networkx as nx
import matplotlib.pyplot as plt

# --- Створення власного зваженого графа ---
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "Z", weight=6)
G.add_edge("E", "Z", weight=3)

# --- Реалізація алгоритму Дейкстри ---
def dijkstra(graph, start):
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів
    у зваженому графі з використанням бінарної купи (heapq).
    """
    # 1. Ініціалізація
    shortest_paths = {vertex: float("infinity") for vertex in graph}
    shortest_paths[start] = 0
    visited = set()

    # 2. Пріоритетна черга (купа), елементи: (вага, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        # 3. Вибір вершини з мінімальною вагою
        current_dist, current_vertex = heapq.heappop(priority_queue)

        # Якщо вершина вже оброблена, пропускаємо
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # 4. Оновлення сусідів
        for neighbor, attrs in graph[current_vertex].items():
            weight = attrs["weight"]
            distance = current_dist + weight

            # Якщо знайдено коротший шлях — оновлюємо
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# --- Використання алгоритму Дейкстри ---
shortest_paths = dijkstra(G, "A")
print("Найкоротші відстані від вершини A:")
for vertex, dist in shortest_paths.items():
    print(f"A → {vertex}: {dist}")

# --- Візуалізація графа ---
pos = nx.spring_layout(G, seed=42)  # для стабільного відображення
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")

plt.axis("off")
plt.show()