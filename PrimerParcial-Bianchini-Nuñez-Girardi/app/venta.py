import tkinter as tk
from tkinter import messagebox
from app.models import obtener_libros, realizar_venta  # Asegúrate de tener estas funciones en models.py

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

    # Función para manejar la venta
    def realizar_venta_funcion():
        try:
            id_libro = int(entry_id_libro.get())
            cantidad = int(entry_cantidad.get())

            # Llamamos a la función para realizar la venta y verificar el stock
            exito, libro_vendido = realizar_venta(id_libro, cantidad)  # `realizar_venta` debería retornar (bool, detalles libro)

            if exito:
                # Calculamos el costo total
                precio_individual = libro_vendido['precio']
                costo_total = precio_individual * cantidad

                # Mostramos el resumen de la venta
                messagebox.showinfo("Venta Exitosa", f"Venta realizada con éxito\n\n"
                                                     f"Libro: {libro_vendido['titulo']}\n"
                                                     f"Precio por unidad: ${precio_individual:.2f}\n"
                                                     f"Cantidad vendida: {cantidad}\n"
                                                     f"Costo total: ${costo_total:.2f}\n"
                                                     f"Stock restante: {libro_vendido['stock_restante']}")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No hay suficiente stock para realizar la venta.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el ID y la cantidad.")

    # Botón para confirmar la venta
    tk.Button(ventana, text="Confirmar Venta", command=realizar_venta_funcion, bg="#0b6730", fg="white").pack(pady=10)

    # Botón para cancelar y cerrar la ventana
    tk.Button(ventana, text="Cancelar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)

# Nota: Asegúrate de que `realizar_venta` en models.py maneje la lógica de actualización de stock y verifique el precio.
