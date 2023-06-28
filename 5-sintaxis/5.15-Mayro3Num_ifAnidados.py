# Pedimos al usuario los tres números
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Tercer número: "))

# Lo encontramos con if anidados
if numero1 > numero2:
    if numero1 > numero3:
        mayor = numero1
    else:
        mayor = numero3
else:
    if numero2 > numero3:
        mayor = numero2
    else:
        mayor = numero3

# Imprimimos el número mayor
print("El número mayor es: ", mayor)
