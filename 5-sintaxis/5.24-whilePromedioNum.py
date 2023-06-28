suma = 0 #acumulador
contador = 0
numero = float(input("Introduce un número (0 para terminar): "))

#bucle de petición de números
while numero != 0:
    suma += numero
    contador += 1
    numero = float(input("Introduce un número (0 para terminar): "))

#mostramos resultado solo si hemos metido algún número
if contador != 0:
    promedio = suma / contador
    print("El promedio de los números es:", promedio)
