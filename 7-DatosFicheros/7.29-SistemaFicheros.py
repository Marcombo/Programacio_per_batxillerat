import os

#obtener el directorio de trabajo
dir_actual = os.getcwd()
print(f"Tu directorio de trabajo es: {dir_actual}")

#listado de ficheros
files = os.listdir()
print("Listado de ficheros:\n",files)

#rear una carpeta
os.mkdir('carpeta_nueva')

#creamos un fichero para las siguientes operaciones
open("archivo.txt","x")

#cambiar el nombre de un archivo
os.rename('archivo.txt', 'nuevo_nombre.txt')

#elimina un archivo
os.remove('nuevo_nombre.txt')

