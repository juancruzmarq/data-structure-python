# Heap in python
# Author: Juan Cruz Marquez
# Date: 2023-01-05

# Que es un heap?
# Un heap es una estructura de datos que es similar a una cola de prioridad. En un heap, los elementos tienen una prioridad asociada con ellos. Un elemento con prioridad mas alta es servido antes que un elemento con prioridad mas baja. Si dos elementos tienen la misma prioridad, son servidos segun su orden de llegada.

# Max heap
# En un max heap, el elemento con la prioridad mas alta es el elemento mas grande. En un max heap, el padre es siempre mayor que sus hijos.

# Min heap
# En un min heap, el elemento con la prioridad mas alta es el elemento mas pequeño. En un min heap, el padre es siempre menor que sus hijos.

# Complejidad de los heaps:
# Search: O(n)
# Insert: O(log n)
# Delete: O(log n)
# Space: O(n)

# Creacion de la clase Heap

def heapify(arr, n, i):  # heapify function to create heap using array elements
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:  # See if left child of root exists and is greater than root
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)

    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
