# ventana_agregar.py

import tkinter as tk
from tkinter import messagebox
from app.models import agregar_libro

def ventana_agregar_libro():
    ventana = tk.Toplevel()
    ventana.title("Agregar Libro")
    ventana.geometry("300x400")
    
    # Título en grande en la parte superior
    titulo = tk.Label(ventana, text="AGREGAR", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Crear un frame para centrar el contenido
    frame = tk.Frame(ventana)
    frame.pack(expand=True)  # Expandir el frame para centrar el contenido verticalmente

    # Campos de entrada
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

    # Función para confirmar la acción de agregar libro
    def confirmar_agregar():
        try:
            # Intentar convertir Precio y Stock a los tipos correctos
            precio_float = float(precio.get())
            stock_int = int(stock.get())

            # Llamada a la función para agregar el libro
            agregar_libro(titulo.get(), autor.get(), genero.get(), precio_float, stock_int)
            
            # Mostrar mensaje de éxito y cerrar la ventana
            messagebox.showinfo("Éxito", "El libro se añadió correctamente.")
            ventana.destroy()
        except ValueError:
            # Mostrar mensaje de error si hay un valor no numérico en Precio o Stock
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")

    # Botones de Agregar y Cerrar con colores solicitados
    tk.Button(frame, text="Agregar", command=confirmar_agregar, bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(frame, text="Cerrar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)

# Asegúrate de que esta función se llame en el contexto adecuado para abrir la ventana.
