from ferreteria import Ferreteria, ElementoFerreteria

class CRUDferreteria:
    def __init__(self, archivo_csv):
        self.ferreteria = Ferreteria(archivo_csv)
        
    def mostrar_menu(self):
        while True:
            print("====== Menú Ferretería ======")
            print("1. Alta de elemento")
            print("2. Baja de elemento")
            print("3. Consulta de elemento")
            print("4. Modificación de elemento")
            print("5. Listar todos los elementos")
            print("6. Salir")
            opcion = input("Introduce la opción deseada: ")
            if opcion == "1":
                self.alta_elemento()
            elif opcion == "2":
                self.baja_elemento()
            elif opcion == "3":
                self.consulta_elemento()
            elif opcion == "4":
                self.modificacion_elemento()
            elif opcion == "5":
                self.listar_todos_los_elementos()
            elif opcion == "6":
                break
            else:
                print("Opción inválida. Introduce un número del 1 al 6.")    
        
    def alta_elemento(self):
        codigo = input("Introduce el código del elemento: ")
        nombre = input("Introduce el nombre del elemento: ")
        cantidad = int(input("Introduce la cantidad del elemento: "))
        precio = float(input("Introduce el precio del elemento: "))
        elemento = ElementoFerreteria(codigo, nombre, cantidad, precio)
        self.ferreteria.guardar_elemento(elemento)
        print("Elemento agregado con éxito.")
        
    def baja_elemento(self):
        codigo = input("Introduce el código del elemento a eliminar: ")
        self.ferreteria.eliminar_elemento(codigo)
        print("Elemento eliminado con éxito.")
        
    def consulta_elemento(self):
        codigo = input("Introduce el código del elemento a consultar: ")
        elemento = self.ferreteria.buscar_elemento(codigo)
        if elemento:
            print("Código: ", elemento.codigo)
            print("Nombre: ", elemento.nombre)
            print("Cantidad: ", elemento.cantidad)
            print("Precio: ", elemento.precio)
        else:
            print("Elemento no encontrado.")
            
    def modificacion_elemento(self):
        codigo = input("Introduce el código del elemento a modificar: ")
        elemento = self.ferreteria.buscar_elemento(codigo)
        if elemento:
            print("Introduce los nuevos datos del elemento (dejar en blanco para mantener el valor actual):")
            nombre = input("Nombre (" + elemento.nombre + "): ")
            cantidad = input("Cantidad (" + str(elemento.cantidad) + "): ")
            precio = input("Precio (" + str(elemento.precio) + "): ")
            if nombre == "":
                nombre = elemento.nombre
            if cantidad == "":
                cantidad = elemento.cantidad
            else:
                cantidad = int(cantidad)
            if precio == "":
                precio = elemento.precio
            else:
                precio = float(precio)
            elemento_modificado = ElementoFerreteria(codigo, nombre, cantidad, precio)
            self.ferreteria.modificar_elemento(elemento_modificado)
            print("Elemento modificado con éxito.")
        else:
            print("Elemento no encontrado.")

    def listar_todos_los_elementos(self):
        elementos = self.ferreteria.listar_elementos()
        if len(elementos) > 0:
            print("Código   | Nombre                          | Cantidad | Precio")
            print("-------- | ------------------------------- | -------- | ------")
            for elemento in elementos:
                print("{:8s} | {:30s}  | {:8d} |  {:,.2f}€".format(elemento.codigo, elemento.nombre, elemento.cantidad, elemento.precio))
        else:
            print("No hay elementos en la ferretería.")

if __name__ == '__main__':
    crud = CRUDferreteria("almacen_ferreteria.csv")
    crud.mostrar_menu()