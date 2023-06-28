# Ejemplo de uso de count()
cadena = "Hola, ¿cómo estás hoy?"
caracter = "o"
print(cadena.count(caracter)) # salida: 4

# Ejemplo de uso de find()
subcadena = "estás"
print(cadena.find(subcadena)) # salida: 11

# Ejemplo de uso de isalpha()
cadena1 = "Hola"
print(cadena1.isalpha()) # salida: True
print(cadena.isalpha()) # salida: False

# Ejemplo de uso de isnumeric()
cadena1 = "1234"
print(cadena1.isnumeric()) # salida: True
print(cadena.isnumeric()) # salida: False

# Ejemplo de uso de isalnum()
cadena1 = "Hola123"
cadena = "Hola, ¿cómo estás hoy?"
print(cadena1.isalnum()) # salida: True
print(cadena.isalnum()) # salida: False
