#apertura de un fichero de texto
archivo = open('datos.txt', mode="r", encoding="utf-8")

#obtener todo su contenido
contenido = archivo.read()
print (contenido)

#cierre del fichero
archivo.close()