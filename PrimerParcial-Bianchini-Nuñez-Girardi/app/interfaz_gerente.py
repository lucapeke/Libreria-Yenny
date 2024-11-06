import tkinter as tk
from app.inventario import ventana_inventario
from app.venta import ventana_venta
from app.gestionar_inventario import ventana_gestionar_inventario
from app.gestionar_usuarios import ventana_gestionar_usuarios

def ventana_gerente():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente")
    ventana.geometry("400x400")

    titulo = tk.Label(ventana, text="PANEL DE GERENTE", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Button(marco, text="Ver Inventario", command=ventana_inventario, width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Gestionar Inventario", command=lambda: boton_gestionar_inventario(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Realizar Venta", command=ventana_venta, width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Gestionar Usuarios", command=lambda: boton_gestionar_usuarios(ventana), width=20, bg="#0b6730", fg="white").pack(pady=10)

    tk.Button(marco, text="Cerrar Sesión", command=ventana.destroy, width=20, bg="#b32428", fg="white").pack(pady=10)

def boton_gestionar_usuarios(ventana):
    from app.gestionar_usuarios import ventana_gestionar_usuarios 
    ventana.destroy()
    ventana_gestionar_usuarios()

def boton_gestionar_inventario(ventana):
    from app.gestionar_inventario import ventana_gestionar_inventario  
    ventana.destroy()
    ventana_gestionar_inventario()
