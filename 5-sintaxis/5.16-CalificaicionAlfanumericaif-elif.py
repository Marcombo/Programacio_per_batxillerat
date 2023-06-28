# Pedimos al usuario una nota numérica
nota = float(input("Dame tu nota de 0 a 10: "))

# Asignamos la nota alfanumérica
if nota >= 9 and nota <= 10:
    nota_alfanumerica = "Sobresaliente"
elif nota >= 7:
    nota_alfanumerica = "Notable"
elif nota >= 6:
    nota_alfanumerica = "Bien"
elif nota >= 5:
    nota_alfanumerica = "Suficiente"
else:
    nota_alfanumerica = "Suspenso"

# Imprimimos la nota alfanumérica encontrada
print("Tu nota alfanumérica es:", nota_alfanumerica)