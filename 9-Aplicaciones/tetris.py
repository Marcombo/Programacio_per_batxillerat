from tkinter import *
from tkinter import messagebox
import random

VELOCIDAD_INICIAL = 1000 # 1 segundo
ACELERACION = 5 

CELDAS_HORIZONTAL = 10
CELDAS_VERTICAL = 20

ANCHO_TABLERO = CELDAS_HORIZONTAL *2
ALTO_TABLERO = CELDAS_VERTICAL*2
TAM_CELDA =10

class Tetris:
    def __init__(self, master):
        self.master = master
        master.title("Tetris")
        self.timer_on =False

        # Variables
        self.tablero = [[0] * CELDAS_HORIZONTAL for _ in range(CELDAS_VERTICAL)]
        self.figuras = ["I", "O", "T", "S", "Z", "J", "L"]
        self.figura_actual = None
        self.posicion_actual = [0, 0]
        self.puntuacion = 0

        # Frames
        self.tablero_frame = Frame(master)
        self.tablero_frame.pack(side=LEFT)

        self.puntuacion_frame = Frame(master)
        self.puntuacion_frame.pack(side=RIGHT)
 
        # Crear el objeto Canvas para dibujar el tablero
        self.tablero_canvas = Canvas(self.tablero_frame, width=ANCHO_TABLERO * TAM_CELDA, height=ALTO_TABLERO * TAM_CELDA, bg="black")
        self.tablero_canvas.pack()

        # Crear una lista para guardar los objetos Canvas de las celdas del tablero
        self.celdas_canvas = []
        for i in range(ALTO_TABLERO):
            fila = []
            for j in range(ANCHO_TABLERO):
                x1 = j * TAM_CELDA
                y1 = i * TAM_CELDA
                x2 = x1 + TAM_CELDA
                y2 = y1 + TAM_CELDA
                celda = self.tablero_canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="white")
                fila.append(celda)
            self.celdas_canvas.append(fila)

        # Crear una lista para guardar los objetos Canvas de las celdas de la figura actual
        self.figura_canvas = []
        for i in range(ALTO_TABLERO):
            fila = []
            for j in range(ANCHO_TABLERO):
                fila.append(None)
            self.figura_canvas.append(fila)

        # Puntuacion
        self.puntuacion_label = Label(self.puntuacion_frame, text="Puntuacion: 0")
        self.puntuacion_label.pack()

        # Controles
        self.master.bind("<Left>", lambda event: self.mover_figura("izquierda"))
        self.master.bind("<Right>", lambda event: self.mover_figura("derecha"))
        self.master.bind("<Down>", lambda event: self.mover_figura("abajo"))
        self.master.bind("<Up>", lambda event: self.rotar_figura())

        # Iniciar juego
        self.nuevo_juego()

        # Iniciamos temporizador
        self.timer() 

    def nuevo_juego(self):
        self.tablero = [[0] * CELDAS_HORIZONTAL for _ in range(CELDAS_VERTICAL)]
        self.puntuacion = 0
        self.timer_on =True
        self.puntuacion_label.config(text="Puntuación: {}".format(self.puntuacion))
        self.dibujar_tablero()
        self.nueva_figura()

    def nueva_figura(self):
        figura = random.choice(self.figuras)
        self.figura_actual = self.get_figura(figura)
        self.posicion_actual = [0, 3]
        if self.colisiona(self.figura_actual, self.posicion_actual):
            self.game_over()
        else:
            self.dibujar_figura(self.figura_actual, self.posicion_actual)

    def get_figura(self, figura):
        if figura == "I":
            return [[1, 1, 1, 1]]
        elif figura == "O":
            return [[1, 1], [1, 1]]
        elif figura == "T":
            return [[0, 1, 0], [1, 1, 1]]
        elif figura == "S":
            return [[0, 1, 1], [1, 1, 0]]
        elif figura == "Z":
            return [[1, 1, 0], [0, 1, 1]]
        elif figura == "J":
            return [[1, 0, 0], [1, 1, 1]]
        elif figura == "L":
            return [[0, 0, 1], [1, 1, 1]]

    def dibujar_tablero(self):
        self.tablero_canvas.delete(ALL)
        for i in range(CELDAS_VERTICAL):
            for j in range(CELDAS_HORIZONTAL):
                if self.tablero[i][j] != 0:
                    self.tablero_canvas.create_rectangle(j * CELDAS_VERTICAL, i * CELDAS_VERTICAL, (j + 1) * CELDAS_VERTICAL, (i + 1) * CELDAS_VERTICAL, fill="white")

    def dibujar_figura(self, figura, posicion):
        color = self.get_color(figura)
        for i in range(len(figura)):
            for j in range(len(figura[0])):
                if figura[i][j] != 0:
                    x = (posicion[1] + j) * CELDAS_VERTICAL
                    y = (posicion[0] + i) * CELDAS_VERTICAL
                    self.tablero_canvas.create_rectangle(x, y, x + CELDAS_VERTICAL, y + CELDAS_VERTICAL, fill=color)
    
    def get_color(self, figura):
            if (figura == [[1, 1, 1, 1]] or 
                figura == [[1], [1], [1], [1]]) :
                return "cyan"
            elif figura == [[1, 1], [1, 1]]:
                return "yellow"
            elif (figura == [[0, 1, 0], [1, 1, 1]] or 
                  figura == [[1, 1, 1], [0, 1, 0]]  or
                  figura == [[0, 1], [1, 1], [0, 1]] or
                  figura == [[1, 0], [1, 1], [1, 0]] ):
                return "purple"
            elif (figura == [[0, 1, 1], [1, 1, 0]] or 
                  figura ==[[1, 0], [1, 1], [0, 1]]):
                return "green"
            elif (figura == [[1, 1, 0], [0, 1, 1]]or 
                figura ==[[0, 1], [1, 1], [1, 0]]):
                return "red"
            elif (figura == [[1, 0, 0], [1, 1, 1]]  or 
                  figura ==[[1, 1], [1, 0], [1, 0]] or 
                  figura ==[[1, 1, 1], [0, 0, 1]]   or 
                  figura ==[[0, 1], [0, 1], [1, 1]]):
                return "blue"
            elif (figura == [[0, 0, 1], [1, 1, 1]]  or 
                  figura ==[[1, 1], [0, 1], [0, 1]] or 
                  figura ==[[1, 1, 1], [1, 0, 0]]   or 
                  figura ==[[1, 0], [1, 0], [1, 1]]):
                return "orange"
            else:
                return "pink"

    def mover_figura(self, direccion):
        dx = 0
        dy = 0
        if direccion == "izquierda":
            dx = -1
        elif direccion == "derecha":
            dx = 1
        elif direccion == "abajo":
            dy = 1
        nueva_posicion = [self.posicion_actual[0] + dy, self.posicion_actual[1] + dx]
        if not self.colisiona(self.figura_actual, nueva_posicion):
            self.borrar_figura()
            self.posicion_actual = nueva_posicion
            self.dibujar_figura(self.figura_actual, self.posicion_actual)
        else:
            if direccion == "abajo":
                self.fijar_figura()


    def borrar_figura(self):
        for i in range(len(self.figura_actual)):
            for j in range(len(self.figura_actual[0])):
                if self.figura_actual[i][j] != 0:
                    x = (self.posicion_actual[1] + j) * CELDAS_VERTICAL
                    y = (self.posicion_actual[0] + i) * CELDAS_VERTICAL
                    self.tablero_canvas.create_rectangle(x, y, x + CELDAS_VERTICAL, y + CELDAS_VERTICAL, fill="black")
                    self.figura_canvas[i+self.posicion_actual[0]][j+self.posicion_actual[1]] = None

    def rotar_figura(self):
        figura_rotada = []
        for j in range(len(self.figura_actual[0])-1, -1, -1):
            fila = []
            for i in range(len(self.figura_actual)):
                fila.append(self.figura_actual[i][j])
            figura_rotada.append(fila)
        if not self.colisiona(figura_rotada, self.posicion_actual):
            self.borrar_figura()
            self.figura_actual = figura_rotada
            self.dibujar_figura(self.figura_actual, self.posicion_actual)

    def colisiona(self, figura, posicion):
        for i in range(len(figura)):
            for j in range(len(figura[0])):
                if figura[i][j] != 0:
                    fila = i + posicion[0]
                    columna = j + posicion[1]
                    if fila < 0 or fila >= CELDAS_VERTICAL or columna < 0 or columna >= CELDAS_HORIZONTAL or self.tablero[fila][columna] != 0:
                        return True
        return False

    def generar_nueva_figura(self):
        figura = random.choice(self.figuras)
        posicion = [0, random.randint(0, 9 - len(figura[0]))]
        if self.colisiona(figura, posicion):
            self.game_over()
        else:
            self.figura_actual = figura
            self.posicion_actual = posicion
            self.dibujar_figura(self.figura_actual, self.posicion_actual)

    def fijar_figura(self):
        # Recorrer la figura actual y actualizar el tablero
        figura = self.figura_actual
        posicion = self.posicion_actual
        for i in range(len(figura)):
            for j in range(len(figura[0])):
                if figura[i][j] != 0:
                    fila = posicion[0] + i
                    columna = posicion[1] + j
                    self.tablero[fila][columna] = figura[i][j]

        # Eliminar filas completas y actualizar puntuación
        self.eliminar_filas_completas()
      
        # Dibujar el tablero actualizado
        self.dibujar_tablero()

        # Crear una nueva figura
        self.nueva_figura()


    def eliminar_filas_completas(self):
        # Recorrer las filas del tablero       
        for i in range(0, CELDAS_VERTICAL):
            # Verificar si la fila está completa
            if all(self.tablero[i]):               
                # Eliminar la fila del tablero
                del self.tablero[i]
                # Añadir una nueva fila vacía en la parte superior del tablero
                self.tablero.insert(0, [0] * CELDAS_HORIZONTAL)
                # Incrementar la puntuación en 10 puntos
                self.puntuacion += 10
                # Actualizar la etiqueta de la puntuación
                self.puntuacion_label.config(text="Puntuación: {}".format(self.puntuacion))
   
    def game_over(self): 
        self.timer_on =False      
        answer =   messagebox.askyesno("Game Over", "¿Deseas jugar otra partida?")
        if answer:
            self.nuevo_juego()
        else:
            self.master.destroy() # suponiendo que "ventana" es el nombre de la ventana actual

    def timer(self):
        # Iniciar temporizador para ejecutar la función mover_figura cada cierto tiempo
        if self.timer_on:
            self.mover_figura("abajo")
        self.velocidad = VELOCIDAD_INICIAL - self.puntuacion * ACELERACION
        self.master.after(self.velocidad, self.timer)

if __name__ == '__main__':    
    v = Tk()
    Tetris(v)
    v.mainloop()