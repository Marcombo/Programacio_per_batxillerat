import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("200x80")

# Widget  label
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()

# Widget cuadro de texto
cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()

# Widget botón
boton_saludar =tk.Button(ventana, text="OK")
boton_saludar.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()
