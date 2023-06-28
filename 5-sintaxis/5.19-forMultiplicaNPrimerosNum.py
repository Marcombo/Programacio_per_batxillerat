n = int(input("Introduce un número positivo: "))
producto = 1 #ojo iniciamos a uno, no a cero

#usamos n+1, para que n también entre en el cálculo
for i in range(1, n+1):
    producto *= i

#mostrar resultado
print("El producto de los", n, "primeros números es:", producto)
