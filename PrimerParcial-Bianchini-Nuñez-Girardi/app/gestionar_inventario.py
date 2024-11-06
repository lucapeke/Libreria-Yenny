import tkinter as tk
from app.agregar import ventana_agregar_libro
from app.eliminar import ventana_eliminar_libro
from app.editar import ventana_editar_libro

def ventana_gestionar_inventario():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente - Gestionar Inventario")
    ventana.geometry("400x300")

    titulo = tk.Label(ventana, text="GESTIONAR INVENTARIO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Button(marco, text="Agregar Libro", command=ventana_agregar_libro, width=20, bg="#0b6730", fg="white").pack(pady=10)
    tk.Button(marco, text="Eliminar Libro", command=ventana_eliminar_libro, width=20, bg="#0b6730", fg="white").pack(pady=10)
    tk.Button(marco, text="Editar Libro", command=ventana_editar_libro, width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Volver", command=lambda: volver_a_gerente(ventana), width=20, bg="#b32428", fg="white").pack(pady=10)

def volver_a_gerente(ventana):
    from app.interfaz_gerente import ventana_gerente
    ventana.destroy()
    ventana_gerente()
