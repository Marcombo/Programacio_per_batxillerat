import tkinter as tk

class SecondaryWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Ventana Secundaria")
        self.transient(parent)
        self.grab_set()
        
        self.name_label = tk.Label(self, text="Nombre:")
        self.name_label.pack(side="left", padx=(5, 0), pady=5)
        
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(side="left", padx=(0, 5), pady=5)
        
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok_button_click)
        self.ok_button.pack(side="right", padx=5, pady=5)
        
        self.parent = parent
    
    def on_ok_button_click(self):
        name = self.name_entry.get()
        self.parent.update_name(name)
        self.destroy()

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Ventana Principal")
        
        self.name_label = tk.Label(self, text="Nombre:")
        self.name_label.pack(padx=5, pady=5)
        
        self.name_var = tk.StringVar()
        self.name_var.set("N/A")
        
        self.name_display_label = tk.Label(self, textvariable=self.name_var)
        self.name_display_label.pack(padx=5, pady=5)
        
        self.change_name_button = tk.Button(self, text="Cambiar Nombre", command=self.on_change_name_button_click)
        self.change_name_button.pack(padx=5, pady=5)
        
        self.secondary_window = None
    
    def on_change_name_button_click(self):
        if self.secondary_window is None:
            self.secondary_window = SecondaryWindow(self)
        else:
            self.secondary_window.lift()
    
    def update_name(self, name):
        self.name_var.set(name)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
