class Ejemplo:
    def __init__(self):
        self._atributo_con_guion = "Atributo con guion"
        self.__atributo_con_doble_guion = "Atributo con doble guion"

    def metodo_ejemplo(self):
        print(self._atributo_con_guion)
        print(self.__atributo_con_doble_guion)

ejemplo = Ejemplo()

# Uso de los atributos desde dentro de la clase
ejemplo.metodo_ejemplo()

# Accediendo al atributo con guion
print(ejemplo._atributo_con_guion)  # Salida: "Atributo con guion"

# Accediendo al atributo con doble guion
# Esto dará un error ya que no podemos acceder fuera de la clase.
print(ejemplo.__atributo_con_doble_guion)
