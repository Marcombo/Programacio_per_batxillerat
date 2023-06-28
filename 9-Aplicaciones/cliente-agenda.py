import requests

# URL del servidor Flask
url = "https://luin.pythonanywhwere.com/app-agenda"

# Función para mostrar la lista de contactos
def show_contacts():
    response = requests.get(url)
    if response.ok:
        contacts = response.json()
        print("Contactos:")
        for contact in contacts:
            print(f"{contact['name']}: {contact['phone']}")
    else:
        print("Error al recuperar la lista de contactos")

# Función para agregar un contacto
def add_contact(name, phone):
    data = {"name": name, "phone": phone}
    response = requests.post(f"{url}/add", data=data)
    if response.ok:
        print("Contacto agregado exitosamente")
    else:
        print("Error al agregar el contacto")

# Solicitar al usuario que seleccione una opción
while True:
    print("Seleccione una opción:")
    print("1. Mostrar lista de contactos")
    print("2. Agregar contacto")
    print("0. Salir")
    option = input("> ")

    if option == "1":
        show_contacts()
    elif option == "2":
        name = input("Nombre del contacto: ")
        phone = input("Teléfono del contacto: ")
        add_contact(name, phone)
    elif option == "0":
        break
    else:
        print("Opción inválida")
