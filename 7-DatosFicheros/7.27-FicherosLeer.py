#lectura de un número determinado de caracteres
f = open('datos.txt', encoding="utf-8")
texto = f.read(3)
print(texto)
f.close()

#lectura de dos líneas
f = open('datos.txt', encoding="utf-8")
linea1 = f.readline()
linea2 = f.readline()
print ("longitud de línea 1:", len(linea1))
print(linea1)
# con strip() eliminamos caráctess especiales como saltos de linea
print (linea1.strip()) 
print ("longitud sin saltos de línae:", len(linea1.strip()))
print (linea2.strip())
f.close()

#recorrer todas las líneas
f = open('datos.txt', encoding="utf-8")
for x in f:
  print (x.strip())
f.close()

#recorrer con un while
f = open('datos.txt', encoding="utf-8")
linea = f.readline()
while linea:
    # Procesar la línea
    print(linea.strip())  # Imprime la línea sin el salto de línea
    # Leer la siguiente línea
    linea = f.readline()
f.close()


#obtener una lista de lineas
f = open('datos.txt', encoding="utf-8")
lineas = f.readlines()
print (lineas) #podemos ver los saltos de línea como "\n"
print (lineas[1])
f.close()