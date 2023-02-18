# Stack's en python
# Author: Juan Cruz Marquez
# Date: 2023-01-02

# Que es un stack ?
# Un stack es una estructura de datos en donde los elementos se agregan y se remueven en el orden LIFO (Last In First Out).

# Que es LIFO?
# LIFO es un acronimo que significa Last In First Out. En este caso, el ultimo elemento que se agrega al stack es el primero en ser removido.

# Complejidad de los stacks:
# - Insertion: O(1)
# - Removal: O(1)
# - Searching: O(n)
# - Access: O(n)

# Creacion de la clase Stack
class Stack():
    def __init__(self):
        self.stack = []  # Creacion de la lista

    def push(self, item):
        self.stack.append(item)  # Agregar un elemento al stack

    def pop(self):
        if self.is_empty():  # Si el stack esta vacio, no se puede remover un elemento
            return None

        return self.stack.pop()  # Remover el ultimo elemento del stack

    def peek(self):
        if self.is_empty():  # Si el stack esta vacio, no se puede ver el ultimo elemento
            return None

        return self.stack[-1]  # Ver el ultimo elemento del stack

    def is_empty(self):
        return len(self.stack) == 0  # Verificar si el stack esta vacio

    def size(self):
        return len(self.stack)  # Ver el tamaño del stack

    def __len__(self):
        return self.size()  # Ver el tamaño del stack

    def __str__(self):
        return str(self.stack)  # Ver el stack como una cadena de texto


# Creacion del stack
stack = Stack()

# Agregar elementos al stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# Ver el stack
print("Stack: ", stack)

# Ver el tamaño del stack
print("Size: ", stack.size())

# Ver el ultimo elemento del stack
print("Peek: ", stack.peek())

# Remover el ultimo elemento del stack
stack.pop()
print("Pop: ", stack)

# Verificar si el stack esta vacio
print("Is empty: ", stack.is_empty())

# Ver el stack como una cadena de texto
print("Stack: ", stack)
