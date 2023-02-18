# Dijkstra's algorithm
# Author: Juan Cruz Marquez
# Date: 2023-01-18

# Que es el algoritmo de Dijkstra?
# El algoritmo de Dijkstra es un algoritmo que encuentra el camino mas corto entre un nodo origen y todos los demas nodos en un grafo dirigido con pesos no negativos.

# Que es un grafo?
# Un grafo es una estructura de datos que consiste en un conjunto de nodos conectados por aristas. Un grafo puede ser dirigido o no dirigido. Un grafo dirigido tiene aristas que solo se pueden recorrer en una direccion. Un grafo no dirigido tiene aristas que se pueden recorrer en ambas direcciones.

# Que es un nodo?
# Un nodo es un objeto que contiene un valor y una lista de punteros a los nodos adyacentes.

# Que es un puntero?
# Un puntero es una variable que contiene la direccion de memoria de otro objeto. En este caso, el puntero del nodo apunta a los nodos adyacentes.

# Complejidad de los grafos
# Search: O(n)
# Insert: O(n)
# Delete: O(n)
# Space: O(n)

# Creacion de el algoritmo de Dijkstra
import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Grafo ejemplo:
# https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3, 'C': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {},
    'E': {'D': 1}
}

print(dijkstra(graph, 'A'))
