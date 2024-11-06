
import tkinter as tk
from tkinter import messagebox
from app.models import obtener_libros, confirmar_eliminar

def ventana_eliminar_libro():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Libro")
    ventana.geometry("1100x750")

    titulo = tk.Label(ventana, text="ELIMINAR", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco_inventario = tk.Frame(ventana)
    marco_inventario.pack(expand=True, pady=10)

    tk.Label(marco_inventario, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco_inventario, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    def buscar_libros():
        for widget in marco_inventario.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
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

    frame = tk.Frame(ventana)
    frame.pack(pady=20)

    tk.Label(frame, text="ID del Libro a Eliminar").pack(pady=5)
    id_libro = tk.Entry(frame)
    id_libro.pack(pady=5)

    tk.Button(frame, text="Eliminar", command=lambda: confirmar_eliminar(ventana, id_libro), bg="#b32428", fg="white").pack(pady=10)
    tk.Button(frame, text="Volver", command=ventana.destroy, bg="#2196F3", fg="white").pack(pady=10)
