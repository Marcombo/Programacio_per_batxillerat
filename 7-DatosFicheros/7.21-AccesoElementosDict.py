dict1 = {"nombre": "Juan", "edad": 25, "ciudad": "Valencia"}

#acceos por clave
print(dict1["nombre"])   # Imprime "Juan"
#la siguiente línea daría una excepción de clave
#print(dict1["fecha"]) 

#acceso usando get()
print(dict1.get("edad"))   # Imprime 25
print(dict1.get("telefono"))   # Imprime "None"

#obterner la lista de claves
for clave in dict1.keys():
    print(clave)

#obtener la lista de valores
for valor in dict1.values():
    print(valor)

#obtener la lista de tuplas (clave, valor)
for clave, valor in dict1.items():
    print(clave, valor)