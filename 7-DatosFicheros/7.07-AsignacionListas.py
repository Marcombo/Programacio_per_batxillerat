X = 3
Y = X 
X = 5 
print (Y) #valor 3

txt1 = "hola"
txt2 = txt1
txt1 = "adiros"
print (txt2) #valor "hola"

lista1 = ["A","B","C","D"]
print (lista1)
#lo siguiente no es una copia de una lista en otra
#es la MISMA LISTA que tiene dos nombres o referencias
lista2 = lista1 

lista1.pop() #eliminamos algo en lista1
print (lista2) #su efecto se refleja en lista2

lista2.append("E") #añadimos algo en lista2
print (lista1) #su efecto se refleja en lista1