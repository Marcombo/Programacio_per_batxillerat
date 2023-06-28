#sintaxis más usual de creación de un diccionario
dict1 = {"nombre": "Yolanda", "edad": 25, "ciudad": "Ourense"}
print (dict1)

#creación de un diccionario a través de la función dict()
dict2 = dict(nombre="Margarita", edad=26, ciudad="Bilbao")
print (dict2)

#cración en base a una lista de tuplas
tuplas = [("nombre", "Marta"), ("edad", 27), ("ciudad", "León")]
dict3 = dict(tuplas)
print (dict3)

#cración de diccionario vacío y adición de elemntos
dict4 = {}
dict4["nombre"] = "Patricia"
dict4["edad"] = 29
dict4["ciudad"] = "Ferrol"
print (dict4)

#creación a partir de dos listas de igual longitud
claves = ["nombre", "edad", "ciudad"]
valores = ["Rosa", 31, "Ávila"]
dict5 = dict(zip(claves, valores))
print (dict5)

#comprobación de que un diccionario no permite claves repetidas
#en este caso nos quedaremos con la último valor 
dict5 = {"clave1": 5, "clave1": 555}
print (dict5)