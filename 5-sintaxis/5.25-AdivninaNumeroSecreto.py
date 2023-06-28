import random #para poder usar randint()

numero = random.randint(1, 100) #numero aleatorio
adivinado = False
intentos = 0

print("Adivina mi número (entre 1 y 100).")

#not Adivinado es equivalente a "adivinado==True"
while not adivinado:
    numJugador = int(input("Dime un número: "))
    intentos += 1
    if numJugador == numero:
        print("¡Adivinado en", intentos, "intentos!")
        adivinado = True
    elif numJugador < numero:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
