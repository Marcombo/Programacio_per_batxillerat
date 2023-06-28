import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Crear widget Label
label = tk.Label(ventana, text="Ejemplo de Label")

# Usando el gestor de geometría place
label.place(x=50, y=50, width=150, height=30)

# Mostrar ventana
ventana.mainloop()
