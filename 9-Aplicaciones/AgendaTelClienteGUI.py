import tkinter as tk
import tkinter.messagebox as messagebox
import requests

class ContactClientGUI:

    def __init__(self, master):
        self.master = master
        master.title("Agemga online")

        self.label = tk.Label(master, text="Buscar un contacto:")
        self.label.pack()

        self.search_frame = tk.Frame(master)
        self.search_frame.pack()

        self.search_name_label = tk.Label(self.search_frame, text="Nombre:")
        self.search_name_label.pack(side=tk.LEFT)

        self.search_name_entry = tk.Entry(self.search_frame)
        self.search_name_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.search_frame, text="Buscar", command=self.search_contact)
        self.search_button.pack(side=tk.LEFT)

        self.insert_label = tk.Label(master, text="Insertar un contacto:")
        self.insert_label.pack()

        self.insert_frame = tk.Frame(master)
        self.insert_frame.pack()

        self.insert_name_label = tk.Label(self.insert_frame, text="Nombre:")
        self.insert_name_label.pack(side=tk.LEFT)

        self.insert_name_entry = tk.Entry(self.insert_frame)
        self.insert_name_entry.pack(side=tk.LEFT)

        self.insert_phone_label = tk.Label(self.insert_frame, text="Teléfono:")
        self.insert_phone_label.pack(side=tk.LEFT)

        self.insert_phone_entry = tk.Entry(self.insert_frame)
        self.insert_phone_entry.pack(side=tk.LEFT)

        self.insert_button = tk.Button(self.insert_frame, text="Insertar", command=self.insert_contact)
        self.insert_button.pack(side=tk.LEFT)

        self.list_frame = tk.Frame(master)
        self.list_frame.pack()

        self.list_scrollbar = tk.Scrollbar(self.list_frame)
        self.list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_text = tk.Text(self.list_frame, yscrollcommand=self.list_scrollbar.set)
        self.list_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.list_scrollbar.config(command=self.list_text.yview)

        self.list_letter_frame = tk.Frame(master)
        self.list_letter_frame.pack()

        self.list_label = tk.Label(self.list_letter_frame, text="Listar contactos:")
        self.list_label.pack()

        self.list_all_button = tk.Button(self.list_letter_frame, text="Listar todos", command=self.list_contacts)
        self.list_all_button.pack(side=tk.LEFT)

        self.list_letter_label = tk.Label(self.list_letter_frame, text="Listar por letra:")
        self.list_letter_label.pack(side=tk.LEFT)

        self.list_letter_entry = tk.Entry(self.list_letter_frame)
        self.list_letter_entry.pack(side=tk.LEFT)

        self.list_letter_button = tk.Button(self.list_letter_frame, text="Listar", command=self.list_contacts_by_letter)
        self.list_letter_button.pack(side=tk.LEFT)

    def search_contact(self):
        # Método que se ejecuta al presionar el botón "Buscar". Obtiene el nombre del contacto
        # a buscar, lo envía al servidor y muestra el resultado en el campo de texto.
        nombre = self.search_name_entry.get()
        if not nombre:
            messagebox.showerror("Error", "Introduce el nombre del contacto a buscar")
            return

        url = "https://luin.pythonanywhere.com/buscar/"
        params = {"nombre": nombre}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            telefono = response.text
            self.list_text.delete(1.0, tk.END)
            self.list_text.insert(tk.END, f"{nombre} {telefono}")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor")
 
    def insert_contact(self):
        #Método para insertar un nuevo contacto en el servidor
        nombre = self.insert_name_entry.get()
        telefono = self.insert_phone_entry.get()
        if not nombre or not telefono:
            messagebox.showerror("Error", "Introduce el nombre y el teléfono del contacto a insertar")
            return

        url = "https://luin.pythonanywhere.com/insertar/"
        params = {"nombre": nombre, "telefono": telefono}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            messagebox.showinfo("Insertado correctamente", f"Contacto {nombre} {telefono}")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor")

    def list_contacts(self):
        #Método para listar todos los contactos del servidor
        #Realiza una petición GET al servidor remoto con la ruta /listar/
        url = "https://luin.pythonanywhere.com/listar/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            contacts = response.content.decode('utf-8')
            self.list_text.delete(1.0, tk.END)
            self.list_text.insert(tk.END, contacts)
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor")

    def list_contacts_by_letter(self):
        # Método para listar los contactos que empiezan por una letra determinada
        letter = self.list_letter_entry.get()
        if not letter:
            messagebox.showerror("Error", "Introduce una letra para listar los contactos")
            return

        url = "https://luin.pythonanywhere.com/listarLetra/"
        params = {"letra": letter}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            contacts = response.content.decode('utf-8')
            self.list_text.delete(1.0, tk.END)
            self.list_text.insert(tk.END, contacts)
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor")

if __name__ == '__main__': 
    ventana = tk.Tk()
    contact_client_gui = ContactClientGUI(ventana)
    ventana.mainloop()