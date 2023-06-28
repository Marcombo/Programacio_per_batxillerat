tupla = ("naranja", "plátano", "manzana")

#esto no es tuna tupla, es un 'string'
falsa_tupla =("limón") 
print (type(falsa_tupla))

#una tupla de un solo elemento lleva una coma final
tupla2  = ("mandarina",)

#operación de concatenación de tuplas
tupla += tupla2
print(tupla)

#añadir un elemento a una tupla usando lista
auxiliar = list(tupla)
auxiliar.append("fresa")
tupla = tuple(auxiliar)
print (tupla)

#eliminar un elemento a una tupla usando lista
auxiliar = list(tupla)
auxiliar.remove("plátano")
tupla = tuple(auxiliar)
print (tupla)
