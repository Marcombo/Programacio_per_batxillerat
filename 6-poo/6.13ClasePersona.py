# declaración de la clase Persona
class Persona:
    nombre = "Roberto" # propiedad de clase
    edad = 21          # propiedad de clase

# instanciar dos objetos de la clase Persona
p1 = Persona() 
p2 = Persona()
# mostrar los datos del objeto p1
print (p1.nombre, p1.edad)

#cambiamos una propiedad del objeto p2
p2.nombre = "Jorge"

# mostrar los datos del objeto p1
print (p2.nombre, p2.edad)