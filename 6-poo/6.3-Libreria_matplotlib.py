import matplotlib.pyplot as plt

# Datos para el gráfico de barras
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
ventas = [100, 120, 90, 110, 80, 130]

# Crea el gráfico de barras
plt.bar(meses, ventas)

# Añade etiquetas y título
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas por mes")

# Muestra el gráfico
plt.show()