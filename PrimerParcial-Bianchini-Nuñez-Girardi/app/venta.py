import tkinter as tk
from tkinter import messagebox
from app.models import obtener_libros, realizar_venta_funcion  # Asegúrate de tener estas funciones en models.py

def ventana_venta():
    ventana = tk.Toplevel()
    ventana.title("Realizar Venta")
    ventana.geometry("1100x700")

    # Título en grande en la parte superior
    titulo = tk.Label(ventana, text="VENTA", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Marco para mostrar el inventario
    marco_inventario = tk.Frame(ventana)
    marco_inventario.pack(expand=True, pady=10)

    # Encabezados de la tabla de inventario
    encabezados = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
    for i, encabezado in enumerate(encabezados):
        tk.Label(marco_inventario, text=encabezado, borderwidth=1, relief="solid", width=25, bg="#d3d3d3").grid(row=0, column=i)

    # Mostrar los libros en el inventario
    libros = obtener_libros()
    for fila, libro in enumerate(libros, start=1):
        for col, dato in enumerate(libro):
            tk.Label(marco_inventario, text=dato, borderwidth=1, relief="solid", width=25).grid(row=fila, column=col)

    # Campos de entrada para la venta
    tk.Label(ventana, text="ID del Libro a Vender").pack(pady=5)
    entry_id_libro = tk.Entry(ventana)
    entry_id_libro.pack(pady=5)

    tk.Label(ventana, text="Cantidad a Vender").pack(pady=5)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.pack(pady=5)    

    # Botón para confirmar la venta
    tk.Button(ventana, text="Confirmar Venta", command=lambda: realizar_venta_funcion(ventana, entry_id_libro, entry_cantidad), bg="#0b6730", fg="white").pack(pady=10)

    # Botón para cancelar y cerrar la ventana
    tk.Button(ventana, text="Cancelar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)

# Nota: Asegúrate de que `realizar_venta` en models.py maneje la lógica de actualización de stock y verifique el precio.
