#función saludo con parámetros
def saludo(hora):
    if hora >= 6 and hora < 14:
        print("¡Buenos días! ¿Cómo estás?")
    elif hora >= 14 and hora < 20:
        print("¡Buenas tardes! ¿Cómo estás?")
    else:
        print("¡Buenas noches! ¿Cómo estás?")

#invocación a la función con distintos parámetros
saludo(10) 
saludo(15)
saludo(22)