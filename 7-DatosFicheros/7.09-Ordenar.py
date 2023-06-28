numeros = [5, 2, 9, 1, 7]
numeros.sort()
print(numeros) # Resultado: [1, 2, 5, 7, 9]
numeros.sort(reverse=True)
print(numeros) # Resultado:[9, 7, 5, 2, 1]

muebles = ["mesa", "silla", "lámpara", "estantería"]
muebles.sort()
print(muebles) # Resultado: ['estantería', 'lámpara', 'mesa', 'silla'] 
muebles.sort(reverse=True)
print(muebles) # Resultado: ['silla', 'mesa', 'lámpara', 'estantería']

#función que nos devuelve la longitud de una una cadena
def OrdenPropio(m):
  return len(m)

#ordenar en base a una función propia
muebles.sort(key= OrdenPropio)
print(muebles) # resultado: ['mesa', 'silla', 'lámpara', 'estantería']