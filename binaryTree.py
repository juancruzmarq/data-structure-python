# Binary Tree in Python
# Author: Juan Cruz Marquez
# Date: 2023-01-05

# Que es un binary tree?
# Un binary tree es una estructura de datos que consiste en un nodo raiz, nodos hijos y nodos padres. Cada nodo puede tener un maximo de dos hijos.

# Que es un nodo raiz?
# El nodo raiz es el nodo principal de un binary tree. El nodo raiz no tiene un nodo padre.

# Que es un nodo hijo?
# Un nodo hijo es un nodo que tiene un nodo padre.

# Que es un nodo padre?
# Un nodo padre es un nodo que tiene un nodo hijo.

# Que es un nodo hoja?
# Un nodo hoja es un nodo que no tiene nodos hijos.

# Complejidad de los binary trees
# Search: O(n)
# Insert: O(n)
# Delete: O(n)
# Space: O(n)

# Tipos de binary trees
# Binary search tree: Un binary search tree es un binary tree donde cada nodo tiene un valor y todos los valores de los nodos hijos izquierdos son menores que el valor del nodo padre, y todos los valores de los nodos hijos derechos son mayores que el valor del nodo padre.
# AVL tree: Un AVL tree es un binary search tree balanceado. Un AVL tree esta balanceado si la diferencia de altura entre los subarboles izquierdo y derecho de cada nodo es menor o igual a 1.
# Binary heap: Un binary heap es un binary tree donde todos los nodos hijos izquierdos son menores que el valor del nodo padre, y todos los nodos hijos derechos son mayores que el valor del nodo padre.

# Creacion de la clase Node

class Node():
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
        # Traverse inorder

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

# Drawn tree
#       1
#      / \
#     2   3
#    /
#   4

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()
