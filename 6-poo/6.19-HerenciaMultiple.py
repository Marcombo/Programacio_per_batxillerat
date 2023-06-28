#clase padre1
class A:
    def print_a(self):
        print('a')

#clase padre2
class B:
    def print_b(self):
        print('b')

#clase hija que hereda de dos padres
class C(A, B):
    def print_c(self):
        print('c')

c = C() #instanciación de clase hija
c.print_a() #uso de un método de la clase padre
c.print_b() #uso de un método de otra clase padre
c.print_c() #uso de un méotodo propio