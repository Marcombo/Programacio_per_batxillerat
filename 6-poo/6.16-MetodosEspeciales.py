# declaración de la clase Persona
class Persona:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre # propiedad de instancia
        self.edad = edad # propiedad de instancia

    #devuelve un string al imprimir o usar Persona como cadena
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    #destructor
    def __del__(self):
        print (f"{self.nombre} ha muerto :(")

#este objeto persona solo existe dentro de su bloque de código
p1 = Persona("Javier", 24)
p1 = None #eliminación manual del objeto
    
# instanciar dos objetos de la clase Persona
p2 = Persona("Ramón", 17) 

# mostrar los datos del objeto p1
print (p2)

