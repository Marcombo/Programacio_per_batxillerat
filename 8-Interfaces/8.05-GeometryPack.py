import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Crear widgets Label
label = tk.Label(ventana, text="Etiqueta 1")
labe2 = tk.Label(ventana, text="Etiqueta 2")

# Usando el gestor de geometría pack
label.pack(side="kj" "left", padx=10, pady=10)
labe2.pack(side="bottom", padx=10, pady=10)

# Mostrar ventana
ventana.mainloop()
