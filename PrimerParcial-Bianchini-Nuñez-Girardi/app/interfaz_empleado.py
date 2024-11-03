import tkinter as tk
from app.models import obtener_libros

def ventana_empleado():
    ventana = tk.Toplevel()
    ventana.title("Panel de Empleado")
    tk.Label(ventana, text="Inventario").pack()

    libros = obtener_libros()
    for libro in libros:
        tk.Label(ventana, text=f"{libro[1]} - {libro[2]} - {libro[3]} - ${libro[4]}").pack()
