
print("¿Cómo te llamas llamas?") #input sin parámetros
nombre = input() 
#input con texto asociado
apellido = input (nombre +", ¿Cuál es tu apellido? ")
print("Encantado de conocerte " + nombre + " " + apellido)
edad = input ("¿Cuantos años tienes?")
edadFutura = int(edad) + 8 #conversión de edad a entero
print ("{} {} dentro de 8 años tendrás {} años".format(nombre, apellido, edadFutura))