import tkinter as tk
from tkinter import ttk

# Función que se ejecuta al hacer clic en el botón "Seleccionar"
def mostrar_seleccion():
    seleccion = bebida.get()
    mensaje.config(text="Has seleccionado: {}".format(seleccion))

ventana = tk.Tk()
ventana.title("Selección bebida")
ventana.geometry("300x200")

label = ttk.Label(ventana, text="Selecciona tu bebida preferida:")
label.pack(pady=10)

#variable asociada a los dos Radiobutton
bebida = tk.StringVar()
bebida.set("Café")

# Primer Radiobutton
rb1 = ttk.Radiobutton(ventana, text="Café", value="Café", variable=bebida)
rb1.pack(pady=5)

# Segundo Radiobutton
rb2 = ttk.Radiobutton(ventana, text="  Té  ", value="Té", variable=bebida)
rb2.pack(pady=5)

boton = ttk.Button(ventana, text="Seleccionar", command=mostrar_seleccion)
boton.pack(pady=10)

mensaje = ttk.Label(ventana, text="")
mensaje.pack(pady=10)

ventana.mainloop()
