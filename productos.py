class Tienda: # Se define la clase Tienda para gestionar productos
    def __init__(self): # Se inicializa la clase Tienda y se definen los atributos
        self.productos = {}
        self.historial = []

    def cargar_productos_iniciales(self): # Se definen los productos iniciales 
        self.productos = { # Y se cargan en un diccionario para despues ser utilizados
                          
    "P01": {"nombre": "Manzana", "precio": 700, "stock": 300},
    "P02": {"nombre": "Banano", "precio": 200, "stock": 300},
    "P03": {"nombre": "Fresa", "precio": 300, "stock": 100},
    "P04": {"nombre": "Naranja", "precio": 200, "stock": 500},
    "P05": {"nombre": "Pera", "precio": 600, "stock": 200},
    "P06": {"nombre": "Mango", "precio": 1000, "stock": 150},
    "P07": {"nombre": "Uva", "precio": 1200, "stock": 100},
    "P08": {"nombre": "Piña", "precio": 1800, "stock": 80},
    "P09": {"nombre": "Papaya", "precio": 1500, "stock": 90},
    "P10": {"nombre": "Sandía", "precio": 2500, "stock": 60},
    "P11": {"nombre": "Melón", "precio": 2400, "stock": 50},
    "P12": {"nombre": "Kiwi", "precio": 1300, "stock": 70},
    "P13": {"nombre": "Granadilla", "precio": 900, "stock": 110},
    "P14": {"nombre": "Mandarina", "precio": 400, "stock": 300},
    "P15": {"nombre": "Limón", "precio": 300, "stock": 400},
    "P16": {"nombre": "Aguacate", "precio": 2500, "stock": 85},
    "P17": {"nombre": "Coco", "precio": 2000, "stock": 40},
    "P18": {"nombre": "Maracuyá", "precio": 1100, "stock": 95},
    "P19": {"nombre": "Tamarindo", "precio": 750, "stock": 70},
    "P20": {"nombre": "Cereza", "precio": 1400, "stock": 30},
    "P21": {"nombre": "Guayaba", "precio": 800, "stock": 100},
    "P22": {"nombre": "Ciruela", "precio": 1100, "stock": 60},
    "P23": {"nombre": "Durazno", "precio": 1200, "stock": 90},
    "P24": {"nombre": "Frambuesa", "precio": 1600, "stock": 40},
    "P25": {"nombre": "Mora", "precio": 1000, "stock": 80},
    "P26": {"nombre": "Arándano", "precio": 1900, "stock": 45},
    "P27": {"nombre": "Lulo", "precio": 900, "stock": 100},
    "P28": {"nombre": "Zapote", "precio": 1400, "stock": 60},
    "P29": {"nombre": "Pitahaya", "precio": 2200, "stock": 35},
    "P30": {"nombre": "Mangostino", "precio": 3000, "stock": 25},
    "P31": {"nombre": "Pomelo", "precio": 1300, "stock": 55},
    "P32": {"nombre": "Carambolo", "precio": 1600, "stock": 40},
    "P33": {"nombre": "Chirimoya", "precio": 2000, "stock": 50},
    "P34": {"nombre": "Guanábana", "precio": 2700, "stock": 30},
    "P35": {"nombre": "Feijoa", "precio": 900, "stock": 60}
}
    def agregar_producto(self, idp, nombre, precio, stock): # Se define la función para agregar un producto
        if idp not in self.productos: # Y se verifica si el idp no existe en el diccionario de productos
            self.productos[idp] = {"nombre": nombre, "precio": precio, "stock": stock}
            self.historial.append(f"Agregado: {idp} - {nombre}")
            return True
        return False

    def eliminar_producto(self, idp): # Se define la función para eliminar un producto 
        if idp in self.productos:
            del self.productos[idp]
            self.historial.append(f"Eliminado: {idp}") # Se agrega el idp al historial para saber que se ha eliminado
            return True
        return False

    def modificar_producto(self, idp, nombre, precio, stock): # Se define la función para modificar un producto para cambiar sus datos
        if idp in self.productos:
            self.productos[idp] = {"nombre": nombre, "precio": precio, "stock": stock}
            self.historial.append(f"Modificado: {idp} - {nombre}") # Se agrega el idp al historial para saber que se ha modificado 
            return True
        return False # Se retorna False si el idp no existe en el diccionario de productos para que no se modifique