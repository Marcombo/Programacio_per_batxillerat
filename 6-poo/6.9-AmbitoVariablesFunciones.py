def func1 (var1):
    var2 = 3
    total = var1 * var2
    var1 = 0
    return total

#la ejecución del programa empieza aquí
x = func1(3)
print (x)

#var2 es una variable distinta a la de la función
var2 = 5
x = func1(var2)
print (x)
print (var2)

#aunque la función pone var1 a 0 aquí no tiene efecto, proque son distintas
var1= 4
x = func1(var1)
print (x)
print (var1)