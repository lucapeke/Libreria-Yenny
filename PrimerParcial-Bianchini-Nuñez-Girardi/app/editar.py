# ventana_editar.py

import tkinter as tk
from tkinter import messagebox
from app.models import obtener_libros, editar_libro

def ventana_editar_libro():
    ventana = tk.Toplevel()
    ventana.title("Editar Libro")
    ventana.geometry("1100x700")

    # Título en grande en la parte superior
    titulo = tk.Label(ventana, text="EDITAR", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Marco para la búsqueda y la tabla de inventario
    marco_inventario = tk.Frame(ventana)
    marco_inventario.pack(expand=True, pady=10)

    # Campo de búsqueda
    tk.Label(marco_inventario, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco_inventario, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    # Función para buscar libros
    def buscar_libros():
        # Limpiar la tabla existente
        for widget in marco_inventario.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:  # Limpiar solo las filas de datos
                widget.grid_forget()

        # Obtener el texto de búsqueda
        texto_busqueda = busqueda_entry.get().lower()

        # Obtener y filtrar los libros
        libros = obtener_libros()
        libros_filtrados = [libro for libro in libros if texto_busqueda in libro[1].lower() or texto_busqueda in libro[2].lower()]

        # Mostrar los encabezados de la tabla
        encabezados = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
        for i, encabezado in enumerate(encabezados):
            tk.Label(marco_inventario, text=encabezado, borderwidth=1, relief="solid", width=25, bg="#d3d3d3").grid(row=1, column=i)

        # Mostrar los libros filtrados en la tabla
        for fila, libro in enumerate(libros_filtrados, start=2):  # start=2 para dejar espacio para los encabezados
            for col, dato in enumerate(libro):
                tk.Label(marco_inventario, text=dato, borderwidth=1, relief="solid", width=25).grid(row=fila, column=col)

    # Botón para buscar libros
    tk.Button(marco_inventario, text="Buscar", command=buscar_libros, bg="#2196F3", fg="white").grid(row=0, column=2, padx=10, pady=10)

    # Función para borrar filtros y mostrar todos los libros
    def borrar_filtros():
        busqueda_entry.delete(0, tk.END)  # Limpiar el campo de búsqueda
        buscar_libros()  # Mostrar todos los libros

    # Botón para borrar filtros
    tk.Button(marco_inventario, text="Borrar Filtros", command=borrar_filtros, bg="#b32428", fg="white").grid(row=0, column=3, padx=10, pady=10)

    # Obtener y mostrar todos los libros inicialmente
    buscar_libros()

    # Marco para los campos de entrada
    frame_campos = tk.Frame(ventana)
    frame_campos.pack(pady=20)

    # Campos de entrada para editar libro, organizados horizontalmente
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

    # Función para confirmar la edición del libro
    def confirmar_editar():
        try:
            id_libro_int = int(id_libro.get())
            nuevo_precio_float = float(nuevo_precio.get())
            nuevo_stock_int = int(nuevo_stock.get())

            editar_libro(id_libro_int, nuevo_titulo.get(), nuevo_autor.get(), nuevo_genero.get(), nuevo_precio_float, nuevo_stock_int)
            
            messagebox.showinfo("Éxito", "El libro se ha editado correctamente.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el ID, el Precio y el Stock.")

    # Botones de Editar y Cerrar con colores solicitados
    tk.Button(ventana, text="Editar", command=confirmar_editar, bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)
