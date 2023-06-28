import tkinter as tk
import tkinter as ttk

# Crear una ventana principal
ventana = tk.Tk()
ventana.geometry("200x100")

# Crear una etiqueta y configurar su texto inicial
label = ttk.Label(ventana, text="Soy una etiqueta")

# Definir una función para cambiar el texto de la etiqueta
def cambiarTextoEtiqueta(event):
    label.configure(text="¡Bienvenido!")

# Definir una función para restaurar el texto de la etiqueta
def restaurarTextoEtiqueta(event):
    label.configure(text="Soy una etiqueta")

# Asociar la función de cambio de texto con el evento <Enter>
label.bind("<Enter>", cambiarTextoEtiqueta)

# Asociar la función de restauración de texto con el evento <Leave>
label.bind("<Leave>", restaurarTextoEtiqueta)

# Empaquetar la etiqueta en la ventana principal
label.pack()

# Ejecutar el bucle principal
ventana.mainloop()
