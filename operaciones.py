import tkinter as tk # Esta línea importa el módulo tkinter para la creación de interfaces gráficas
from tkinter import messagebox, simpledialog, ttk # Sirve para importar componentes específicos de tkinter
from PIL import Image, ImageTk# Se importa la biblioteca PIL para trabajar con imágenes 
from excepciones import mostrar_info,mostrar_error,mostrar_advertencia # Esta línea importa el módulo excepciones y sus funciones
from productos import Tienda # Se importa la clase Tienda del módulo productos para gestionar la tienda
class InterfazTienda: # Esta clase representa la interfaz gráfica de la tienda
    def __init__(self, root): # Se define el constructor de la clase, para inicializar la ventana principal        self.root = root
        self.root.title("Menú Principal - Tienda")
        self.root.geometry("800x700")
        self.fondo_img = ImageTk.PhotoImage(Image.open("python-supermarket.jpg").resize((800, 700))) # Se carga la imagen de fondo para una mejor apariencia
        self.canvas = None
        self.tienda = Tienda()
        self.tienda.cargar_productos_iniciales()
        self.usuario_es_admin = False
        self.carrito = []
        self.menu_inicio() # Se llama al método menu_inicio para mostrar el menú principal al iniciar la aplicación

    
    def limpiar_ventana(self, mostrar_fondo=True):# Se define el método limpiar_ventana para tener una mejor visualizacion
       for widget in self.root.winfo_children(): 
         widget.destroy()
       self.canvas = tk.Canvas(self.root, width=650, height=700) # Esta linea se encarga de crear un canvas para la ventana
       self.canvas.pack(fill="both", expand=True)
       if mostrar_fondo:
          self.fondo_id = self.canvas.create_image(0, 0, image=self.fondo_img, anchor="nw")  # Se crea una imagen de fondo en el canvas

    def menu_inicio(self):# Aca se muestra el menu principal para despues de iniciar la aplicacion
        self.limpiar_ventana()
        btn_client = tk.Button(self.root, text="🧑‍💻🍍 FrutaStack – Alimenta tu RAM con Vitaminas 🍇⚙️", width=50,) 
        btn_cliente = tk.Button(self.root, text="Cliente", width=20, command=self.ventana_cliente)
        btn_admin = tk.Button(self.root, text="Administrador", width=20, command=self.ventana_admin_login) 
        self.canvas.create_window(325, 600, window=btn_cliente) # Se crea un botón para el cliente para que pueda acceder a la tienda
        
        self.canvas.create_window(325, 560, window=btn_admin) # Se crea un botón para el acceso de admin para gestionar la tienda
        self.canvas.create_window(325, 100, window=btn_client)# Aqui se crea un botón para el cliente para que pueda acceder a la tienda
        

    def ventana_cliente(self):# Aca lo que se hace es mostrar la ventana del cliente
        if hasattr(self, "fondo_id"):
         self.canvas.delete(self.fondo_id)# Se elimina el fondo de la ventana

        
        self.usuario_es_admin = False
        self.carrito = []
        self.ventana_cliente_compra()

    def ventana_cliente_compra(self): # Aca lo que se hace es mostrar la ventana del cliente
        self.limpiar_ventana(mostrar_fondo=False)
        
    # 👉 Frame que contiene la imagen + texto
        titulo_frame = tk.Frame(self.root, bg="white")
        self.canvas.create_window(325, 30, window=titulo_frame)# Se crea un frame para la imagen

    # 👉 Cargar la imagen
        img = Image.open("supermarket.jpg").resize((200, 120))
        img_tk = ImageTk.PhotoImage(img)
        self.icono_producto = img_tk  # Guardar la imagen en la clase y no perder la referencia

        img_label = tk.Label(titulo_frame, image=img_tk, bg="white") # Se crea un label para la imagen
        img_label.pack(side="left", padx=(0, 10)) # Se coloca la imagen a la izquierda del frame
        # Se le da un padding a la imagen para que no quede pegada al texto

    # 👉 Texto al lado derecho
        texto_label = tk.Label(titulo_frame, text="Productos disponibles", font=("Arial", 14, "bold"), bg="white") # Se crea un label para el texto y asi mismo se le da la fuente
        texto_label.pack(side="left") # Se coloca el texto a la derecha del frame para que quede alineado con la imagen

    # 👉 Frame para los productos debajo
        frame = tk.Frame(self.root) 
        self.canvas.create_window(325, 180, window=frame) # Se crea un frame para los productos
    
        self.canvas.create_text(325, 30, text="Productos disponibles", font=("Arial", 14, "bold"), fill="black") 
        
        frame = tk.Frame(self.root)
        self.canvas.create_window(325, 180, window=frame)

        columnas = ("ID", "Nombre", "Precio unidad ", "Stock") # Se definen las columnas de la tabla de productos 
        self.tree_productos = ttk.Treeview(frame, columns=columnas, show="headings", height=7) # Se crea un Treeview para mostrar los productos
        for col in columnas:
            self.tree_productos.heading(col, text=col)
            self.tree_productos.column(col, anchor="center") # Se le da un ancho a las columnas para que queden alineadas
        self.tree_productos.pack()
        self.actualizar_tabla_productos()# Se actualiza la tabla de productos

        btn_agregar = tk.Button(self.root, text="Agregar al carrito", command=self.agregar_al_carrito) # Esta linea crea un botón para agregar productos al carrito
        self.canvas.create_window(325, 340, window=btn_agregar) # con esta linea se crea el botón en la ventana

        self.canvas.create_text(325, 370, text="🧺 Carrito de Compras", font=("Arial", 12, "bold"), fill="black")

        frame_carrito = tk.Frame(self.root) # 
        self.canvas.create_window(325, 470, window=frame_carrito) # Aqui se crea un frame para el carrito de compras

        carrito_cols = ("Nombre", "Precio", "Cantidad", "Subtotal") # Se definen las columnas de la tabla del carrito de compras
        self.tree_carrito = ttk.Treeview(frame_carrito, columns=carrito_cols, show="headings", height=5) # Se crea un Treeview para mostrar el carrito de compras
        for col in carrito_cols:
            self.tree_carrito.heading(col, text=col)# Se le da un nombre a las columnas 
            self.tree_carrito.column(col, anchor="center") 
        self.tree_carrito.pack() # Se empaqueta el Treeview para que se muestre en la ventana

        self.label_total = tk.Label(self.root, text="Total: $0.00", font=("Arial", 12, "bold"), bg="lightgray")# Se crea un label para mostrar el total de la compra 
        self.canvas.create_window(325, 540, window=self.label_total) # aqui se crea el label en la ventana para mostrar el total

        btn_factura = tk.Button(self.root, text="Ver factura", command=self.mostrar_factura) # En esta linea se crea un botón para ver la factura
        btn_volver = tk.Button(self.root, text="Regresar al menú principal", command=self.menu_inicio) # Luego se crea un botón para regresar al menú principal
        self.canvas.create_window(325, 580, window=btn_factura)
        self.canvas.create_window(325, 620, window=btn_volver) 

    def actualizar_tabla_productos(self): # Se define el método para actualizar la tabla de productos y mostrar los productos disponibles
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        for pid, datos in self.tienda.productos.items():# Se itera sobre los productos de la tienda
            self.tree_productos.insert("", tk.END, values=(pid, datos['nombre'], f"${datos['precio']}", datos['stock'])) # En esta linea se insertan los productos en la tabla para que se muestren en la ventana

    def actualizar_tabla_carrito(self):# Se define el método para actualizar la tabla del carrito de compras para que se muestre el total
        for item in self.tree_carrito.get_children():
            self.tree_carrito.delete(item)
        total = 0
        for item in self.carrito: # Aca se itera sobre los productos del carrito de compras 
            subtotal = item['cantidad'] * item['precio']
            self.tree_carrito.insert("", tk.END, values=(item['producto'], f"${item['precio']:.2f}", item['cantidad'], f"${subtotal:.2f}"))  # Se insertan los productos en la tabla del carrito
            total += subtotal
        self.label_total.config(text=f"Total: ${total:.2f}") #En esta linea se muestra el total de la compra para que el cliente lo vea

    def agregar_al_carrito(self):# Se define el método para agregar productos al carrito de compras 
        try:
            seleccion = self.tree_productos.selection() # Se obtiene la selección del Treeview de productos
            if not seleccion:
                mostrar_advertencia("Selecciona un producto") # Si no se selecciona un producto, se muestra un mensaje de advertencia
                return
            valores = self.tree_productos.item(seleccion[0], "values")
            idp = valores[0]
            producto = self.tienda.productos.get(idp)
            cantidad = simpledialog.askinteger("Cantidad", f"Ingrese la cantidad de {producto['nombre']}:") # Con askinteger se le pide al cliente la cantidad de productos que quiere comprar
            if cantidad and cantidad > 0:
                if cantidad <= producto["stock"]:
                    self.carrito.append({"producto": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad}) # Se agrega el producto al carrito
                    producto["stock"] -= cantidad
                    mostrar_info(f"Agregado {producto['nombre']} al carrito")
                    self.actualizar_tabla_productos()
                    self.actualizar_tabla_carrito() # Se actualiza la tabla del carrito
                else:
                    mostrar_error("Stock insuficiente") # Si no hay suficiente stock, se muestra un mensaje de error
            else:
                mostrar_advertencia("Cantidad inválida") # Si la cantidad es inválida, se muestra un mensaje de advertencia 
        except Exception as e:
            mostrar_error(f"Error al agregar al carrito: {e}") # Si hay un error al agregar al carrito, se muestra un mensaje de error

    def mostrar_factura(self): # Se define el método para mostrar la factura de compra
        if not self.carrito:
            mostrar_advertencia("El carrito está vacío") # Si el carrito de compras está vacío, se muestra un mensaje de advertencia
            return
        factura_ventana = tk.Toplevel(self.root)
        factura_ventana.title("Factura")
        factura_ventana.geometry("400x400") # Se define el tamaño de la ventana de la factura
        tk.Label(factura_ventana, text="Factura de Compra", font=("Courier", 14, "bold")).pack(pady=10) # Se crea un label para mostrar el título de la factura
        frame = tk.Frame(factura_ventana) 
        frame.pack(pady=10) # Se crea un frame para mostrar los productos de la factura
        total = 0
        for item in self.carrito:
            linea = f"{item['cantidad']} x {item['producto']:<12} ${item['precio']:.2f} = ${item['cantidad'] * item['precio']:.2f}"# Se define la linea de la factura para mostrar los productos
            tk.Label(frame, text=linea, font=("Courier", 10)).pack(anchor="w") # En esta linea se muestra la linea de la factura para que el cliente la vea
            total += item['cantidad'] * item['precio']
        tk.Label(factura_ventana, text=f"\nTotal a pagar: ${total:.2f}", font=("Courier", 12, "bold")).pack() # Se muestra el total a pagar en la factura
        tk.Button(factura_ventana, text="Volver al menú principal", command=lambda: [factura_ventana.destroy(), self.menu_inicio()]).pack(pady=20) # Se crea un botón para volver al menú principal

    def ventana_admin_login(self):# Aca se define el método para mostrar la ventana de inicio de sesión del administrador
        self.limpiar_ventana(mostrar_fondo=False)
        
        self.canvas.create_text(325, 100, text="Inicio de Sesión", font=("Arial", 14, "bold"), fill="black")
        self.user_entry = tk.Entry(self.root)
        self.pass_entry = tk.Entry(self.root, show="*")
        self.canvas.create_window(325, 160, window=self.user_entry)
        self.canvas.create_window(325, 200, window=self.pass_entry)
        self.canvas.create_text(325, 145, text="Usuario:", fill="black")
        self.canvas.create_text(325, 185, text="Contraseña:", fill="black")
        login_btn = tk.Button(self.root, text="Ingresar", command=self.verificar_login_admin) # Se crea un botón para iniciar sesión 
        self.canvas.create_window(325, 240, window=login_btn)

    def verificar_login_admin(self): # Se define el método para verificar las credenciales del administrador 
        usuario = self.user_entry.get()
        password = self.pass_entry.get()
        if usuario == "admin" and password == "1234": # Se verifica si el usuario y la contraseña son correctos
            self.usuario_es_admin = True
            self.ventana_admin() # Se llama al método ventana_admin para mostrar la ventana de administración
        else:
            mostrar_error("Credenciales incorrectas") # Si las credenciales son incorrectas, se muestra un mensaje de error

    def ventana_admin(self): # Se define el método para mostrar la ventana de administración
        self.limpiar_ventana()
        self.canvas.create_text(325, 30, text="Gestión de Productos", font=("Arial", 14, "bold"), fill="white") # Se crea un label para mostrar el título de la ventana
        frame = tk.Frame(self.root)
        self.canvas.create_window(325, 240, window=frame)# Se crea un frame para mostrar los productos

        columnas = ("ID", "Nombre", "Precio", "Stock")
        self.tree = ttk.Treeview(frame, columns=columnas, show="headings", height=7) # Se crea un treeview para mostrar los productos y sus datos en la ventana
        for col in columnas:
            self.tree.heading(col, text=col) # Se define el texto de las columnas
            self.tree.column(col, anchor="center") # Se define el alineamiento de las columnas
        self.tree.pack()
        self.actualizar_tabla_productos_admin() # aca se llama al metodo actualizar_tabla_productos_admin para mostrar los productos

        botones = [ # En estas lineas se crean los botones para la ventana de administración y se les asigna una función a cada uno
            ("Agregar", self.agregar_producto),
            ("Modificar", self.modificar_producto),
            ("Eliminar", self.eliminar_producto),
            ("Ver Historial", self.ver_historial),
            ("Volver", self.menu_inicio)
        ]
        for i, (texto, comando) in enumerate(botones): # Se itera sobre la lista de botones
            btn = tk.Button(self.root, text=texto, command=comando)
            self.canvas.create_window(325, 420 + i*40, window=btn) # Se crea un botón para cada acción en la ventana de administración

    def actualizar_tabla_productos_admin(self):# Para
        for item in self.tree.get_children():# Se define el método para actualizar la tabla de productos en la ventana de administración
            self.tree.delete(item)
        for pid, datos in self.tienda.productos.items():
            self.tree.insert("", tk.END, values=(pid, datos['nombre'], f"${datos['precio']}", datos['stock'])) # Aca se insertan los productos en la tabla como se muestra en la ventana

    def agregar_producto(self):# Se define el método para agregar un producto a la tienda para que el administrador y lo pueda gestionar
        try:
            idp = simpledialog.askstring("Agregar", "ID:")
            nombre = simpledialog.askstring("Agregar", "Nombre:")
            precio = float(simpledialog.askstring("Agregar", "Precio:")) # float se utiliza para convertir una cadena de texto en un número decimal
            stock = int(simpledialog.askstring("Agregar", "Stock:"))
            if self.tienda.agregar_producto(idp, nombre, precio, stock):
                self.actualizar_tabla_productos_admin()
                mostrar_info("Producto agregado") # Se muestra un mensaje de información al agregar el producto
            else:
                mostrar_error("ID ya registrado")
        except Exception:
            mostrar_error("Datos inválidos") # Si hay un error al agregar el producto, se muestra un mensaje de error

    def eliminar_producto(self): # Se define el método para eliminar un producto de la tienda
        seleccion = self.tree.selection()
        if not seleccion:
            return
        valores = self.tree.item(seleccion[0], "values")
        idp = valores[0]
        if self.tienda.eliminar_producto(idp):
            self.actualizar_tabla_productos_admin()
            mostrar_info(f"Producto {idp} eliminado") # Se muestra un mensaje de información al eliminar el producto

    def modificar_producto(self): # Se define el método para modificar un producto de la tienda
        seleccion = self.tree.selection()
        if not seleccion:
            return
        valores = self.tree.item(seleccion[0], "values")
        idp = valores[0]
        try:
            nombre = simpledialog.askstring("Modificar", "Nuevo nombre:")
            precio = float(simpledialog.askstring("Modificar", "Nuevo precio:"))
            stock = int(simpledialog.askstring("Modificar", "Nuevo stock:"))
            if self.tienda.modificar_producto(idp, nombre, precio, stock):# Se llama al metodo modificar_producto para modificar el producto
                self.actualizar_tabla_productos_admin()# Se llama al metodo actualizar_tabla_productos_admin para actualizar la tabla
                mostrar_info("Producto modificado") # Se muestra un mensaje de información al modificar el producto
        except Exception:
            mostrar_error("Datos inválidos")

    def ver_historial(self): # Se define el método para ver el historial de acciones
        historial = "\n".join(self.tienda.historial)# Se obtiene el historial de acciones de la tienda
        messagebox.showinfo("Historial de acciones", historial) # & Se muestra el historial de acciones en un cuadro de mensaje