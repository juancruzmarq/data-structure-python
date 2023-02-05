# Queue en python
# Author: Juan Cruz Marquez
# Date: 2023-01-02

# Que es una queue?
# Una queue es una estructura de datos en donde los elementos se agregan y se remueven en el orden FIFO (First In First Out).

# Que es FIFO?
# FIFO es un acronimo que significa First In First Out. En este caso, el primer elemento que se agrega a la queue es el primero en ser removido.

# Complejidad de las queues:
# - Insertion: O(1)
# - Removal: O(1)
# - Searching: O(n)
# - Access: O(n)

# Tipos de queues:
# - Simple Queue (FIFO) - La queue mas comun
# - Priority Queue (FIFO) - En este caso, los elementos se ordenan por prioridad y se remueven en el orden FIFO
# - Double Ended Queue (FIFO) - En este caso, los elementos se pueden agregar y remover tanto al principio como al final de la queue
# - Circular Queue (FIFO) - En este caso, la queue es circular, es decir, cuando se agrega un elemento al final de la queue, el primer elemento de la queue es removido


# Creacion de la clase Queue
class Queue():
    def __init__(self):
        self.queue = []  # Creacion de la lista

    def enqueue(self, item):
        self.queue.insert(0, item)  # Agregar un elemento a la queue

    def dequeue(self):
        if self.is_empty():  # Si la queue esta vacia, no se puede remover un elemento
            return None

        return self.queue.pop()  # Remover el primer elemento de la queue

    def peek(self):
        if self.is_empty():  # Si la queue esta vacia, no se puede ver el primer elemento
            return None

        return self.queue[-1]  # Ver el primer elemento de la queue

    def is_empty(self):
        return len(self.queue) == 0  # Verificar si la queue esta vacia

    def size(self):
        return len(self.queue)  # Ver el tamaño de la queue

    def __len__(self):
        return self.size()  # Ver el tamaño de la queue

    def __str__(self):
        return str(self.queue)  # Ver la queue como una cadena de texto


# Creacion de la queue
queue = Queue()

# Agregar elementos a la queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Ver la queue
print("Queue:", queue)

# Remover elementos de la queue
queue.dequeue()
print("Dequeue:", queue)

# Peek de la queue
print("Peek:", queue.peek())

# Verificar si la queue esta vacia
print("Is empty:", queue.is_empty())

# Ver el tamaño de la queue
print("Size:", queue.size())
