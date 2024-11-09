import tkinter as tk
from tkinter import ttk
from app.models import obtener_libros

def ventana_inventario(ventana_anterior):
    ventana = tk.Toplevel()
    ventana.title("Inventario de Libros")
    ventana.geometry("1100x600")

    titulo = tk.Label(ventana, text="INVENTARIO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True, fill="both")

    tk.Label(marco, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    columnas = ("ID", "Título", "Autor", "Género", "Precio", "Stock")
    tree = ttk.Treeview(marco, columns=columnas, show="headings", selectmode="browse")
    bold_font = ("Arial", 10, "bold")
    for col in columnas:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=150, anchor="center")
        tree.tag_configure("header", font=bold_font)

    scrollbar = ttk.Scrollbar(marco, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    tree.grid(row=1, column=0, columnspan=5, sticky="nsew")
    scrollbar.grid(row=1, column=5, sticky="ns")

    marco.grid_rowconfigure(1, weight=1)
    marco.grid_columnconfigure(1, weight=1)

    def buscar_libros():
        for item in tree.get_children():
            tree.delete(item)

        texto_busqueda = busqueda_entry.get().lower()
        libros = obtener_libros()
        libros_filtrados = [libro for libro in libros if texto_busqueda in libro[1].lower() or texto_busqueda in libro[2].lower()]

        for libro in libros_filtrados:
            tree.insert("", "end", values=libro)

    tk.Button(marco, text="Buscar", command=buscar_libros, bg="#2196F3", fg="white").grid(row=0, column=2, padx=10, pady=10)
    
    def borrar_filtros():
        busqueda_entry.delete(0, tk.END)
        buscar_libros()

    tk.Button(marco, text="Borrar Filtros", command=borrar_filtros, bg="#b32428", fg="white").grid(row=0, column=3, padx=10, pady=10)

    buscar_libros()

    tk.Button(ventana, text="Cerrar", command=lambda: [ventana.destroy(), ventana_anterior()], bg="#b32428", fg="white").pack(pady=10)
