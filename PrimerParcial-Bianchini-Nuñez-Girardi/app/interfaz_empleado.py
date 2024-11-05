import tkinter as tk
from app.inventario import ventana_inventario
from app.venta import ventana_venta

def ventana_empleado():
    ventana = tk.Toplevel()
    ventana.title("Panel de Empleado")
    ventana.geometry("400x300")

    # Marco para centrar los botones
    marco = tk.Frame(ventana)
    marco.pack(expand=True)  # Expande el marco para ocupar el espacio disponible

    # Botón para ver el inventario
    tk.Button(marco, text="Ver Inventario", command=ventana_inventario, width=20, bg="#0b6730", fg="white").pack(pady=10)

    # Botón para realizar una venta
    tk.Button(marco, text="Realizar Venta", command=ventana_venta, width=20, bg="#0b6730", fg="white").pack(pady=10)

    # Botón para cerrar sesión
    tk.Button(marco, text="Cerrar Sesión", command=ventana.destroy, width=20, bg="#b32428", fg="white").pack(pady=10)

# Llamar a la función para mostrar la ventana (puedes hacerlo desde otra parte de tu código)
# ventana_empleado()
