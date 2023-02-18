# Tree in Python
# Author: Juan Cruz Marquez
# Date: 2023-01-05

# Que es un arbol?
# Un arbol es una estructura de datos que consiste en un conjunto de nodos conectados por aristas. Un arbol tiene un nodo raiz y cada nodo tiene un padre y cero o mas hijos.

# Que es un nodo?
# Un nodo es un objeto que contiene un valor y una lista de punteros a los nodos hijos.

# Que es un puntero?
# Un puntero es una variable que contiene la direccion de memoria de otro objeto. En este caso, el puntero del nodo apunta a los nodos hijos.

# Que es un nodo raiz?
# El nodo raiz es el primer nodo del arbol. El nodo raiz no contiene un valor, solo apunta a los nodos hijos.

# Que es un nodo hoja?
# El nodo hoja es el ultimo nodo del arbol. El nodo hoja no contiene un valor, solo apunta a una lista vacia.

# Que es un edge o arista?
# Una arista es una conexion entre dos nodos. En este caso, una arista conecta un nodo padre con un nodo hijo.

# Complejidad de los arboles
# Search: O(n)
# Insert: O(n)
# Delete: O(n)
# Space: O(n)

# Tipos de arboles
# Arbol binario: Un arbol binario es un arbol donde cada nodo tiene cero, uno o dos hijos.
# Arbol binario de busqueda: Un arbol binario de busqueda es un arbol binario donde cada nodo tiene un valor y todos los valores de los nodos hijos izquierdos son menores que el valor del nodo padre, y todos los valores de los nodos hijos derechos son mayores que el valor del nodo padre.
# Arbol AVL: Un arbol AVL es un arbol binario de busqueda balanceado. Un arbol AVL esta balanceado si la diferencia de altura entre los subarboles izquierdo y derecho de cada nodo es menor o igual a 1.
# B-Tree: Un B-Tree es un arbol donde cada nodo tiene cero o mas hijos, y cada nodo tiene un valor. Los valores de los nodos hijos izquierdos son menores que el valor del nodo padre, y los valores de los nodos hijos derechos son mayores que el valor del nodo padre. Los nodos hoja estan en el mismo nivel.

from enum import Enum, auto


class Node():
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def inorder(root):  # Inorder traversal is a tree traversal technique that starts at the root node and explores all the nodes in the left subtree first, then the root node, and finally all the nodes in the right subtree.
    if root:
        inorder(root.left)
        print(str(root.value) + "->", end="")
        inorder(root.right)


def preorder(root):  # Preorder traversal is a tree traversal technique that starts at the root node and explores all the nodes in the left subtree first, then the right subtree.
    if root:
        print(str(root.value) + "->", end="")
        preorder(root.left)
        preorder(root.right)


def postorder(root):  # Postorder traversal is a tree traversal technique that starts at the root node and explores all the nodes in the left subtree first, then the right subtree, and finally the root node.
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value) + "->", end="")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Draw the tree
#       1
#      / \
#     2   3
#    / \
#   4   5

print("Inorder traversal: ", end="")
inorder(root)

print("\nPreorder traversal: ", end="")
preorder(root)

print("\nPostorder traversal: ", end="")
postorder(root)
