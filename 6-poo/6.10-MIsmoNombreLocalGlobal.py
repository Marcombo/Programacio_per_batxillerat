x = 10 # variable global

def func1():
    x = 5 # variable local
    print("El valor de x dentro de la función 1 es:", x)

def func2(x):
    x = x+100 #un parámetro actúa de variable local
    print("El valor de x dentro de la función 2 es:", x)

func1()
func2(x)
print("El valor de x fuera de la función es:", x)
