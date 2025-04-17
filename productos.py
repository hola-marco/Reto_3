
class Tienda: # Se define la clase Tienda para gestionar productos
    def __init__(self): # Se inicializa la clase Tienda y se definen los atributos
        self.productos = {}
        self.historial = []

    def cargar_productos_iniciales(self): # Se definen los productos iniciales 
        self.productos = { # Y se cargan en un diccionario para despues ser utilizados
            "P01": {"nombre": "Manzana", "precio": 700, "stock": 300},
            "P02": {"nombre": "Banano", "precio": 200, "stock": 300},
            "P03": {"nombre": "Fresa", "precio": 300, "stock": 100},
            "po4": {"nombre":"Naranja","precio":200,"stock": 500},
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