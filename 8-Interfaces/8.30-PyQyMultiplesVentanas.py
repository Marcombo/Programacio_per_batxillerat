from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt6.uic import loadUi

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar interfaz de login desde el archivo .ui
        loadUi('login.ui', self)

    def abrirPrincipal(self):
        self.main_window = QMainWindow()    
        # Cargar interfaz de formulario desde el archivo .ui
        loadUi('formPelicula.ui', self.main_window)
        self.main_window.show()
        self.close()
  
if __name__ == '__main__':
    # Crear la aplicación y la ventana de inicio de sesión
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    # Ejecutar la aplicación
    app.exec()