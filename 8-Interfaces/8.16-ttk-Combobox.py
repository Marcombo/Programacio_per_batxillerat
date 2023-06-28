import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()
ventana.geometry('300x200')
ventana.title('Combobox')

# Crear la etiqueta y el ComboBox
label = ttk.Label(ventana, text="Tipo de inmueble:")
label.pack(pady=10)

combo = ttk.Combobox(ventana)
combo['values'] = ('Apartamento', 'Piso', 'Chalet')
combo.pack(pady=10)

# Función para obtener el valor seleccionado
def get_selected_value():
    resultado.config(text=combo.get())

# Crear el botón para obtener el valor seleccionado
button = ttk.Button(ventana, text="Obtener valor seleccionado", command=get_selected_value)
button.pack(pady=10)

# Crear el label para mostrar el resultado
resultado = ttk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
