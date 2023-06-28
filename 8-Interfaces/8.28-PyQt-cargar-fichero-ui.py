import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

# Clase de la ventana principal
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar el archivo de interfaz de usuario
        uic.loadUi('holaPyQtDesigner.ui', self)

# Entrada al programa
if __name__ == '__main__':
    app = QApplication([])
    ventana = MyMainWindow()
    # Mostrar la ventana principal
    ventana.show()
    # Iniciar y salir del programa cuando se cierra la ventana principal
    sys.exit(app.exec())
