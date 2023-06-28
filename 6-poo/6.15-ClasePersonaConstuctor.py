# declaración de la clase Persona
class Persona:

    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre # propiedad de instancia
        self.edad = edad # propiedad de instancia

# instanciar dos objetos de la clase Persona
p1 = Persona("Ramón", 17) 

# mostrar los datos del objeto p1
print (p1.nombre, p1.edad)
