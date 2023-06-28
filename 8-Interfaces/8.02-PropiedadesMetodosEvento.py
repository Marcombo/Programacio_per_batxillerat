import tkinter as tk
from tkinter import messagebox

def mostrarPosicion(event):    
    # Mostrar la posición
    message = f"Clic en ({event.x}, {event.y})"
    messagebox.showinfo("Posición", message)

def ApareceDesaparece():
    #comprobar si está actualmente visiable
    if ventana.winfo_viewable():
        ventana.withdraw()
    else:
        ventana.deiconify()
    ventana.after(3000, ApareceDesaparece)

# Crear una ventana
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ventana.geometry("300x200")

# Establecer otro color de fondo
ventana.configure(background="green")

# Establecer el título de la ventana
ventana.title("Mi Ventana")

# Asociar un evanto a una función (clic botón principal ratón)
ventana.bind("<Button-1>", mostrarPosicion)

# Programar la primera llamada después de cinco segundos
ventana.after(3000, ApareceDesaparece)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
