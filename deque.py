#
# Deque en Python
# Author: Juan Cruz Marquez
# Date: 2023-01-05

# Que es una deque?
# Deque o cola de doble extremo es un tipo de cola en la que la inserción y extracción de elementos puede realizarse por delante o por detrás. Por tanto, no sigue la regla FIFO (primero en entrar, primero en salir).

# Complejidad de las deques:
# - Insertion: O(1)
# - Removal: O(1)
# - Searching: O(n)
# - Access: O(n)


class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
d.addRear(8.4)

# Ver la deque
print(d.items)

# Ver el tamaño de la deque
print("Tamaño de la deque: ", d.size())

# Ver si la deque esta vacia
print("¿La deque esta vacia?: ", d.isEmpty())

# Remover elementos de la deque
d.removeRear()
d.removeFront()

# Ver la deque
print(d.items)
