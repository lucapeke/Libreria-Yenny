import tkinter as tk
from tkinter import messagebox
from app.models import on_login
from app import interfaz_empleado, interfaz_gerente
from app.registro import ventana_registro
from PIL import Image, ImageTk

def ventana_inicio():
    ventana_login = tk.Tk()
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("600x400")
    ventana_login.config(bg="#f0f0f0")

    frame = tk.Frame(ventana_login, bg="#ffffff", padx=20, pady=20)
    frame.pack(expand=True)

    try:
        imagen = Image.open("img/yenny.png")  
        imagen = imagen.resize((400, 150), Image.LANCZOS)
        img = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(frame, image=img, bg="#ffffff")
        label_imagen.image = img  
        label_imagen.pack(pady=10)
    except Exception as e:
        print("Error al cargar la imagen:", e)

    tk.Label(frame, text="Usuario", bg="#ffffff").pack(pady=5)
    entry_usuario = tk.Entry(frame)
    entry_usuario.pack()

    tk.Label(frame, text="Contraseña", bg="#ffffff").pack(pady=5)
    entry_contrasena = tk.Entry(frame, show="*")
    entry_contrasena.pack()

    tk.Button(frame, text="Iniciar Sesión", command=lambda: on_login(ventana_login, interfaz_gerente, interfaz_empleado, entry_usuario, entry_contrasena), bg="#0b6730", fg="white").pack(pady=5)
    tk.Button(frame, text="Registrarse", command=lambda: [ventana_login.withdraw(), ventana_registro(ventana_login)], bg="#2196F3", fg="white").pack(pady=5)

    ventana_login.mainloop()
