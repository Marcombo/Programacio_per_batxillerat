import tkinter as tk
from tkinter import ttk

class Formulario:
    def __init__(self):
        # Inicializa la ventana principal del formulario
        self.ventana = tk.Tk()
        self.ventana.title("Formulario")
        # Crea los widgets en la ventana
        self.__crear_widgets()

    def __crear_widgets(self):
        # Crea los widgets del formulario (etiquetas, cajas de texto, botón, etc.)
        self.nombre_label = ttk.Label(self.ventana, text="Nombre:")
        self.nombre_label.grid(column=0, row=0)

        self.nombre_entry = ttk.Entry(self.ventana)
        self.nombre_entry.grid(column=1, row=0)

        self.edad_label = ttk.Label(self.ventana, text="Edad:")
        self.edad_label.grid(column=0, row=1)
        
        self.edad = tk.IntVar(value=18)  
        self.edad_spinbox = ttk.Spinbox(self.ventana, from_=1, to=120 , textvariable=self.edad)
        self.edad_spinbox.grid(column=1, row=1)
  
        self.boton = ttk.Button(self.ventana, text="Mostrar resultados", command=self.mostrar_resultados)
        self.boton.grid(column=0, row=2, columnspan=2)
       
        self.resultado_label = ttk.Label(self.ventana, text="")
        self.resultado_label.grid(column=0, row=3, columnspan=2)

    def mostrar_resultados(self):
        # Muestra los resultados en el label de resultados
        nombre = self.nombre_entry.get()
        edad = self.edad.get()
        resultado = f"Tu nombre es {nombre} y tienes {edad} años."
        self.resultado_label.config(text=resultado)

    def run(self):
        # Inicia el bucle principal de la ventana (mainloop)
        self.ventana.mainloop()

# Crea una instancia del formulario y lo muestra
f = Formulario()
f.run()
