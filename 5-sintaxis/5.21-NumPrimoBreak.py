#comprobaremos se el número es primo
numero = int(input("Introduce un número entero: "))

#partimos con la presunción de que es primo
#hasta que no se demuestre lo contrario
es_primo = True

if numero < 2:
    es_primo = False

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False #si divisible=>no es primo
        break

if es_primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")
