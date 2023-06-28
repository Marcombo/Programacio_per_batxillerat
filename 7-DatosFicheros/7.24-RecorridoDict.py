dict1 = {"nombre": "Antonio", "edad": 22, "ciudad": "Vigo"}

#obtener las claves
for k in dict1:
    print(k)
#manera alternativa con keys()
for k in dict1.keys():
    print (k)

#obtener los valores
for k in dict1:
    print(dict1[k])
#manera alternativa con values()
for k in dict1.values():
    print (k)
#manera alternativa con acceos a las claves   
for k in dict1.keys():
    print(dict1[k])

#obterner pares (key,valor) como una tupla
for k, v in dict1.items():
  print("Para la clave",k,"tenemos el valor", v)