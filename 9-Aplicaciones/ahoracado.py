from tkinter import *
from tkinter import messagebox
import random

class Ahorcado:
    def __init__(self, master):
        self.master = master
        master.title("Ahorcado")
        icono = PhotoImage(file ="imgAhorcado/hangman32.png")
        master.iconphoto(True,icono)        
        
        # Variables
        self.intentos = 0
        self.letras_adivinadas = []

        # Frames
        self.letras_frame = Frame(master)
        self.letras_frame.pack()

        self.palabra_frame = Frame(master)
        self.palabra_frame.pack()

        self.juego_frame = Frame(master)
        self.juego_frame.pack()

        # Letras
        self.letras = "abcdefghijklmnñopqrstuvwxyz"
        self.botones_letras = []

        # Crear botones para cada letra del alfabeto
        for letra in self.letras:
            # Cada botón llama al método adivinar_letra con la letra correspondiente como argumento
            boton = Button(self.letras_frame, text=letra, command=lambda letra=letra: self.adivinar_letra(letra), state=DISABLED)
            boton.pack(side=LEFT)
            self.botones_letras.append(boton)

        # Palabra
        self.label_palabra = Label(self.palabra_frame, font=("Arial", 24))
        self.label_palabra.pack()

        # Juego
        self.imagenes = ["ahorcado0.png","ahorcado1.png", "ahorcado2.png", "ahorcado3.png", "ahorcado4.png", "ahorcado5.png", "ahorcado6.png"]
        self.imagen_ahorcado = PhotoImage(file="imgAhorcado/" + self.imagenes[self.intentos])
        self.label_imagen = Label(self.juego_frame, image=self.imagen_ahorcado)
        self.label_imagen.pack()

        self.boton_nuevo_juego = Button(self.juego_frame, text="Nuevo Juego", command=self.nuevo_juego)
        self.boton_nuevo_juego.pack()

    def mostrar_palabra(self):
        # Mostrar las letras adivinadas y los espacios en blanco para las letras no adivinadas
        resultado = ""
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                resultado += letra
            else:
                resultado += "_ "
        return resultado

    def adivinar_letra(self, letra):
        # Si la letra adivinada está en la palabra, actualizar las letras adivinadas y la palabra en la pantalla
        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
            self.label_palabra.config(text=self.mostrar_palabra())
            # Si todas las letras de la palabra han sido adivinadas, el usuario ha ganado
            if "_" not in self.mostrar_palabra():
                self.ganaste_juego()
        else:
            # Si la letra adivinada no está en la palabra, actualizar la imagen del ahorcado y el número de intentos
            self.intentos += 1
            if self.intentos == 7:
                # Si el número máximo de intentos ha sido alcanzado, el usuario ha perdido
                self.perdiste_juego()
            else:
                self.imagen_ahorcado = PhotoImage(file="imgAhorcado/" + self.imagenes[self.intentos])
                self.label_imagen.config(image=self.imagen_ahorcado)

        # Desactivar el botón correspondiente a la letra adivinada
        self.botones_letras[self.letras.index(letra)].config(state=DISABLED)

    def nuevo_juego(self):
        # Abrir archivo de palabras y elegir una al azar
        with open("dictAhorcado/palabras.txt", "r") as archivo:
            palabras = [linea.strip() for linea in archivo.readlines()]
            self.palabra = random.choice(palabras)
        # Reiniciar variables del juego
        self.intentos = 0
        self.letras_adivinadas = []
        # Actualizar la palabra en la pantalla
        self.label_palabra.config(text=self.mostrar_palabra())
        # Reiniciar imagen del ahorcado
        self.imagen_ahorcado = PhotoImage(file="imgAhorcado/" + self.imagenes[self.intentos])
        self.label_imagen.config(image=self.imagen_ahorcado)
        # Activar botones de letras y desactivar botón de nuevo juego
        for boton in self.botones_letras:
            boton.config(state=NORMAL)
        self.boton_nuevo_juego.config(state=DISABLED)

    def ganaste_juego(self):
        # Mostrar mensaje de victoria y preguntar si se quiere jugar de nuevo
        mensaje = "¡Ganaste! ¿Quieres jugar de nuevo?"
        if messagebox.askyesno("Ahorcado", mensaje):
            self.nuevo_juego()
        else:
            self.master.destroy()
        # Activar botón de nuevo juego
        self.boton_nuevo_juego.config(state=NORMAL)

    def perdiste_juego(self):
        # Mostrar mensaje de derrota y la palabra que se intentaba adivinar, y preguntar si se quiere jugar de nuevo
        mensaje = "¡Perdiste! La palabra era '{}'. ¿Quieres jugar de nuevo?".format(self.palabra)
        if messagebox.askyesno("Ahorcado", mensaje):
            self.nuevo_juego()
        else:
            self.master.destroy()
        # Activar botón de nuevo juego
        self.boton_nuevo_juego.config(state=NORMAL)

if __name__ == '__main__':
    ventana = Tk()
    ahorcado = Ahorcado(ventana)
    ventana.mainloop()