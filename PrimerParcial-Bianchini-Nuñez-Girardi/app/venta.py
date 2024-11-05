import tkinter as tk
from tkinter import messagebox
from app.models import realizar_venta  # Asegúrate de tener esta función en models.py

def ventana_venta():
    ventana = tk.Toplevel()
    ventana.title("Realizar Venta")
    ventana.geometry("400x300")

    # Elementos de la ventana de venta
    tk.Label(ventana, text="ID del Libro").pack(pady=5)
    entry_id_libro = tk.Entry(ventana)
    entry_id_libro.pack(pady=5)

    tk.Label(ventana, text="Cantidad").pack(pady=5)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.pack(pady=5)

    # Función para manejar la venta
    def realizar_venta_funcion():
        id_libro = entry_id_libro.get()
        cantidad = entry_cantidad.get()
        if realizar_venta(id_libro, cantidad):
            messagebox.showinfo("Venta", "Venta realizada exitosamente")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Error en la venta. Verifique los datos")

    # Botón para confirmar la venta
    tk.Button(ventana, text="Confirmar Venta", command=realizar_venta_funcion).pack(pady=10)
