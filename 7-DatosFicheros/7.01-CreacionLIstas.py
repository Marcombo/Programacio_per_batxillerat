#Crear una lista con elementos iniciales
lista1 = ["naranja", "plátano", "manzana"]
print (lista1)

#Crear una lista vacía y agregar elementos uno por uno
lista2 = []
lista2.append("Coche")
lista2.append("Moto")
lista2.append("Barco")
print (lista2)

#Crear una lista usando la función list() 
lista3 = list ("abcdefghi")
lista4 = list(range(1, 11))
print (lista3)
print (lista4)

#Crear una lista a partir de una cadena separada por comas usando el método split()
mi_cadena = "Manuel, María, Noemí"
lista5 = mi_cadena.split(", ")
print (lista5)

#Ejemplo de lista heterogenea (elementos de distinto tipo)
lista_h = ["hola", 7, True, 8.75]
print (lista_h)