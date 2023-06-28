import tkinter as tk
from tkinter import ttk

# Función para mostrar el mensaje si está lloviendo
def comprobar_lluvia():
    if llueve.get():
        label.config(text="Hay que llevar paraguas")
    else:
        label.config(text="No es necesario llevar paraguas")

# Crear ventana
ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("Comprobar tiempo")

# Crear Checkbutton para verificar si está lloviendo
llueve = tk.BooleanVar()
checkbutton = ttk.Checkbutton(ventana, text="Está lloviendo", variable=llueve)
llueve.set(True) # Se puede prestablecer un valor inicial
checkbutton.pack()

# Crear botón para comprobar 
boton = ttk.Button(ventana, text="Comprobar", command=comprobar_lluvia)
boton.pack()

# Crear label para mostrar el mensaje
label = ttk.Label(ventana, text="")
label.pack()

# Iniciar loop de la aplicación
ventana.mainloop()
