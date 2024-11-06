
import tkinter as tk
from tkinter import messagebox
from app.models import confirmar_agregar

def ventana_agregar_libro():
    ventana = tk.Toplevel()
    ventana.title("Agregar Libro")
    ventana.geometry("300x400")
    
    titulo = tk.Label(ventana, text="AGREGAR", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    tk.Label(frame, text="Título").pack(pady=5)
    titulo = tk.Entry(frame)
    titulo.pack()

    tk.Label(frame, text="Autor").pack(pady=5)
    autor = tk.Entry(frame)
    autor.pack()

    tk.Label(frame, text="Género").pack(pady=5)
    genero = tk.Entry(frame)
    genero.pack()

    tk.Label(frame, text="Precio").pack(pady=5)
    precio = tk.Entry(frame)
    precio.pack()

    tk.Label(frame, text="Stock").pack(pady=5)
    stock = tk.Entry(frame)
    stock.pack()


    tk.Button(frame, text="Agregar", command=lambda: confirmar_agregar(ventana, titulo, autor, genero, precio, stock), bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(frame, text="Cerrar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)
