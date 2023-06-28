import csv
import shutil
import os

class ElementoFerreteria:
    def __init__(self, codigo, nombre="", cantidad=0, precio=0.0):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Ferreteria:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    # Busca un elemento en el archivo CSV por código y devuelve una instancia de ElementoFerreteria
    def buscar_elemento(self, codigo):
        with open(self.archivo_csv, 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                if row[0] == codigo:
                    return ElementoFerreteria(row[0], row[1], int(row[2]), float(row[3]))
        return None
    
    # Guarda un elemento en el archivo CSV
    def guardar_elemento(self, elemento):
        with open(self.archivo_csv, 'a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([elemento.codigo, elemento.nombre, elemento.cantidad, elemento.precio])

    # Modifica un elemento en el archivo CSV por código
    def modificar_elemento(self, elemento):
        archivo_temp = self.archivo_csv + '.temp'
        with open(self.archivo_csv, 'r', encoding='utf-8') as archivo, open(archivo_temp, 'w', newline='', encoding='utf-8') as archivo_temporal:
            reader = csv.reader(archivo)
            writer = csv.writer(archivo_temporal)
            for row in reader:
                if row[0] == elemento.codigo:
                    writer.writerow([elemento.codigo, elemento.nombre, elemento.cantidad, elemento.precio])
                else:
                    writer.writerow(row)
        os.remove(self.archivo_csv)
        shutil.move(archivo_temp, self.archivo_csv)

    # Elimina un elemento del archivo CSV por código
    def eliminar_elemento(self, codigo):
        archivo_temp = self.archivo_csv + '.temp'
        with open(self.archivo_csv, 'r', encoding='utf-8') as archivo, open(archivo_temp, 'w', newline='', encoding='utf-8') as archivo_temporal:
            reader = csv.reader(archivo)
            writer = csv.writer(archivo_temporal)
            for row in reader:
                if row[0] == codigo:
                    continue
                writer.writerow(row)
        os.remove(self.archivo_csv)
        shutil.move(archivo_temp, self.archivo_csv)
    
     # Lista todos los elementos en el archivo CSV y devuelve una lista de instancias de ElementoFerreteria
    def listar_elementos(self):
        elementos = []
        with open(self.archivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) # saltar linea de encabezados
            for row in reader:
                codigo, nombre, cantidad, precio = row
                elemento = ElementoFerreteria(codigo, nombre, int(cantidad), float(precio))
                elementos.append(elemento)
        return elementos
    
    # Devuelve el siguiente código disponible en el archivo CSV
    def siguiente_codigo(self):
        with open(self.archivo_csv, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) # saltar linea de encabezados
            max_codigo = 0
            for row in reader:
                codigo = int(row[0])
                if codigo > max_codigo:
                    max_codigo = codigo
            return max_codigo + 1