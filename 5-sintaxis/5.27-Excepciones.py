#excepción genérica sin especificar tipo
try:
    x = 10 / 0
except :
    print("No se puede dividir entre cero.")

#excepción en la conversión a numérico
try:
    x = int(input("Introduce un número: "))
except ValueError:
    print("Debes introducir un número válido.")

#excepción con múltiples posibilidades
try:
    a = int(input("Introduce un número: "))
    b = int(input("Introduce otro número: "))
    resultado = a / b
    print("El resultado es:", resultado)
except ValueError:
    print("Debes dar valores numéricos.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
#en cualquier otra excepción mostraría el error asociado
except Exception as e:
    print("Ha ocurrido una excepción:", e)
