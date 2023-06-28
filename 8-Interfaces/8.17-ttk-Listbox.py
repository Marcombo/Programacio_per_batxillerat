import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('300x300')
ventana.title('Selecciona tus deportes favoritos')

# Crear la lista de deportes
deportes = ['Baloncesto', 'Fútbol', 'Balonmano', 'Tenis', 'Ciclismo', 'Golf', 'Voleibol',  'Hokey']

# Crear el widget Listbox y agregar los deportes
listbox = tk.Listbox(ventana, selectmode=tk.MULTIPLE, height=5)
for deporte in deportes:
    listbox.insert(tk.END, deporte)

# Función para mostrar los deportes seleccionados
def mostrar_deportes_seleccionados():
    deportes_seleccionados = [listbox.get(index) for index in listbox.curselection()]
    mensaje = 'Los deportes seleccionados son:\n{}'.format(', '.join(deportes_seleccionados))
    etiqueta_resultado.config(text=mensaje)

# Crear el botón y la etiqueta para mostrar el resultado
boton_mostrar = ttk.Button(ventana, text='Mostrar deportes seleccionados', command=mostrar_deportes_seleccionados)
etiqueta_resultado = ttk.Label(ventana, text='')

# Ubicar los widgets en la ventana
listbox.pack(padx=10, pady=10)
boton_mostrar.pack(padx=10, pady=10)
etiqueta_resultado.pack(padx=10, pady=10)

ventana.mainloop()
