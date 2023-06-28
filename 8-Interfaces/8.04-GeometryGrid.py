import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Crear widgets Label
label = tk.Label(ventana, text="Etiqueta 1")
labe2 = tk.Label(ventana, text="Etiqueta 2")

# Usando el gestor de geometría grid
label.grid(row=0, column=0, padx=10, pady=10)
labe2.grid(row=1, column=2, padx=10, pady=10)

# Mostrar ventana
ventana.mainloop()
