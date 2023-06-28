import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry('300x200')
ventana.title('Ejemplo de Frame')

# Crear un frame con borde de 2 píxeles y color azul
frame = ttk.Frame(ventana, borderwidth=2, relief="sunken")
frame.pack(expand=True, padx=10, pady=10)

# Crear una etiqueta en el frame
etiqueta = ttk.Label(frame, text='Este es un frame de ejemplo.')
etiqueta.pack(padx=10, pady=10)

# Crear un botón en el frame
boton = ttk.Button(frame, text='Cerrar', command=frame.destroy)
boton.pack(pady=10,)

# Función para mover el Frame
def mover_frame():
    if frame.winfo_exists():
        if frame.winfo_x() == 10:
            frame.place(x=50, y=50)
        else:
            frame.place(x=10, y=10)
    else:
        boton_mover.config(text='Frame ya no existe') 

# Crear un botón fuera del frame para moverlo
boton_mover = ttk.Button(ventana, text='Mover Frame', command=mover_frame)
boton_mover.pack(side="bottom",padx=10, pady=10)

# Iniciar el loop principal de la aplicación
ventana.mainloop()
