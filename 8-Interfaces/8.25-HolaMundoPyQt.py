import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# Creamos una clase que hereda de QWidget (ventana básico en PyQt)
class MainWindow(QWidget):
    def __init__(self):
        # Constructor que inicializa la ventana
        super().__init__()
        # Título y dimensiones
        self.setWindowTitle('Hola Mundo en PyQt')
        self.setGeometry(100, 100, 300, 200)
        # Objeto QLabel (etiqueta) que muestra el texto "Hola Mundo!"
        self.label = QLabel('Hola Mundo!', self)
        self.label.move(100, 80)
        # Hacemos visible la ventana
        self.show()

if __name__ == '__main__':
    # QApplication, que maneja la línea de comandos y otros aspectos básicos de la aplicación
    app = QApplication(sys.argv)
    # Instancia de nuestra clase MainWindow
    ventana = MainWindow()
    # Ejecutamos la aplicación
    sys.exit(app.exec())

