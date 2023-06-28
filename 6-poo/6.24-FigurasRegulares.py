class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass


class FiguraGeometricaRegular(FiguraGeometrica):
    def __init__(self, nombre, lado, numero_lados):
        super().__init__(nombre)
        self.lado = lado
        self._numero_lados = numero_lados

    @property
    def numero_lados(self):
        return self._numero_lados

    def perimetro(self):
        return self.lado * self.numero_lados


class TrianguloEquilatero(FiguraGeometricaRegular):
    def __init__(self, lado):
        super().__init__('Triángulo Equilátero', lado, 3)

    def area(self):
        return (self.lado ** 2) * 0.4330127


class CuadradoRegular(FiguraGeometricaRegular):
    def __init__(self, lado):
        super().__init__('Cuadrado', lado, 4)

    def area(self):
        return self.lado ** 2


class PentagonoRegular(FiguraGeometricaRegular):
    def __init__(self, lado):
        super().__init__('Pentágono', lado, 5)

    def area(self):
        # Calculamos el área de un pentágono regular con la fórmula
        # (lado ^ 2) * (5 * (5 + 2 * (5 ^ 0.5))) / 4
        return (self.lado ** 2) * 1.7204774

class HexagonoRegular(FiguraGeometricaRegular):
    def __init__(self, lado):
        super().__init__('Hexágono', lado, 6)

    def area(self):
        # Calculamos el área de un hexágono regular con la fórmula
        # (3 * lado ^ 2 * 3 * (3 ^ 0.5)) / 2
        return (3 * self.lado ** 2 * 3 * (3 ** 0.5)) / 2


# Creamos una instancia de un triángulo equilátero, calculamos su área y perímetro,
# e imprimimos su nombre, área, perímetro y número de lados.
triangulo = TrianguloEquilatero(6)
print("Nombre figura:",triangulo.nombre)
print("Área:",triangulo.area())
print("Perímetro",triangulo.perimetro())
print("Número de lados",triangulo.numero_lados)

# Creamos una instancia de un cuadrado regular, calculamos su área y perímetro,
# e imprimimos su nombre, área, perímetro y número de lados.
cuadrado = CuadradoRegular(5)
print("Nombre figura:",cuadrado.nombre)
print("Área:",cuadrado.area())
print("Perímetro",cuadrado.perimetro())
print("Número de lados",cuadrado.numero_lados)

# Creamos una instancia de un pentágono regular, calculamos su área y perímetro,
# e imprimimos su nombre, área, perímetro y número de lados.
pentagono = PentagonoRegular(4)
print("Nombre figura:",pentagono.nombre)
print("Área:",pentagono.area())
print("Perímetro",pentagono.perimetro())
print("Número de lados",pentagono.numero_lados)

# Creamos una instancia de un hexágono regular, calculamos su área y perímetro,
# e imprimimos su nombre, área, perímetro y número de lados
hexagono = HexagonoRegular(3)
print("Nombre figura:",hexagono.nombre)
print("Área:",hexagono.area())
print("Perímetro",hexagono.perimetro())
print("Número de lados",hexagono.numero_lados)