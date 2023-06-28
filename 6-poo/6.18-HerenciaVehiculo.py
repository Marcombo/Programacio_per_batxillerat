# clase Padre
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

# clase hija        
class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio, num_puertas):
        super().__init__(marca, modelo, precio) 
        self.num_puertas = num_puertas
        
    def __str__(self):
        return (f"Coche\nMarca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio}€\nNúmero de puertas: {self.num_puertas}\n")

# clase hija             
class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, cilindrada):
        #sintasis alternativa a usar el constructor del padre
        #self.marca = marca
        #self.modelo = modelo
        #self.precio = precio
        super().__init__(marca, modelo, precio)
        self.cilindrada = cilindrada
    
    def __str__(self):
        return (f"Moto\nMarca: {self.marca}\nModelo: {self.modelo}\nPrecio: ${self.precio}€\nCilindrada: {self.cilindrada}\n")

coche1 = Coche("Seat", "León", 30000, 4)
moto1 = Moto("Honda", "CBR", 15000, 1000)

print (coche1)
print (moto1)
