# Pedir al usuario el tipo de figura
tipo_figura = input("Dime una figura \n(T)riángulo\n(C)uadrado\(R)ectángulo): ")

# Calcular el área según el tipo de figura usando match...case
match tipo_figura:
    case "T":
        base = float(input("Base del triángulo: "))
        altura = float(input("Altura del triángulo: "))
        area = 0.5 * base * altura
        print(f"El área del triángulo es: {area}")
    case "c":
        lado = float(input("Longitud del lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    case "R":
        ancho = float(input("Ancho del rectángulo: "))
        largo = float(input("Largo del rectángulo: "))
        area = ancho * largo
        print(f"El área del rectángulo es: {area}")
    case _:
        print("Tipo de figura no válido")
