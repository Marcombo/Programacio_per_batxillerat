set1 = {"patata", "berenjena", "zanahoria"}

#recorrido simple en un bucle for
for elto in set1:
    print(elto)

#comprobación de que un elemento está en el set
if "berenjena" in set1:
    print ("Hemos encontrado una berenjena en el conjunto")

#acceso a los elementos a medida que los vamos eliminando
while len(set1) > 0:
    elto = set1.pop()
    print(elto)
print ("El valor actual del set es vacío: ", set1)
