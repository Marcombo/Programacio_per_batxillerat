import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('300x300')
ventana.title("Menús")

# Crear una barra de menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Crear un menú Archivo
archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar", state="disabled")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

# Crear un menú Editar
editar_menu = tk.Menu(menu_bar, tearoff=0)
editar_menu.add_command(label="Cortar")
editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Pegar")

# Añadir el menú Archivo y Editar a la barra de menú
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
menu_bar.add_cascade(label="Editar", menu=editar_menu)

ventana.mainloop()
