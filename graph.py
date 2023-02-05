# Graph in Python
# Author: Juan Cruz Marquez
# Date: 2023-01-05

# Que es un grafo?
# Un grafo es una estructura de datos que consiste en un conjunto de nodos y enlaces entre ellos. Los nodos son los vertices y los enlaces son las aristas.

# Que es un nodo?
# Un nodo es un punto en un grafo.

# Que es un enlace?
# Un enlace es una conexion entre dos nodos.

# Que es un grafo dirigido?
# Un grafo dirigido es un grafo donde las aristas tienen una direccion.

# Que es un grafo no dirigido?
# Un grafo no dirigido es un grafo donde las aristas no tienen una direccion.

# Que es un grafo ponderado?
# Un grafo ponderado es un grafo donde las aristas tienen un peso.

# Que es la adjacencia?
# La adjacencia es la relacion entre dos nodos.

# Como se representa un grafo?
# Un grafo se representa con una matriz de adyacencia.
# Donde cada fila y columna representa un nodo y cada celda representa la relacion entre dos nodos.


# Complejidad de los grafos
# Search: O(n)
# Insert: O(n)
# Delete: O(n)
# Space: O(n)

# Tipos de grafos
# Grafo dirigido: Un grafo dirigido es un grafo donde las aristas tienen una direccion.
# Grafo no dirigido: Un grafo no dirigido es un grafo donde las aristas no tienen una direccion.
# Grafo ponderado: Un grafo ponderado es un grafo donde las aristas tienen un peso.
# Grafo no ponderado: Un grafo no ponderado es un grafo donde las aristas no tienen un peso.
# Grafo conexo: Un grafo conexo es un grafo donde todos los nodos estan conectados.
# Grafo no conexo: Un grafo no conexo es un grafo donde no todos los nodos estan conectados.
# Grafo aciclico: Un grafo aciclico es un grafo donde no hay ciclos.
# Grafo ciclico: Un grafo ciclico es un grafo donde hay ciclos.
# Grafo bipartito: Un grafo bipartito es un grafo donde los nodos se pueden dividir en dos grupos de nodos donde cada nodo en un grupo esta conectado a un nodo en el otro grupo.
# Grafo no bipartito: Un grafo no bipartito es un grafo donde los nodos no se pueden dividir en dos grupos de nodos donde cada nodo en un grupo esta conectado a un nodo en el otro grupo.

# Adjacency Matrix representation in Python


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        # Print the first row
        print("   ", end=" ")
        for i in range(self.size):
            print(i, end=" ")
        print()
        print("_" * (self.size * 3))

        for i in range(self.size):
            print(i, end=" ")
            print("|", end=" ")
            for j in range(self.size):
                print(self.adjMatrix[i][j], end=" ")
            print()


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_matrix()
