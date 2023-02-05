# Hash Tables in Python
# Author: Juan Cruz Marquez
# Date: 2023-01-05

# Que es una hash table?
# Una hash table es una estructura de datos que consiste en una tabla de datos que contiene una lista de valores. Cada valor tiene una clave asociada a el. La clave es un valor que se utiliza para acceder al valor en la tabla de datos.

# Complejidad de las hash tables:
# Search: O(1)
# Insert: O(1)
# Delete: O(1)
# Space: O(n)

# Creacion de la clase HashTable
hashTable = [[],] * 10


def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]


def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0


insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)
