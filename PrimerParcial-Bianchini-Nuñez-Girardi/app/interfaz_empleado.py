import tkinter as tk
from app.inventario import ventana_inventario
from app.venta import ventana_venta

def ventana_empleado():
    ventana = tk.Toplevel()
    ventana.title("Panel de Empleado")
    ventana.geometry("400x300")

    titulo = tk.Label(ventana, text="PANEL DE EMPLEADO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Button(marco, text="Ver Inventario", command=ventana_inventario, width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Realizar Venta", command=ventana_venta, width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Cerrar Sesión", command=ventana.destroy, width=20, bg="#b32428", fg="white").pack(pady=10)
