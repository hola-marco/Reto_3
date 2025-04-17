# Se importa el módulo tkinter para la creación de interfaces gráficas
import tkinter as tk
# Del módulo tkinter se importan componentes específicos:

from tkinter import messagebox, simpledialog, ttk # Se importa messagebox para mostrar mensajes emergentes
# & Se define una función para mostrar un cuadro de entrada


def mostrar_error(mensaje):# Se define esta función para mostrar un cuadro de error
    messagebox.showerror("Error", mensaje)

def mostrar_info(mensaje):# Se define esta función para mostrar un cuadro de información y mostrar un mensaje
    messagebox.showinfo("Información", mensaje)

def mostrar_advertencia(mensaje):# Se define esta función para mostrar un cuadro de advertencia    
    messagebox.showwarning("Advertencia", mensaje) #
