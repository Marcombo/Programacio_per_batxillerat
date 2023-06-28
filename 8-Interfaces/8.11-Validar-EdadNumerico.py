import tkinter as tk
from tkinter import ttk

# Función para mostrar el nombre y la edad ingresados
def mostrar_datos():
    ventana.title (f"Nombre: {nombre.get()}, Edad: {edad.get()}")

# Validamos que la edad sea mayor que 18
def validar_edad_mayor(event):
    if not (int(entry_edad.get()) >= 18):
        entry_edad.delete(0,tk.END)

# Descartamos cualquier valor no numérrico
def validar_numero(event):
    # Obtiene el carácter que se pulsó
    c = event.char
    # Verifica si el carácter es un número o el botón borrar
    if not c.isdigit() and c != '\b':
        # Si el carácter no es un número ni el botón borrar, ignora el evento
        event.widget.bell() #sonido beep
        return 'break'

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
# Validaciones
entry_edad.bind("<FocusOut>", validar_edad_mayor)
entry_edad.bind("<Key>", validar_numero)

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