lista =[2,4,6,8,10,12,14,16,18]

#rango de inclusión
rango = lista[1:4]
print (rango) #salida: [4,6,8]

#desde el inicio de la lista
rango = lista [:5] 
print (rango) #slida: [2,4,6,8,10]

#hasta el final de la lista
rango = lista [5:] 
print (rango) #slida: [2,4,6,8,10]

#contando desde el final
rango = lista [-4:-1] 
print (rango) #slida: [12,14,16]

#combinación índices negativo positivo
rango = lista [-6:8] 
print (rango) #slida: [8,10,12,14,16]

#indice inicial superrior al final
rango = lista [5:2] 
print (rango) #slida: []

#indices fuera de las dimensiones
rango = lista [-60:82] 
print (rango) #slida: [2,4,6,8,10,12,14,16,18]