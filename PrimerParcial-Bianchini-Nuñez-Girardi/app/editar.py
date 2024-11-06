
import tkinter as tk
from tkinter import messagebox
from app.models import obtener_libros, confirmar_editar

def ventana_editar_libro():
    ventana = tk.Toplevel()
    ventana.title("Editar Libro")
    ventana.geometry("1100x800")

    titulo = tk.Label(ventana, text="EDITAR", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco_inventario = tk.Frame(ventana)
    marco_inventario.pack(expand=True, pady=10)

    tk.Label(marco_inventario, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco_inventario, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    def buscar_libros():
        for widget in marco_inventario.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        texto_busqueda = busqueda_entry.get().lower()

        libros = obtener_libros()
        libros_filtrados = [libro for libro in libros if texto_busqueda in libro[1].lower() or texto_busqueda in libro[2].lower()]

        encabezados = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
        for i, encabezado in enumerate(encabezados):
            tk.Label(marco_inventario, text=encabezado, borderwidth=1, relief="solid", width=25, bg="#d3d3d3").grid(row=1, column=i)

        for fila, libro in enumerate(libros_filtrados, start=2):
            for col, dato in enumerate(libro):
                tk.Label(marco_inventario, text=dato, borderwidth=1, relief="solid", width=25).grid(row=fila, column=col)

    tk.Button(marco_inventario, text="Buscar", command=buscar_libros, bg="#2196F3", fg="white").grid(row=0, column=2, padx=10, pady=10)

    def borrar_filtros():
        busqueda_entry.delete(0, tk.END)
        buscar_libros()

    tk.Button(marco_inventario, text="Borrar Filtros", command=borrar_filtros, bg="#b32428", fg="white").grid(row=0, column=3, padx=10, pady=10)

    buscar_libros()

    frame_campos = tk.Frame(ventana)
    frame_campos.pack(pady=20)

    tk.Label(frame_campos, text="ID del Libro").grid(row=0, column=0, padx=5, pady=5)
    id_libro = tk.Entry(frame_campos, width=20)
    id_libro.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Título").grid(row=0, column=2, padx=5, pady=5)
    nuevo_titulo = tk.Entry(frame_campos, width=20)
    nuevo_titulo.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Autor").grid(row=1, column=0, padx=5, pady=5)
    nuevo_autor = tk.Entry(frame_campos, width=20)
    nuevo_autor.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Género").grid(row=1, column=2, padx=5, pady=5)
    nuevo_genero = tk.Entry(frame_campos, width=20)
    nuevo_genero.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Precio").grid(row=2, column=0, padx=5, pady=5)
    nuevo_precio = tk.Entry(frame_campos, width=20)
    nuevo_precio.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Stock").grid(row=2, column=2, padx=5, pady=5)
    nuevo_stock = tk.Entry(frame_campos, width=20)
    nuevo_stock.grid(row=2, column=3, padx=5, pady=5)

    tk.Button(ventana, text="Editar", command=lambda: confirmar_editar(ventana, id_libro, nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_precio, nuevo_stock), bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)
