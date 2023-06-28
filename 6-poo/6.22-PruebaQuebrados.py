from ClaseQuebrado import Quebrado

# Creamos dos objetos Quebrado
q1 = Quebrado(1, 2)
q2 = Quebrado(3, 4)

# Sumamos y restamos los dos objetos
q_suma = q1 + q2
q_resta = q1 - q2

# Mostramos los resultados
print("La suma de", q1, "y", q2, "es", q_suma)
print("La resta de", q1, "y", q2, "es", q_resta)

# Multiplicamos y dividimos los dos objetos
q_producto = q1 * q2
q_division = q1 / q2

# Mostramos los resultados
print("El producto de", q1, "y", q2, "es", q_producto)
print("La división de", q1, "y", q2, "es", q_division)

# Invertimos un objeto
q_invertido = q1.invertir()

# Mostramos el resultado
print("El quebrado invertido de", q1, "es", q_invertido)

# Simplificamos un objeto
q_simplificado = Quebrado(8, 12)
q_simplificado.simplificar()

# Mostramos el resultado
print("El quebrado", Quebrado(8, 12), "simplificado es", q_simplificado)

# Calculamos el valor decimal de un objeto
q_valor_real = Quebrado(3, 5)
valor_real = q_valor_real.valor_real()

# Mostramos el resultado
print("El valor decimal de", q_valor_real, "es", valor_real)
