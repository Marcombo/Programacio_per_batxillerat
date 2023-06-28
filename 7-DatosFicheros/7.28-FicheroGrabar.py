#abrimos un archivo para añadir datos al final
#si el fichero no existe lo crea
f = open("datos1.txt", "a")
f.write("Añado esta nueva línea\n")
f.close()

#uso de un objeto dentro de un bloque with
with open("datos1.txt", "r") as f:
    print (f.read())

#abrimos un archivo para escribir
#si ya existe borra el contenido y sobrescribe
f = open("datos2.txt", "w")
f.write("Línea de pruebas\n")
f.close()

with open("datos2.txt", "r") as f:
    print (f.read())

#abrimos un archivo para escribir
#si ya existe dará una excepción
try:
    f = open("datos3.txt", "x")
    f.close()
except FileExistsError:
    print("El fichero 'datos3.txt' ya existe!")    