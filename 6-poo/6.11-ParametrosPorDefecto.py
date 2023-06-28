def calcular_precio(base, impuesto=0.21): 
    return base + (base * impuesto)

# Calculamos el precio con el impuesto por defecto
print (calcular_precio(145))
# Calculamos el precio con el impuesto del 4%
print (calcular_precio(210, 0.04))
