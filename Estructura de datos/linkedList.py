# Linked List en python
# Author: Juan Cruz Marquez
# Date: 2023-01-02

# Que es una lista enlazada?
# Una lista enlazada es una estructura de datos que consiste en una secuencia de nodos, donde cada nodo contiene un valor y un puntero al siguiente nodo.

# Que es un nodo?
# Un nodo es un objeto que contiene un valor y un puntero al siguiente nodo.

# Que es un puntero?
# Un puntero es una variable que contiene la direccion de memoria de otro objeto. En este caso, el puntero del nodo apunta al siguiente nodo.

# Que es un nodo cabeza?
# El nodo cabeza es el primer nodo de la lista enlazada. El nodo cabeza no contiene un valor, solo apunta al primer nodo de la lista.

# Que es un nodo cola?
# El nodo cola es el ultimo nodo de la lista enlazada. El nodo cola no contiene un valor, solo apunta a None.

# Que es None?
# None es un valor especial que significa que no hay nada. En este caso, el nodo cola apunta a None.

# Que es un nodo vacio?
# Un nodo vacio es un nodo que no contiene un valor, solo apunta al siguiente nodo.

# Que es un nodo con valor?
# Un nodo con valor es un nodo que contiene un valor, y apunta al siguiente nodo.

# Creacion de la clase Node
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None

# Creacion de la clase LinkedList


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, item):
        node = Node(item)  # Creacion del nodo
        # El puntero del nodo apunta al nodo cabeza actual (None)
        node.next = self.head
        self.head = node  # El nodo cabeza apunta al nuevo nodo

    def insertAfter(self, prevNode, item):
        if prevNode is None:  # Si el nodo previo es None, no se puede insertar el nuevo nodo
            print("El nodo previo no puede ser None")
            return

        node = Node(item)  # Creacion del nodo
        # El puntero del nodo apunta al nodo siguiente del nodo previo
        node.next = prevNode.next
        prevNode.next = node  # El puntero del nodo previo apunta al nuevo nodo

    def insertAtEnd(self, item):
        node = Node(item)

        if self.head is None:  # Si el nodo cabeza es None, el nuevo nodo sera el nodo cabeza
            self.head = node
            return

        last = self.head  # Se crea un nodo auxiliar que apunta al nodo cabeza
        while last.next:  # Mientras el nodo auxiliar apunte a un nodo, se recorre la lista enlazada
            last = last.next  # El nodo auxiliar apunta al siguiente nodo

        last.next = node  # El puntero del ultimo nodo apunta al nuevo nodo

    def deleteNode(self, position):
        if self.head is None:  # Si el nodo cabeza es None, no se puede eliminar un nodo
            return

        temp = self.head  # Se crea un nodo auxiliar que apunta al nodo cabeza

        if position == 0:  # Si la posicion es 0, se elimina el nodo cabeza
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):  # Se recorre la lista enlazada hasta la posicion - 1
            temp = temp.next  # El nodo auxiliar apunta al siguiente nodo
            if temp is None:  # Si el nodo auxiliar es None, no se puede eliminar un nodo
                break

        if temp is None:  # Si el nodo auxiliar es None, no se puede eliminar un nodo
            return

        if temp.next is None:  # Si el nodo siguiente del nodo auxiliar es None, no se puede eliminar un nodo
            return

        # Se crea un nodo auxiliar que apunta al nodo siguiente del nodo siguiente del nodo auxiliar
        next = temp.next.next

        temp.next = None  # Se elimina el nodo siguiente del nodo auxiliar

        temp.next = next  # El puntero del nodo auxiliar apunta al nodo auxiliar

    def search(self, item):
        temp = self.head  # Se crea un nodo auxiliar que apunta al nodo cabeza
        while temp is not None:  # Mientras el nodo auxiliar no sea None, se recorre la lista enlazada
            if temp.value == item:  # Si el valor del nodo auxiliar es igual al valor buscado, se retorna True
                return True
            temp = temp.next  # El nodo auxiliar apunta al siguiente nodo
        return False  # Si el nodo auxiliar es None, se retorna False

    def sort(self, head):
        current = head  # Nodo auxiliar que apunta al nodo cabeza
        index = Node(None)  # Nodo auxiliar que apunta a None

        if head is None:  # Si el nodo cabeza es None, no se puede ordenar la lista enlazada
            return
        else:
            while current is not None:  # Mientras el nodo auxiliar no sea None, se recorre la lista enlazada
                index = current.next  # El nodo auxiliar apunta al siguiente nodo

                while index is not None:  # Mientras el nodo auxiliar no sea None, se recorre la lista enlazada
                    if current.value > index.value:  # Si el valor del nodo auxiliar es mayor al valor del nodo auxiliar, se intercambian valores
                        # Se crea una variable temporal que almacena el valor del nodo auxiliar
                        temp = current.value
                        # El valor del nodo auxiliar es igual al valor del nodo auxiliar
                        current.value = index.value
                        index.value = temp  # El valor del nodo auxiliar es igual a la variable temporal
                    index = index.next  # El nodo auxiliar apunta al siguiente nodo
                current = current.next  # El nodo auxiliar apunta al siguiente nodo

    def printList(self):
        temp = self.head
        while temp:
            print(str(temp.value) + " ", end="")
            temp = temp.next

# Complejidad de la lista enlazada
# La complejidad de la lista enlazada es O(n) ya que se recorre la lista enlazada una sola vez.
# De insercion y eliminacion de nodos, la complejidad es O(1) ya que se agrega o elimina un nodo al principio de la lista enlazada.

# Tipos de lista enlazada:
# Lista enlazada simple: Cada nodo apunta al siguiente nodo.
# Lista enlazada doble: Cada nodo apunta al siguiente nodo y al nodo anterior.
# Lista enlazada circular: El ultimo nodo apunta al primer nodo.


# Nueva lista enlazada
linkedList = LinkedList()
linkedList.head = Node(2)
first = Node(1)
second = Node(3)
third = Node(4)
fourth = Node(5)

linkedList.head.next = first
first.next = second
second.next = third
third.next = fourth

# Implementacion del metodo insertAtBeginning
print("Lista enlazada simple: Metodo insertAtBeginning()")
linkedList.insertAtBeginning(0)
linkedList.printList()

# Implementacion del metodo insertAfter
print(" \nLista enlazada simple: Metodo insertAfter()")
linkedList.insertAfter(linkedList.head.next, 14)
linkedList.printList()

# Implementacion del metodo insertAtEnd
print(" \nLista enlazada simple: Metodo insertAtEnd()")
linkedList.insertAtEnd(6)
linkedList.printList()

# Implementacion del metodo deleteNode
print(" \nLista enlazada simple: Metodo deleteNode()")
linkedList.deleteNode(2)
linkedList.printList()

# Implementacion del metodo search
print(" \nLista enlazada simple: Metodo search()")
print(linkedList.search(2))

# Implementacion del metodo sort
print(" \nLista enlazada simple: Metodo sort()")
linkedList.sort(linkedList.head)
linkedList.printList()

# Implementacion del metodo printList
print(" \nLista enlazada simple: Metodo printList()")
linkedList.printList()
