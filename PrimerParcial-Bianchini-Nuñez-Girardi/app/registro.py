import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

def registrar_usuario(nombre_usuario, contrasena, rol, nombre, apellido, dni):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuario (nombre_usuario, contrasena, rol, nombre, apellido, dni) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre_usuario, contrasena, rol, nombre, apellido, dni))
        conn.commit()
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El usuario ya existe")
    conn.close()

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

    tk.Label(ventana, text="Rol (empleado o gerente)").pack()
    entry_rol = tk.Entry(ventana)
    entry_rol.pack()

    tk.Label(ventana, text="Nombre").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Apellido").pack()
    entry_apellido = tk.Entry(ventana)
    entry_apellido.pack()

    tk.Label(ventana, text="DNI").pack()
    entry_dni = tk.Entry(ventana)
    entry_dni.pack()

    def on_register():
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()
        rol = entry_rol.get().lower()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        dni = entry_dni.get()

        if len(contrasena) >= 6 and any(c.isupper() for c in contrasena):
            registrar_usuario(usuario, contrasena, rol, nombre, apellido, dni)
            ventana.destroy()
            ventana_login.deiconify()  
        else:
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres y una letra mayúscula.")

    tk.Button(ventana, text="Registrarse", command=on_register, bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(ventana, text="Volver", command=volver_a_inicio, bg="#b32428", fg="white").pack(pady=5)

