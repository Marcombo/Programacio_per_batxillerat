class Quebrado:
    def __init__(self, numerador=0, denominador=1):
        self.numerador = numerador
        self.denominador = denominador

    # retorna el quebrado como cadena de caracteres
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"  

    # retorna la suma de dos quebrados
    def __add__(self, otro_quebrado):
        num = self.numerador * otro_quebrado.denominador + otro_quebrado.numerador * self.denominador
        den = self.denominador * otro_quebrado.denominador
        return Quebrado(num, den)  

    # retorna la diferencia entre dos quebrados
    def __sub__(self, otro_quebrado):
        num = self.numerador * otro_quebrado.denominador - otro_quebrado.numerador * self.denominador
        den = self.denominador * otro_quebrado.denominador
        return Quebrado(num, den) 

    # retorna el producto de dos quebrados
    def __mul__(self, otro_quebrado):
        num = self.numerador * otro_quebrado.numerador
        den = self.denominador * otro_quebrado.denominador
        return Quebrado(num, den) 
    
    # retorna la división entre dos quebrados
    def __truediv__(self, otro_quebrado):
        num = self.numerador * otro_quebrado.denominador
        den = self.denominador * otro_quebrado.numerador
        return Quebrado(num, den)  
    
    # retorna un quebrado simplificado
    def simplificar(self):
        comun_div = self.mcd(self.numerador, self.denominador)
        self.numerador //= comun_div
        self.denominador //= comun_div  

    # retorna el valor real de la división
    def valor_real(self):
        return self.numerador / self.denominador  # retorna el valor decimal del quebrado

    # retorna un quebrado invertido
    def invertir(self):        
        self.numerador, self.denominador = self.denominador, self.numerador  # intercambia numerador y denominador

    #   Método estático que calcula el máximo común divisor usando el algoritmo de Euclides
    @staticmethod
    def mcd(a, b):
        if b == 0:
            return a
        return Quebrado.mcd(b, a % b)