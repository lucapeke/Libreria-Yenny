import tkinter as tk
from tkinter import messagebox, ttk
from app.models import obtener_libros, confirmar_editar, nav_gestionar_inventario

def ventana_editar_libro():
    ventana = tk.Toplevel()
    ventana.title("Editar Libro")
    ventana.geometry("960x500")

    titulo = tk.Label(ventana, text="EDITAR", font=("Arial", 16, "bold"))
    titulo.grid(row=0, column=0, columnspan=6, pady=10)

    marco_inventario = tk.Frame(ventana)
    marco_inventario.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

    tk.Label(marco_inventario, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco_inventario, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    columnas = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
    tree = ttk.Treeview(marco_inventario, columns=columnas, show="headings", selectmode="browse")
    for col in columnas:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=150, anchor="center")

    tree.grid(row=1, column=0, columnspan=5, sticky="nsew")
    scrollbar = ttk.Scrollbar(marco_inventario, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=5, sticky="ns")

    def buscar_libros():
        for item in tree.get_children():
            tree.delete(item)

        texto_busqueda = busqueda_entry.get().lower()
        libros = obtener_libros()
        libros_filtrados = [libro for libro in libros if texto_busqueda in libro[1].lower() or texto_busqueda in libro[2].lower()]

        for libro in libros_filtrados:
            tree.insert("", "end", values=libro)

    tk.Button(marco_inventario, text="Buscar", command=buscar_libros, bg="#2196F3", fg="white").grid(row=0, column=2, padx=10, pady=10)

    def borrar_filtros():
        busqueda_entry.delete(0, tk.END)
        buscar_libros()

    tk.Button(marco_inventario, text="Borrar Filtros", command=borrar_filtros, bg="#b32428", fg="white").grid(row=0, column=3, padx=10, pady=10)

    buscar_libros()

    frame_campos = tk.Frame(ventana)
    frame_campos.grid(row=2, column=0, columnspan=6, pady=20)

    tk.Label(frame_campos, text="ID del Libro").grid(row=0, column=0, padx=5, pady=5)
    id_libro = tk.Label(frame_campos, text="", width=20, relief="solid")  # Cambiamos a Label
    id_libro.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Título").grid(row=0, column=2, padx=5, pady=5)
    nuevo_titulo = tk.Entry(frame_campos, width=20)
    nuevo_titulo.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Autor").grid(row=0, column=4, padx=5, pady=5)
    nuevo_autor = tk.Entry(frame_campos, width=20)
    nuevo_autor.grid(row=0, column=5, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Género").grid(row=1, column=0, padx=5, pady=5)
    nuevo_genero = tk.Entry(frame_campos, width=20)
    nuevo_genero.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Precio").grid(row=1, column=2, padx=5, pady=5)
    nuevo_precio = tk.Entry(frame_campos, width=20)
    nuevo_precio.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(frame_campos, text="Nuevo Stock").grid(row=1, column=4, padx=5, pady=5)
    nuevo_stock = tk.Entry(frame_campos, width=20)
    nuevo_stock.grid(row=1, column=5, padx=5, pady=5)

    def cargar_libro(event):
        selected_item = tree.selection()
        if selected_item:
            libro = tree.item(selected_item)["values"]
            id_libro.config(text=libro[0])  # Actualiza el texto del Label
            nuevo_titulo.delete(0, tk.END)
            nuevo_titulo.insert(0, libro[1])
            nuevo_autor.delete(0, tk.END)
            nuevo_autor.insert(0, libro[2])
            nuevo_genero.delete(0, tk.END)
            nuevo_genero.insert(0, libro[3])
            nuevo_precio.delete(0, tk.END)
            nuevo_precio.insert(0, libro[4])
            nuevo_stock.delete(0, tk.END)
            nuevo_stock.insert(0, libro[5])

    tree.bind("<<TreeviewSelect>>", cargar_libro)

    # Frame para los botones
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=3, column=0, columnspan=6, pady=10)

    boton_editar = tk.Button(
        frame_botones,
        text="Editar",
        command=lambda: confirmar_editar(ventana, id_libro["text"], nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_precio, nuevo_stock),
        bg="#2196F3",
        fg="white"
    )
    boton_editar.grid(row=0, column=0, padx=10)

    boton_cerrar = tk.Button(
        frame_botones,
        text="Cerrar",
        command=lambda: nav_gestionar_inventario(ventana),
        bg="#b32428",
        fg="white"
    )
    boton_cerrar.grid(row=0, column=1, padx=10)
