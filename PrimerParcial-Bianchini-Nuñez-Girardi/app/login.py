import tkinter as tk
from tkinter import messagebox
import sqlite3
from app.models import obtener_libros
from app import interfaz_empleado, interfaz_gerente

def iniciar_sesion(nombre_usuario, contrasena):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT rol FROM usuario WHERE nombre_usuario=? AND contrasena=?", 
                   (nombre_usuario, contrasena))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def ventana_inicio_sesion():
    ventana_login = tk.Tk()
    ventana_login.title("Inicio de Sesión")

    tk.Label(ventana_login, text="Usuario").pack()
    entry_usuario = tk.Entry(ventana_login)
    entry_usuario.pack()

    tk.Label(ventana_login, text="Contraseña").pack()
    entry_contrasena = tk.Entry(ventana_login, show="*")
    entry_contrasena.pack()

    def on_login():
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()
        rol = iniciar_sesion(usuario, contrasena)
        if rol:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {rol}")
            ventana_login.withdraw()
            if rol == "gerente":
                interfaz_gerente.ventana_gerente()
            else:
                interfaz_empleado.ventana_empleado()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    tk.Button(ventana_login, text="Iniciar Sesión", command=on_login).pack()
    ventana_login.mainloop()
