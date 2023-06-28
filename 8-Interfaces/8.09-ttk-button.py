import tkinter as tk
from tkinter import ttk

# decalración de la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de botón TTK")
ventana.geometry("400x200")

#función manejadora del evento
def click_button():
    ventana.title("OK")

#declaración de botón con su evento clic asociado
boton = ttk.Button(ventana, text="Haz clic aquí", command=click_button)
#posicionamiento en la ventana
boton.place(x=5,y=5,width=300, height=100)

#bucle principal
ventana.mainloop()