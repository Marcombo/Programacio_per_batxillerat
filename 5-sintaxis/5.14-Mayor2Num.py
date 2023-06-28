# Pedimos los números al usuario
numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime otro número: "))

# Comparamos para obtener el mayor
if numero1 > numero2:
    mayor = numero1
else:
    mayor = numero2

# Mostramos el mayor
print("El número mayor es:", mayor)