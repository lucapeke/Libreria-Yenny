import tkinter as tk

def ventana_gestionar_usuarios():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente - Gestionar Usuarios")
    ventana.geometry("400x300")

    # Título en grande en la parte superior
    titulo = tk.Label(ventana, text="GESTIONAR USUARIOS", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Label(marco, text="Función en desarrollo").pack()
    tk.Button(marco, text="Volver", command=lambda: volver_a_gerente(ventana), width=20, bg="#b32428", fg="white").pack(pady=10)

def volver_a_gerente(ventana):
    from app.interfaz_gerente import ventana_gerente  # Importación dentro de la función
    ventana.destroy()
    ventana_gerente()
