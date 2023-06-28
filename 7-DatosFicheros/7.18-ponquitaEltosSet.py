# Crear un conjunto con los primeros 5 números
set1 = {1, 2, 3, 4, 5}
print(set1)

# Agregar un elemento al conjunto con add()
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

# Agregar múltiples elementos al conjunto con update()
set1.update([7, 8, 9])
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {10,11}
set1.update(set2)
print(set1) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Eliminar un elemento específico del conjunto con remove()
try:
    set1.remove(99)
except:
    print("El número 99 no existe en el set")
set1.remove(3)
print(set1)  # Output: {1, 2, 4, 5, 6, 7, 8, 9, 10, 11}

# Eliminar un elemento específico del conjunto con discard()
set1.discard(99) #si no existe no da error
set1.discard(8)
print(set1)  # Output: {1, 2, 4, 5, 6, 7, 9, 10, 11}

# Limpiar el conjunto con clear()
set1.clear()
print(set1)  # Output: set()
