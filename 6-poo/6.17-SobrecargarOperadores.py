class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #sobrecarga de + concatenando nombres y sumando edades
    def __add__(self, otraPersona):
        nombre = self.nombre + " " + otraPersona.nombre
        edad = self.edad + otraPersona.edad
        return Persona(nombre, edad)
    
     #devuelve un string al imprimir o usar Persona como cadena
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
    

# Ejemplo de uso
persona1 = Persona("Jose", 18)
persona2 = Persona("Antonio", 21)
persona3 = persona1 + persona2
print(persona3)  # Jose Antino 39
