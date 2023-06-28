import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# decalración de la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de messagebox")
ventana.geometry("400x200")

# delcaración de la etiqueta
label = ttk.Label(ventana, text="Etiqueta")
label.config(font=("Arial", 12), foreground="black")
label.place(x=10, y=10)

# mensaje informativo
messagebox.showinfo("Información", "¡Bienvenido a mi programa!")

# mensaje respuesta SI/NO
respuesta = messagebox.askyesno("Pregunta", "¿Desea cambiar el color de la etiqueta?")

# caso de respuesta afirmativa, cambiar elementos de la etiqueta
if respuesta == True:
    label.config(font=("Times New Roman", 30),foreground="red")
    label.place (x=100,y=100)

# bucle principal
ventana.mainloop()