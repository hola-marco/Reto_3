# main.py
import tkinter as tk # Se importa el módulo tkinter para la creación de interfaces gráficas
# Del módulo tkinter se importan componentes específicos:
from tkinter import ttk
# Se importa el módulo messagebox para mostrar mensajes emergentes

from operaciones import InterfazTienda# Se importa la clase InterfazTienda del módulo operaciones

if __name__ == "__main__":# Se verifica si este archivo es el principal
    root = tk.Tk()# Se crea la ventana principal de la aplicación para la interfaz gráfica
    app = InterfazTienda(root)
    root.mainloop() # Se ejecuta el bucle principal de la ventana para mantenerla abierta y mostrar los widgets