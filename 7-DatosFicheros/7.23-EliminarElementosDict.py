dict1 = {"nombre": "Lara", "edad": 31, "oficio": "Médica", "altura": 172, "peso": "68", "pelo": "rubio"}

#borrar una clave no existente provoca una excepción
try:
    del dict1["nacimiento"]
except KeyError as e:
    print ("Clave no definida:",e)

#borramos una clave con síntaxis de corchetes
del dict1["peso"]
print(dict1)

#eliminación con pop
valor_eliminiado= dict1.pop("pelo")
print (valor_eliminiado)
#si indicamos un segundo parámetro pop() nos lo devuelve en caso de no existir la clave
#si no usamos este segundo parámetro y la clave no existe daría una excepción
valor_eliminiado = dict1.pop("talla", "talla_no_existe")
print (valor_eliminiado)

#eliminación con popitem()
valor_eliminiado = dict1.popitem()
print (valor_eliminiado)

#estado final del diccionario
print (dict1)

#con clear vaciamos todo el contenido del diccionario
dict1.clear()
print (dict1)

#con del eliminamos completamente la variable y cualquier posterior referncia daría una excepción
del (dict1)