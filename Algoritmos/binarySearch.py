# Binary search algorithm
# Author: Juan Cruz Marquez
# Date: 2023-01-18

# Que es la busqueda binaria?
# La busqueda binaria es un algoritmo que encuentra un elemento en un arreglo ordenado en tiempo logaritmico.
# El algoritmo de busqueda binaria divide el arreglo en dos partes y compara el elemento a buscar con el elemento del medio. Si el elemento a buscar es menor que el elemento del medio, entonces el algoritmo busca en la primera mitad del arreglo. Si el elemento a buscar es mayor que el elemento del medio, entonces el algoritmo busca en la segunda mitad del arreglo. El algoritmo se repite hasta que el elemento a buscar es igual al elemento del medio o hasta que el arreglo se encuentra vacio.

# Complejidad de la busqueda binaria
# Search: O(log n)
# Insert: O(n)
# Delete: O(n)
# Space: O(n)

# Implementacion de la busqueda binaria

def binarySearch(arr, x):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1


# Ejemplo de uso
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 5))
print(binarySearch(arr, 10))
