from ferreteria import Ferreteria, ElementoFerreteria
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QDialogButtonBox, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self, ferreteria):
        super().__init__()

        self.ferreteria = ferreteria

        self.setWindowTitle('Ferretería')
        self.setGeometry(100, 100, 680, 600)

        self.crear_interfaz()

    def crear_interfaz(self):
        widget = QWidget()
        layout_principal = QVBoxLayout()

        # Botón para agregar un nuevo elemento
        boton_agregar = QPushButton('Añadir elemento')
        boton_agregar.setMinimumHeight(30)
        boton_agregar.setStyleSheet("background-color: green; color: white; \
                                border-radius: 4px; \
                                padding: 1px; \
                                margin: 3 ; auto")
        boton_agregar.clicked.connect(self.agregar_elemento)
        layout_principal.addWidget(boton_agregar)

        # Crear tabla de elementos
        tabla = QTableWidget()
        tabla.setColumnCount(6)
        tabla.setHorizontalHeaderLabels(['Código', 'Nombre', 'Cantidad', 'Precio', '', ''])
        elementos = self.ferreteria.listar_elementos()
        tabla.setRowCount(len(elementos))
        for i, elemento in enumerate(elementos):
            codigo = QTableWidgetItem(elemento.codigo)
            nombre = QTableWidgetItem(elemento.nombre)
            cantidad = QTableWidgetItem(str(elemento.cantidad))
            precio = QTableWidgetItem(str(elemento.precio))
            tabla.setItem(i, 0, codigo)
            tabla.setItem(i, 1, nombre)
            tabla.setItem(i, 2, cantidad)
            tabla.setItem(i, 3, precio)

            # Establecer los elementos como no editables
            for j in range(4):
                item = tabla.item(i, j)
                #hacer las celdas no editables
                item.setFlags(item.flags() ^ ~ Qt.ItemFlag(2)) # PyQ t Qt.ItemIsEditable)

            # Agregar botones de modificar y eliminar
            boton_modificar = QPushButton('Modificar')
            boton_modificar.setProperty('codigo', elemento.codigo)
            boton_modificar.clicked.connect(self.modificar_elemento)
            boton_modificar.setStyleSheet("background-color: blue; color: white; \
                                border-radius: 4px; \
                                padding: 1px; \
                                margin: 3 ")
            tabla.setCellWidget(i, 4, boton_modificar)

            boton_eliminar = QPushButton('Eliminar')
            boton_eliminar.setProperty('codigo', elemento.codigo)
            boton_eliminar.clicked.connect(self.eliminar_elemento)
            boton_eliminar.setStyleSheet("background-color: red; color: white; \
                                border-radius: 4px; \
                                padding: 1px; \
                                margin: 3 ")
            tabla.setCellWidget(i, 5, boton_eliminar)

        layout_principal.addWidget(tabla)
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)

    def modificar_elemento(self):
        boton = self.sender()
        codigo = boton.property('codigo')
        elemento = self.ferreteria.buscar_elemento(codigo)

        if elemento:
            # Crear ventana de modificar elemento
            self.ventana_modificar = VentanaModificarAgregarElemento(self.ferreteria, elemento)
            self.ventana_modificar.isModal()
            self.ventana_modificar.exec()

            # Actualizar tabla de elementos
            self.crear_interfaz()


    def agregar_elemento(self):

        # Crear ventana de modificar elemento
        self.ventana_agregar = VentanaModificarAgregarElemento(self.ferreteria)
        self.ventana_agregar.isModal()
        self.ventana_agregar.exec()

        # Actualizar tabla de elementos
        self.crear_interfaz()

    def eliminar_elemento(self):
        boton = self.sender()
        codigo = boton.property('codigo')

        # Eliminar elemento de la ferretería
        self.ferreteria.eliminar_elemento(codigo)

        # Actualizar tabla de elementos
        self.crear_interfaz()

class VentanaModificarAgregarElemento(QDialog):
    def __init__(self, ferreteria, elemento= None):
        super().__init__()

        self.ferreteria = ferreteria
        if elemento:
            self.operacion="modificar"
        else:
            self.operacion="agreagar"
        self.elemento = elemento
        if (self.operacion=="modificar"):
            self.setWindowTitle('Modificar elemento')
            self.elemento = elemento
        else:
            self.setWindowTitle('Añadir elemento')
            self.elemento = ElementoFerreteria(str(self.ferreteria.siguiente_codigo()))

        self.crear_interfaz()
        self.campo_nombre.setFocus() # Establecer el foco en el campo de nombre

    def crear_interfaz(self):
        layout = QVBoxLayout()

        # Campo de código (no editable)
        codigo_layout = QFormLayout()
        label_codigo = QLineEdit(self.elemento.codigo)
        label_codigo.setReadOnly(True)
        label_codigo.setStyleSheet("background-color: lightgrey;")
        codigo_layout.addRow('Código:', label_codigo)
        layout.addLayout(codigo_layout)

        # Campo de nombre
        nombre_layout = QFormLayout()
        self.campo_nombre = QLineEdit(self.elemento.nombre)
        nombre_layout.addRow('Nombre:', self.campo_nombre)
        layout.addLayout(nombre_layout)

        # Campo de cantidad
        cantidad_layout = QFormLayout()
        self.campo_cantidad = QLineEdit(str(self.elemento.cantidad))
        self.campo_cantidad.setValidator(QIntValidator())
        cantidad_layout.addRow('Cantidad:', self.campo_cantidad)
        layout.addLayout(cantidad_layout)

        # Campo de precio
        precio_layout = QFormLayout()
        self.campo_precio = QLineEdit(str(self.elemento.precio))
        precio_layout.addRow('Precio:', self.campo_precio)
        layout.addLayout(precio_layout)

        # Botón de guardar cambios
        boton_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        boton_box.accepted.connect(self.guardar_cambios)
        boton_box.rejected.connect(self.close)
        layout.addWidget(boton_box)

        self.setLayout(layout)

    def guardar_cambios(self):
        codigo = self.elemento.codigo
        nombre = self.campo_nombre.text()
        cantidad = int(self.campo_cantidad.text())
        precio = float(self.campo_precio.text())

        # Modificar elemento en la ferretería
        elemento_editado = ElementoFerreteria(codigo, nombre, cantidad, precio)
        if (self.operacion=="modificar"):
            self.ferreteria.modificar_elemento(elemento_editado)
        else:
            self.ferreteria.guardar_elemento(elemento_editado)

        # Cerrar ventana
        self.close()

if __name__ == '__main__':
    f =Ferreteria("almacen_ferreteria.csv")
    # Crear la aplicación y la ventana de inicio de sesión
    app = QApplication([])
    ventana = VentanaPrincipal(f)
    ventana.show()
    # Ejecutar la aplicación
    sys.exit(app.exec())