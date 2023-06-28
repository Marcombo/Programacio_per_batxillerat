# Crear dos conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print ("set1:", set1)
print ("set2:", set2)
# Unión
setUnion = set1.union(set2)
#setUnion = set1 | set2 #sintaxis alternativa
print("Unión:",setUnion)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección
setInterseccion = set1.intersection(set2)
#setInterseccion = set1 & set2 #sintaxis alternativa
print("Intersección:",setInterseccion)  # Output: {4, 5}

# Diferencia
setDiferencia = set1.difference(set2)
#setDiferencia = set1 - set2 #sintaxis alternativa
print("Diferencia:",setDiferencia)  # Output: {1, 2, 3}


# Diferencia simétrica
setDiferenciaSim = set1.symmetric_difference(set2)
#setDiferenciaSim = set1 ^ set2 #sintaxis alternativa
print("Dif. simétrica:",setDiferenciaSim)  # Output: {1, 2, 3, 6, 7, 8}
