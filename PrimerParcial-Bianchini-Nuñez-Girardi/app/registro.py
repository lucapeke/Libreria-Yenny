import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from app.models import on_register

def ventana_registro(ventana_login):
    ventana = tk.Toplevel()
    ventana.title("Registro de Usuario")
    ventana.geometry("600x500")

    try:
        imagen = Image.open("img/yenny.png")  
        imagen = imagen.resize((400, 150), Image.LANCZOS)
        img = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(ventana, image=img)
        label_imagen.image = img
        label_imagen.pack(pady=10)
    except Exception as e:
        print("Error al cargar la imagen:", e)
    
    def volver_a_inicio():
        ventana.destroy()
        ventana_login.deiconify()  

    tk.Label(ventana, text="Usuario").pack()
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack()

    tk.Label(ventana, text="Contraseña").pack()
    entry_contrasena = tk.Entry(ventana, show="*")
    entry_contrasena.pack()

    tk.Label(ventana, text="Nombre").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Apellido").pack()
    entry_apellido = tk.Entry(ventana)
    entry_apellido.pack()

    tk.Label(ventana, text="DNI").pack()
    entry_dni = tk.Entry(ventana)
    entry_dni.pack()

    entry_rol="empleado"

    tk.Button(ventana, text="Registrarse", command=lambda: on_register(ventana, ventana_login, entry_usuario, entry_contrasena, entry_rol, entry_nombre, entry_apellido, entry_dni), bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(ventana, text="Volver", command=volver_a_inicio, bg="#b32428", fg="white").pack(pady=5)
