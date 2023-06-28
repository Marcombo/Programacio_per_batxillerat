x = 10      # variable global

def mi_function():
    y = 5   # variable local
    print("x dentro de la función:", x)
    print("y dentro de la función:", y)
    #no podemos modificar el valor de una global
    #x = 25

mi_function()

print("x fuera de la función:", x)
#no podemos acceder a una variable local
#print ("y fuera de la función:",y)