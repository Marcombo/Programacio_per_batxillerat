import tkinter as tk
from tkinter import ttk

# Función para mostrar el nombre y la edad ingresados
def mostrar_datos():
    ventana.title (f"Nombre: {nombre.get()}, Edad: {edad.get()}")
    nombre.set("") #vaciamos su contenido
    edad.set("") #vaciamos su contenido

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Campos entrada datos")

# Crear objetos StringVar para almacenar el nombre y la edad introducidos
nombre = tk.StringVar()
edad = tk.StringVar()

# Crear widgets de entrada de texto para nombre y la edad
entry_nombre = ttk.Entry(ventana, textvariable=nombre)
entry_edad = ttk.Entry(ventana, textvariable=edad)

# Ubicar los widgets de entrada en la ventana
entry_nombre.pack()
entry_edad.pack()

#establecer el foco al inicair en el primer campo
entry_nombre.focus()

# Crear un botón para mostrar los datos introducidos
boton_mostrar = ttk.Button(ventana, text="Mostrar", command=mostrar_datos)
boton_mostrar.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()