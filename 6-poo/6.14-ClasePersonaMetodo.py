# declaración de la clase Persona
class Persona:
    nombre = "Roberto" # propiedad de clase
    edad = 21          # propiedad de clase
    
    #metodo para incrementar un año
    def incrementa_edad(self):
        self.edad += 1

# instanciar dos objetos de la clase Persona
p1 = Persona() 

# mostrar los datos del objeto p1
print (p1.nombre, p1.edad)

# invocamos un método
p1.incrementa_edad()

# mostrar los datos del objeto p1
print (p1.nombre, p1.edad)