import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Crear widget Label
label = tk.Label(ventana, text="Ejemplo de Label")

# Usando el gestor de geometría pack
label.pack(side="left", padx=10, pady=10)

# Mostrar ventana
ventana.mainloop()
