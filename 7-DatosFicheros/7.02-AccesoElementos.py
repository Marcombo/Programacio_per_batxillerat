#Crear una lista con elementos iniciales
lista1 = ["naranja", "plátano", "manzana"]
print (lista1)

#conslutamos el valor de un elemento de la lista
print (lista1[1])

#consultamos un índice fuera de rango
try:
    elemento = lista1[6]
except IndexError:
    print("Error: el índice está fuera del rango válido.")

#modfificamos un elemento de la lsita
lista1[1] = "limón"

#observamos el nuevo contenido de la lsita
print (lista1)

#uso de índices negativos
print (lista1[-1]) #último elemento

print (lista1[-3]) #penúltimo elemento

print (lista1[-len(lista1)]) #primer elemento genérico para toda lista

#print (lista1[-10]) excepción par valor fuera de rango
