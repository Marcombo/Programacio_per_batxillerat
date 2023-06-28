x = 10      # variable global

def mi_funcion():
    global x #declaracion de acceso a vble global
    x = 50

print("valor inicial de x", x)
mi_funcion()
print("valor finall de x", x)
