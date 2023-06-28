class MaquinaExpendedora:
    def __init__(self):
        self.tipo_bebida = "café"
        self.precio = 1.50
        self.cantidad = 10
        self.ventas_totales = 0
        
    def insertar_dinero(self, monto):
        """Insertar dinero en la máquina"""
        self.monto_insertado = monto
        
    def seleccionar_bebida(self):
        """Seleccionar una bebida"""
        if self.cantidad == 0:
            return "Bebida agotada"
        if self.monto_insertado < self.precio:
            return "Dinero insuficiente"
        self.monto_insertado -= self.precio
        self.cantidad -= 1
        self.ventas_totales += self.precio
        return "¡Disfrute su bebida!"
    
    def obtener_ventas_totales(self):
        """Obtener las ventas totales de la máquina"""
        return self.ventas_totales
    
    def recargar(self):
        """Recargar la máquina con cantidad de bebida predeterminada"""
        self.cantidad = 10

def menu_usuario(maquina):
    while True:
        print("\n--- Máquina expendedora de café ---")
        print("1. Insertar dinero")
        print("2. Seleccionar bebida")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a insertar: "))
            maquina.insertar_dinero(monto)
            print(f"Se han insertado ${monto:.2f} en la máquina.")

        elif opcion == "2":
            resultado = maquina.seleccionar_bebida()
            print(resultado)

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


def menu_administrador(maquina):
    while True:
        print("\n--- Panel de administración ---")
        print("1. Obtener ventas totales")
        print("2. Recargar la máquina")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ventas = maquina.obtener_ventas_totales()
            print(f"Las ventas totales de la máquina son: ${ventas:.2f}")

        elif opcion == "2":
            maquina.recargar()
            print("La máquina ha sido recargada con éxito.")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


def menu_principal():
    maquina = MaquinaExpendedora()

    while True:
        print("\n--- Máquina expendedora de café ---")
        print("1. Usuario")
        print("2. Administrador")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuario(maquina)

        elif opcion == "2":
            menu_administrador(maquina)

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()