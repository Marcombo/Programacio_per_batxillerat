#función que devuelve area de un cuadrilátero
def area_cuadrilatero(b, a):
    area = b * a
    return area

#pruebas de cálculo
base = 35
altura = 8
areaC = area_cuadrilatero(base,altura)
print (f"El area de un cuadrilátero de {base}x{altura} es: {areaC}")