import tkinter as tk
from tkinter import messagebox
from app.models import obtener_libros, realizar_venta_funcion

def ventana_venta():
    ventana = tk.Toplevel()
    ventana.title("Realizar Venta")
    ventana.geometry("1100x700")

    titulo = tk.Label(ventana, text="VENTA", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco_inventario = tk.Frame(ventana)
    marco_inventario.pack(expand=True, pady=10)

    encabezados = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
    for i, encabezado in enumerate(encabezados):
        tk.Label(marco_inventario, text=encabezado, borderwidth=1, relief="solid", width=25, bg="#d3d3d3").grid(row=0, column=i)

    libros = obtener_libros()
    for fila, libro in enumerate(libros, start=1):
        for col, dato in enumerate(libro):
            tk.Label(marco_inventario, text=dato, borderwidth=1, relief="solid", width=25).grid(row=fila, column=col)

    tk.Label(ventana, text="ID del Libro a Vender").pack(pady=5)
    entry_id_libro = tk.Entry(ventana)
    entry_id_libro.pack(pady=5)

    tk.Label(ventana, text="Cantidad a Vender").pack(pady=5)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.pack(pady=5)    

    tk.Button(ventana, text="Confirmar Venta", command=lambda: realizar_venta_funcion(ventana, entry_id_libro, entry_cantidad), bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)
