import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('300x300')
ventana.title("Menú Popup")

# Crear un label
label = ttk.Label(ventana, text="Haz clic derecho para ver las opciones")
label.pack(padx=10, pady=10)

# Crear un popupmenu
opcion_seleccionada = tk.StringVar()

# Definiación de la función en que se haga uso de la opción seleccionada.
popupmenu = tk.Menu(ventana, tearoff=False)
popupmenu.add_command(label="Opción 1", command=lambda: mostrar_mensaje("1"))
popupmenu.add_command(label="Opción 2", command=lambda: mostrar_mensaje("2"))
popupmenu.add_command(label="Opción 3", command=lambda: mostrar_mensaje("3"))

# Función para mostrar un mensaje con la opción seleccionada
def mostrar_mensaje(opcion):
    messagebox.showinfo("Mensaje", f"¡Seleccionaste la opción {opcion}!")

# Mostrar el menú en la posición deonde se hizo clic
def mostrar_popupmenu(event):
    popupmenu.tk_popup(event.x_root, event.y_root)


# Asignación de evento de botón secundario de ratón sobre la etiqueta
label.bind("<Button-3>", mostrar_popupmenu)

ventana.mainloop()
