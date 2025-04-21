# 🛒 Sistema de Caja Registradora para Fruber 🍎🥦

## 📝 Descripción
Este proyecto es un sistema de caja registradora desarrollado en Python para la tienda "Fruber", especializada en la venta de frutas y verduras. La aplicación permite gestionar ventas de manera eficiente, incluyendo la selección de productos, cálculo de totales, actualización de stock y registro del historial de ventas. La interfaz gráfica está construida con Tkinter, garantizando una experiencia de usuario intuitiva. 🚀

## ✨ Características Principales
- **🖥️ Interfaz Gráfica Amigable**:
  - 📋 Lista de productos con nombre, precio y cantidad disponible.
  - 🔢 Campo para seleccionar la cantidad deseada.
  - 🛍️ Botones para agregar productos al carrito, finalizar compra y ver historial de ventas.
  - 💰 Visualización del total acumulado en tiempo real.

- **📦 Gestión de Productos**:
  - ✔️ Validación de stock disponible al agregar productos al carrito.
  - 🔄 Actualización automática del stock después de cada compra.

- **✅ Finalización de Compra**:
  - 📄 Generación de un resumen de compra al finalizar.
  - 📊 Registro automático de la venta en el historial.
  - 🧹 Limpieza del carrito después de cada transacción.

- **📊 Historial de Ventas**:
  - 📜 Tabla que muestra el nombre del producto, cantidad vendida y precio total por venta.
  - 💵 Cálculo y visualización de la ganancia total acumulada.

- **⚠️ Manejo de Excepciones**:
  - 🚫 Validación de entradas (evitar valores no numéricos o cantidades inválidas).
  - 🛡️ Control de errores para evitar cierres inesperados.
  - ❗ Mensajes claros en caso de operaciones incorrectas.

## ⚙️ Requisitos del Sistema
- **🐍 Python 3.x** (versión recomendada: 3.8 o superior).
- **📚 Bibliotecas**:
  - `tkinter` (para la interfaz gráfica).
  - `ttk` (Themed Tkinter Widgets) para mejorar la apariencia.

## 📂 Estructura del Proyecto
El código está organizado en los siguientes archivos:
- `main.py` 🏠: Archivo principal que ejecuta la interfaz gráfica.
- `productos.py` �: Contiene la lista de productos disponibles y sus atributos (nombre, precio, stock).
- `operaciones.py` ⚙️: Implementa funciones auxiliares como agregar productos al carrito y calcular el total.
- `excepciones.py` 🚨: Módulo dedicado al manejo de errores y excepciones.

