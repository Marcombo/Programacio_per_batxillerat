import tkinter as tk
from tkinter import messagebox, Toplevel, scrolledtext
import datetime

class Calculadora:
    def __init__(self, master):
        self.numeros = ""
        self.master = master
        master.title("Calculadora")

        # Pantalla
        self.lbl = tk.Label(master, text=self.numeros, font=("Arial", 15), width=30, height=2, anchor="e", bg="white", bd=5)
        self.lbl.pack(side=tk.TOP, pady=5)

        # Fila 1 de botones
        fila1 = tk.Frame(master)
        fila1.pack(side=tk.TOP, pady=5)

        self.btn7 = tk.Button(fila1, text="7", width=4, height=2, command=lambda:self.agregar("7"))
        self.btn7.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn8 = tk.Button(fila1, text="8", width=4, height=2, command=lambda:self.agregar("8"))
        self.btn8.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn9 = tk.Button(fila1, text="9", width=4, height=2, command=lambda:self.agregar("9"))
        self.btn9.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_div = tk.Button(fila1, text="/", width=4, height=2, command=lambda:self.calcular("/"))
        self.btn_div.pack(side=tk.LEFT, padx=5, pady=5)

        # Fila 2 de botones
        fila2 = tk.Frame(master)
        fila2.pack(side=tk.TOP, pady=5)

        self.btn4 = tk.Button(fila2, text="4", width=4, height=2, command=lambda:self.agregar("4"))
        self.btn4.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn5 = tk.Button(fila2, text="5", width=4, height=2, command=lambda:self.agregar("5"))
        self.btn5.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn6 = tk.Button(fila2, text="6", width=4, height=2, command=lambda:self.agregar("6"))
        self.btn6.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_mult = tk.Button(fila2, text="*", width=4, height=2,command=lambda:self.calcular("*"))
        self.btn_mult.pack(side=tk.LEFT, padx=5, pady=5)

        # Fila 3 de botones
        fila3 = tk.Frame(master)
        fila3.pack(side=tk.TOP, pady=5)

        self.btn1 = tk.Button(fila3, text="1", width=4, height=2, command=lambda:self.agregar("1"))
        self.btn1.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn2 = tk.Button(fila3, text="2", width=4, height=2, command=lambda:self.agregar("2"))
        self.btn2.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn3 = tk.Button(fila3, text="3", width=4, height=2, command=lambda:self.agregar("3"))
        self.btn3.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_resta = tk.Button(fila3, text="-", width=4, height=2, command=lambda:self.calcular("-"))
        self.btn_resta.pack(side=tk.LEFT, padx=5, pady=5)

        # Fila 4 de botones
        fila4 = tk.Frame(master)
        fila4.pack(side=tk.TOP, pady=5)

        self.btn_punto = tk.Button(fila4, text=".", width=4, height=2, command=lambda:self.agregar("."))
        self.btn_punto.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn0 = tk.Button(fila4, text="0", width=9, height=2, command=lambda:self.agregar("0"))
        self.btn0.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_suma = tk.Button(fila4, text="+", width=4, height=2, command=lambda:self.calcular("+"))
        self.btn_suma.pack(side=tk.LEFT, padx=5, pady=5)

        # Fila 5 de botones
        fila5 = tk.Frame(master)
        fila5.pack(side=tk.TOP, pady=5)

        self.btn_clear = tk.Button(fila5, text="C", width=4, height=2, command=lambda:self.borrar())
        self.btn_clear.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_igual = tk.Button(fila5, text="=", width=9, height=2, command=lambda:self.calcular("="))
        self.btn_igual.pack(side=tk.LEFT, padx=5, pady=5)

        
        self.boton_ver = tk.Button(fila5, text="<...>", width=4, height=2, command=self.ver_operaciones)
        self.boton_ver.pack(side=tk.LEFT, padx=5, pady=5)

        self.inicializar_operandos()

    def inicializar_operandos(self):
        self.operando1 = "0"
        self.operando2 = ""
        self.operador = "+"
        self.lbl.config(text =self.operando1)


    def agregar(self, numero):
        self.operando2 += str(numero)
        self.lbl.config(text=self.operando2)

    def borrar(self):
        self.inicializar_operandos()

    def calcular(self, operacion):
        try:      
            self.guardar_operacion()
            if self.operador != "=":
                self.operando1 = str( eval (self.operando1 + self.operador + self.operando2)).replace(".0", "")
            self.operador = operacion
            self.operando2= ""
            self.lbl.config(text =self.operando1)
        except ZeroDivisionError:
            self.lbl.config(text="Error: Division por cero")
            self.inicializar_operandos()
        except Exception as e:
            self.lbl.config(text="Error")
            self.inicializar_operandos()
        return

    def guardar_operacion(self):
        # Obtener la fecha y hora actual
        now = datetime.datetime.now()
        d_m_a_h_m_s = now.strftime("%d-%m-%Y %H:%M:%S")
        # Abrir el archivo en modo de escritura y añadir el argumento 'a' para agregar líneas
        with open("operaciones.txt", "a") as archivo:
            # Construir la cadena de texto con la información de la operación y la fecha y hora actual
            operacion = f"{d_m_a_h_m_s} {self.operando1} {self.operador} {self.operando2} = {eval(self.operando1 + self.operador + self.operando2)}\n"
            archivo.write(operacion)

    def ver_operaciones(self):
        try:
            with open("operaciones.txt", "r") as archivo:
                contenido = archivo.read()
            top = Toplevel(self.master)
            top.title("Operaciones Realizadas")
            # crear un widget de texto multi-línea
            txt = scrolledtext.ScrolledText(top, width=50, height=20)
            txt.pack(expand=True, fill='both')
            txt.insert(tk.END, contenido)

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no se encontró")

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()