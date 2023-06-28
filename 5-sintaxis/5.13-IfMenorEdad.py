PrecioEnt = 8
edad = int(input("Dime cuantos años tienes: "))
if edad < 18 or edad > 65:
    PrecioEnt = 8 *0.7 #descuento del 30%
print (f"El precio de la entrada es: {PrecioEnt} euros")