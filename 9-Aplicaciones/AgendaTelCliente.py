# Instalar con: pip install requests
import requests

# Envía una petición GET a la URL https://luin.pythonanywhere.com/hi/ y muestra la respuesta
response = requests.get("https://luin.pythonanywhere.com/hi/")
print(response.content.decode())

# Envía una petición GET a la URL https://luin.pythonanywhere.com/list y muestra la respuesta
response = requests.get("https://luin.pythonanywhere.com/listar")
print(response.content.decode())

# Busca el número de teléfono de un contacto en particular
nombre = 'Pepe'
response = requests.get('https://luin.pythonanywhere.com/buscar/', params={'nombre': nombre})
if response.status_code == 200:
    print(f"El teléfono de {nombre} es {response.text}")
else:
    print(f"No se encontró ningún contacto con el nombre {nombre}")

# Busca los contactos que empiezan con una letra en particular
letra = 'P'
response = requests.get('https://luin.pythonanywhere.com/listarLetra/',params={'letra': letra})
print (response)
if response.status_code == 200:
    print("Contactos que empiezan con la letra", letra)
    print(response.text)
else:
    print(f"No se encontraron contactos que empiecen con la letra {letra}")

# Inserta un nuevo contacto
nombre = 'Pepe'
telefono = '123456789'
response = requests.get('https://luin.pythonanywhere.com/insertar/', params={'nombre': nombre, 'telefono': telefono})
if response.status_code == 200:
    print(f"Contacto '{nombre}' añadido correctamente")
else:
    print(f"No se pudo añadir el contacto '{nombre}'")
