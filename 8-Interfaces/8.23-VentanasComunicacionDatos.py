import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Crear una variable StringVar para almacenar el nombre
nombre = tk.StringVar()

# Crear una función para abrir una ventana secundaria
def abrir_ventana():
    # Crear una ventana secundaria
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.title("Ventana Secundaria")

    # Crear una variable StringVar para almacenar el nombre introducido en la ventana secundaria
    nombre_secundario = tk.StringVar()

    # Crear un Entry para introducir el nombre
    entry_nombre = tk.Entry(ventana_secundaria, textvariable=nombre_secundario)
    entry_nombre.pack()

    # Crear un botón para aceptar el nombre introducido y cerrar la ventana
    boton_aceptar = tk.Button(ventana_secundaria, text="Aceptar", command=lambda: ventana_secundaria.destroy())
    boton_aceptar.pack()

    # Espera por la finalización de esta ventana
    ventana_secundaria.wait_window(ventana_secundaria)

    # Devolver el valor de la variable StringVar de la ventana secundaria
    return nombre_secundario.get()

# Crear un botón para abrir la ventana secundaria y asignar el valor de la variable StringVar de la ventana secundaria a la variable StringVar de la ventana principal
boton = tk.Button(ventana, text="Abrir Ventana Secundaria", command=lambda: nombre.set(abrir_ventana()))
boton.pack(padx=20, pady=20)

# Crear una etiqueta para mostrar el nombre introducido en la ventana secundaria
etiqueta_nombre = tk.Label(ventana, textvariable=nombre)
etiqueta_nombre.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
