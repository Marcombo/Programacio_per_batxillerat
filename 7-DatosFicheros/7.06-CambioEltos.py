lista = ["Eladio", "Manuel", "Jose", "Julio", "Javier", "Eladio"] 
print (lista)

#sustitución de un elemento por otro
listaPrueba = lista.copy()
listaPrueba[1] = "Jorge"
print (listaPrueba)

#sustitución de un elemento por varios
listaPrueba = lista.copy()
listaPrueba[1:2] = ["María","Susana"]
print (listaPrueba)

#sustitución de varios elementos por uno
listaPrueba = lista.copy()
listaPrueba[1:4] = ["Noemí"]
print (listaPrueba)

#sustitución de varios elementos por otros
listaPrueba = lista.copy()
listaPrueba[1:5] = ["Noemí", "Sara", "Pepa"]
print (listaPrueba)

#eliminar un elemento
listaPrueba = lista.copy()
listaPrueba[1:2] = []
print (listaPrueba)

#eliminar varios elementos 
listaPrueba = lista.copy()
listaPrueba[1:4] = []
print (listaPrueba)

#añadir un elemento en una posición 
listaPrueba = lista.copy()
listaPrueba[2:2] = ["Laura"]
print (listaPrueba)

#añadir varios elementos en una posición 
listaPrueba = lista.copy()
listaPrueba[2:2] = ["Marta","Patricia","Rosa"]
print (listaPrueba)
