import tkinter as tk
from tkinter import ttk

def update_progress():
    value = spinbox.get()
    progress['value'] = int(value)

# Crear la ventana principal
window = tk.Tk()
window.title("Ejemplo de Spinbox y ProgressBar")
window.geometry("300x150")

# Crear el Spinbox
spinbox = tk.Spinbox(window, from_=0, to=100, width=5)
spinbox.pack(pady=10)

# Crear la ProgressBar
progress = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress.pack(pady=10)

# Botón para actualizar el progreso
button = tk.Button(window, text="Actualizar", command=update_progress)
button.pack(pady=10)

# Ejecutar el bucle principal
window.mainloop()
