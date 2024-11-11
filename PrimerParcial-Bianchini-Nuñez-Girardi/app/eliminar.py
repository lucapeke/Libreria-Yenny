import tkinter as tk
from tkinter import messagebox, ttk
from app.models import obtener_libros, confirmar_eliminar, nav_gestionar_inventario

def ventana_eliminar_libro():
    ventana = tk.Toplevel()
    ventana.title("Eliminar Libro")
    ventana.geometry("960x450")

    titulo = tk.Label(ventana, text="ELIMINAR", font=("Arial", 16, "bold"))
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

    
    scrollbar = ttk.Scrollbar(marco_inventario, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=6, sticky="ns")

    tree.grid(row=1, column=0, columnspan=5, pady=(10, 20))

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

    
    def obtener_id_seleccionado():
        seleccionado = tree.selection()
        if seleccionado:
            item = tree.item(seleccionado[0])
            return item['values'][0]  
        return None

    
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=2, column=0, columnspan=6, pady=10)

    
    def eliminar_libro_seleccionado():
        id_libro_seleccionado = obtener_id_seleccionado()

        if id_libro_seleccionado:
            confirmar_eliminar(ventana, id_libro_seleccionado)
        else:
            messagebox.showerror("Error", "Seleccione un libro para eliminar.")

    boton_eliminar = tk.Button(
        frame_botones,
        text="Eliminar",
        command=eliminar_libro_seleccionado,
        bg="#b32428",
        fg="white"
    )
    boton_eliminar.grid(row=0, column=0, padx=10)

    
    boton_volver = tk.Button(
        frame_botones,
        text="Volver",
        command=lambda: nav_gestionar_inventario(ventana),
        bg="#2196F3",
        fg="white"
    )
    boton_volver.grid(row=0, column=1, padx=10)
