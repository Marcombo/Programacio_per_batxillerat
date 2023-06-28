lista = ["Eladio", "Manuel", "Jose", "Julio", "Javier", "Eladio"] 
print (lista)

#eliminamos por valor
lista.remove("Eladio") #quita el primero encontrado
print (lista)
lista.remove("Eladio")
print (lista)

#eliminamos el tercer elemento
lista.pop(2)
print (lista)

#otra forma de eleminar por índice
del lista[1]
print (lista)

#eliminar todos los elementos de una lista
lista.clear()
print (lista)

#eliminación completa de la lista
del lista
#imprimirla daría error porque esa variable ya no existe
#print (lista)