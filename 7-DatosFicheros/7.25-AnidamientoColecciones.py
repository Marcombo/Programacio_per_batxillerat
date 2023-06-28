#matriz representada como una lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Recorremos cada fila de la matriz
for fila in matriz:
    # Recorremos cada elemento de la fila
    for elemento in fila:
        print(elemento)

# Mientras haya filas en la matriz
fila = columna = 0
while fila < len(matriz):
    # Mientras haya elementos en la fila actual
    while columna < len(matriz[fila]):
        print(f"[{fila+1},{columna+1}]:{matriz[fila][columna]}")
        # Incrementamos la columna
        columna += 1
    # Reiniciamos la columna e incrementamos la fila
    columna = 0
    fila += 1

#tupla de coordenadas
coordenadas = ((0, 0), (1, 2), (3, 4), (5, 6))
for x, y in coordenadas:
    print (f"abcisas:{x}, ordenadas:{y}")

#usuarios usando un diccionario de diccionarios
usuarios = {
    'juan': {'nombre': 'Juan', 'edad': 25, 'email': 'juan@marcombo.com'},
    'maria': {'nombre': 'María', 'edad': 30, 'email': 'maria@marcombo.com'},
    'pedro': {'nombre': 'Pedro', 'edad': 28, 'email': 'pedro@emarcombo.com'},
}

# Recorremos cada usuario en el diccionario
for usuario in usuarios.values():
    print(f"Nombre: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']}")
    print(f"Email: {usuario['email']}")

#estructura similar a la anterior pero con lista de diccioanrios
# Creamos una lista de diccionarios
listaUsuarios = [
    {'nombre': 'Asun', 'edad': 19, 'email': 'asun@ejemplo.com'},
    {'nombre': 'Ana', 'edad': 20, 'email': 'ana@ejemplo.com'},
    {'nombre': 'Yolanda', 'edad': 22, 'email': 'yolanda@ejemplo.com'},
]

#reoorremos acad elemnto diccionario en la lista
for diccionario in listaUsuarios:
    # Iteramos sobre las claves-valor del diccionario
    for clave, valor in diccionario.items():
        # Imprimimos cada clave-valor del diccionario
        print(f"{clave}: {valor}")