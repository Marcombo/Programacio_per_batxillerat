import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry('300x300')
ventana.title("PRINCIPAL")

# Crear una función para abrir una ventana secundaria
def abrir_ventana():
    # Crear una ventana secundaria
    ventana_secundaria = tk.Toplevel(ventana)
    ventana_secundaria.geometry('300x100')
    ventana_secundaria.title("Ventana Secundaria")

    # Agregar contenido a la ventana secundaria
    etiqueta = tk.Label(ventana_secundaria, text="Esta es una ventana secundaria")
    etiqueta.pack(padx=20, pady=20)

# Crear un botón para abrir la ventana secundaria
boton = tk.Button(ventana, text="Abrir Ventana Secundaria", command=abrir_ventana)
boton.pack(padx=20, pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
