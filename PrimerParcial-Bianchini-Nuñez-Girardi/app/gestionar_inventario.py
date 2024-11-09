import tkinter as tk
from app.models import nav_gerente, nav_agregar, nav_editar, nav_eliminar

def ventana_gestionar_inventario():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente - Gestionar Inventario")
    ventana.geometry("400x300")

    titulo = tk.Label(ventana, text="GESTIONAR INVENTARIO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Button(marco, text="Agregar Libro", command=lambda: nav_agregar(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)
    tk.Button(marco, text="Eliminar Libro", command=lambda: nav_eliminar(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)
    tk.Button(marco, text="Editar Libro", command=lambda: nav_editar(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Volver", command=lambda: nav_gerente(ventana), width=20, bg="#b32428", fg="white").pack(pady=10)