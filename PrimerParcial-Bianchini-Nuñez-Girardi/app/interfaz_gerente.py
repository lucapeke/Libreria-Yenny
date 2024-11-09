import tkinter as tk
from app.venta import ventana_venta
from app.models import nav_gestionar_inventario, nav_gestionar_usuarios, nav_inventario, nav_venta

def ventana_gerente():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente")
    ventana.geometry("400x400")

    titulo = tk.Label(ventana, text="PANEL DE GERENTE", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Button(marco, text="Ver Inventario", command=lambda: nav_inventario(ventana, ventana_gerente), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Gestionar Inventario", command=lambda: nav_gestionar_inventario(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Realizar Venta", command=lambda: nav_venta(ventana, ventana_gerente), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Gestionar Usuarios", command=lambda: nav_gestionar_usuarios(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Cerrar Sesión", command=ventana.destroy, width=20, bg="#b32428", fg="white").pack(pady=10)
