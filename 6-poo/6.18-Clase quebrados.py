class Quebrado:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumar(self, otro_quebrado):
        denominador_comun = self.denominador * otro_quebrado.denominador
        numerador1 = self.numerador * otro_quebrado.denominador
        numerador2 = otro_quebrado.numerador * self.denominador
        numerador_resultado = numerador1 + numerador2
        return Quebrado(numerador_resultado, denominador_comun)

    def restar(self, otro_quebrado):
        denominador_comun = self.denominador * otro_quebrado.denominador
        numerador1 = self.numerador * otro_quebrado.denominador
        numerador2 = otro_quebrado.numerador * self.denominador
        numerador_resultado = numerador1 - numerador2
        return Quebrado(numerador_resultado, denominador_comun)

    def multiplicar(self, otro_quebrado):
        numerador_resultado = self.numerador * otro_quebrado.numerador
        denominador_resultado = self.denominador * otro_quebrado.denominador
        return Quebrado(numerador_resultado, denominador_resultado)

    def dividir(self, otro_quebrado):
        numerador_resultado = self.numerador * otro_quebrado.denominador
        denominador_resultado = self.denominador * otro_quebrado.numerador
        return Quebrado(numerador_resultado, denominador_resultado)

    def as_float(self):
        return float(self.numerador) / self.denominador
    
    def simplificar(self):
        mcd = self.mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    @staticmethod
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a
    

q1 = Quebrado(1, 2)
q2 = Quebrado(3, 4)

q3 = q1.sumar(q2)
q4 = q1.restar(q2)
q5 = q1.multiplicar(q2)
q6 = q1.dividir(q2)
print ("quebrado1: ",q1.numerador,"/",q1.denominador)
print ("quebrado2: ",q2.numerador,"/",q2.denominador)

print("suma:",q3.numerador,"/",q3.denominador) 
print("resta:",q4.numerador,"/",q4.denominador) 
print("multiplicación:",q5.numerador,"/",q5.denominador) 
print("división:",q6.numerador,"/",q6.denominador) 

q3.simplificar()
print("simplificaicón suma:", q3.numerador,"/",q3.denominador)