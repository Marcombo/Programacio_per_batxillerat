#Crear una tupla con elementos iniciales
tupla1 = ("naranja", "plátano", "manzana")
print (tupla1)

#conslutamos el valor de un elemento de la tupla
print (tupla1[1])

#consultamos un índice fuera de rango
try:
    elemento = tupla1[6]
except IndexError:
    print("Error: el índice está fuera del rango válido.")

#eXCEPCIÓN: NO SE PERMITE MODIFICAR ELEMENTOS de una TUPLA
try:
    tupla1[1] = "limón"
except TypeError as e:
    print(e)

#uso de rangos para obtener una sub-tupla
tupla2 = tupla1[0:2]
print (tupla2)
