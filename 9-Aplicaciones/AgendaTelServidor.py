# Importa los módulos y funciones necesarios
from django.urls import path
from django.http import HttpResponse
import csv
import os

# Define una función de vista para saludar
def say_hello(request):
    return HttpResponse("Hola soy el servidor de agenda")

# Define una función de vista para listar todos los contactos de un archivo CSV
def listing(request):
    # Obtiene la ruta al archivo CSV
    csv_path = os.path.abspath('./agenda/agenda/listing-agenda.csv')
    # Abre el archivo CSV y lee su contenido
    with open(csv_path) as f:
        # Crea un objeto DictReader a partir del contenido del archivo
        reader = csv.DictReader(f)
        # Lee todos los datos del archivo y los guarda en una lista
        data = [row for row in reader]

        # Crea un texto que contiene el nombre y el teléfono de cada contacto
        text = ""
        for row in data:
            text += f"{row['nombre']}: {row['telefono']}\n"
        # Retorna el texto como respuesta HTTP con el tipo de contenido 'text/plain'
        return HttpResponse(text, content_type="text/plain")

# Define una función de vista para insertar un nuevo contacto en el archivo CSV
def insertar_contacto(request):
    if request.method == "GET":
        # Obtiene los datos del nuevo contacto del cuerpo de la solicitud
        nombre = request.GET.get('nombre','')
        telefono = request.GET.get('telefono','')
        # Verifica que se proporcionaron los datos necesarios
        if nombre and telefono:
            # Agrega el nuevo registro al archivo CSV
            csv_path = os.path.abspath('./agenda/agenda/listing-agenda.csv')
            with open(csv_path, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([nombre, telefono])
            # Retorna una respuesta de éxito
            return HttpResponse("Contacto añadido exitosamente")
        else:
            # Retorna una respuesta de error si no se proporcionaron los datos necesarios
            return HttpResponse("Faltan datos del contacto", status=400)
    else:
        # Retorna una respuesta de error si se accede a esta vista con un método diferente a GET
        return HttpResponse("Sólo se permite el método GET", status=405)

#Define una función de vista para buscar un contacto en el archivo CSV
def buscar_contacto(request):
    if request.method == 'GET':
        # Obtiene el nombre del contacto a buscar del cuerpo de la solicitud
        nombre = request.GET.get('nombre')
        # Buscar el contacto en el archivo CSV
        csv_path = os.path.abspath('./agenda/agenda/listing-agenda.csv')
        with open(csv_path, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].lower() == nombre.lower():
                    # Retorna el teléfono del contacto si se encontró
                    return HttpResponse(row[1])

        # Si no se encontró el contacto, retornar None
        return HttpResponse('Contacto no encontrado')
    else:
        # Retorna un error si se accede a esta vista con un método diferente a GET
        return HttpResponse('Método no permitido')


#Define una función de vista para listar los contactos que empiezan por una letra determinada
def listar_letra(request):
    # Verifica que la solicitud se realizó con el método GET
    if request.method == 'GET':
        # Obtiene la letra a buscar del parámetro de la solicitud
        letra = request.GET.get('letra', '').lower()
        # Obtiene la ruta al archivo CSV
        csv_path = os.path.abspath('./agenda/agenda/listing-agenda.csv')
        # Abre el archivo CSV y lee su contenido
        with open(csv_path) as f:
            # Crea un objeto DictReader a partir del contenido del archivo
            reader = csv.DictReader(f)
            # Filtra los datos del archivo para obtener solo los contactos que empiezan con la letra buscada
            data = [row for row in reader if row['nombre'].lower().startswith(letra)]
            # Verifica si se encontraron contactos que empiezan con la letra buscada
            if not data:
                return HttpResponse(f"No se encontraron contactos que empiecen con la letra '{letra}'", status=404)

            # Crea un texto que contiene el nombre y el teléfono de cada contacto encontrado
            text = ""
            for row in data:
                text += f"{row['nombre']}#{row['telefono']}\n"
            # Retorna el texto como respuesta HTTP con el tipo de contenido 'text/plain'
            return HttpResponse(text, content_type="text/plain")

    # Retorna una respuesta de error si se accede a esta vista con un método diferente a GET
    return HttpResponse("Sólo se permite el método GET", status=405)

urlpatterns = [
    path('hi/', say_hello),
    path('listar/', listing),
    path('insertar/', insertar_contacto),
    path('buscar/', buscar_contacto),
    path('listarLetra/', listar_letra)
]