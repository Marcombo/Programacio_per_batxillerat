# Crear dos listas de números
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Método 1: Usando el operador de concatenación "+"
union1 = lista1 + lista2
print(union1)  # Resultado: [1, 2, 3, 4, 5, 6]

# Método 2: Usando el método extend()
union2 = lista1.copy()
union2.extend(lista2)
print(union2)  # Resultado: [1, 2, 3, 4, 5, 6]

# Método 3: Usando el método append() y un bucle for
union3 = lista1.copy()
for numero in lista2:
    union3.append(numero)
print(union3)  # Resultado: [1, 2, 3, 4, 5, 6]

# Método 4: Usando el método insert() y un bucle for
union4 = lista1.copy()
for i in range(len(lista2)):
    union4.insert(i + len(lista1), lista2[i])
print(union4)  # Resultado: [1, 2, 3, 4, 5, 6]

# Método 5: Usando el método += y la sintaxis de listas por comprensión
union5 = lista1.copy()
union5 += [numero for numero in lista2]
print(union5)  # Resultado: [1, 2, 3, 4, 5, 6]
