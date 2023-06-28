texto = input ("Introduce un texto: ")
contador = 0

#recorrer cada letra de la palabra
for letra in texto:
    if letra == "a" or letra =="A":
        contador += 1

#mostrar resultado
print("He encontrado",contador, "veces la letra a/A.")