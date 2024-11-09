import tkinter as tk
from app.models import nav_gerente

def ventana_gestionar_usuarios():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente - Gestionar Usuarios")
    ventana.geometry("400x300")

    titulo = tk.Label(ventana, text="GESTIONAR USUARIOS", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Label(marco, text="Función en desarrollo").pack()
    tk.Button(marco, text="Volver", command=lambda: nav_gerente(ventana), width=20, bg="#b32428", fg="white").pack(pady=10)


