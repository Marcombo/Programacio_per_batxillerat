import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Crear widgets Label
label = tk.Label(ventana, text="Etiqueta 1")
labe2 = tk.Label(ventana, text="Etiqueta 2")

# Usando el gestor de geometría place
label.place(x=50, y=50, width=150, height=30)
labe2.place(x=100, y=100, width=150, height=30)

# Mostrar ventana
ventana.mainloop()
