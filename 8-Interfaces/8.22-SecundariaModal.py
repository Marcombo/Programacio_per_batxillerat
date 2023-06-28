import tkinter as tk
from tkinter import ttk

def abrir_ventana_modal():
    # Crear la ventana secundaria
    ventana_modal = tk.Toplevel(ventana)
    ventana_modal.geometry('200x200')
    
    # Hacer la ventana secundaria modal
    ventana_modal.grab_set()

ventana = tk.Tk()
ventana.geometry('300x300')

# Crear un botón para abrir la ventana secundaria modal
button = ttk.Button(ventana, text='Abrir ventana modal', command=abrir_ventana_modal)
button.pack(pady=50)

ventana.mainloop()
