import tkinter as tk
from app.models import obtener_libros

def ventana_inventario():
    ventana = tk.Toplevel()
    ventana.title("Inventario de Libros")
    ventana.geometry("1100x600")

    titulo = tk.Label(ventana, text="INVENTARIO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    tk.Label(marco, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    def buscar_libros():
        for widget in marco.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()

        texto_busqueda = busqueda_entry.get().lower()

        libros = obtener_libros()
        libros_filtrados = [libro for libro in libros if texto_busqueda in libro[1].lower() or texto_busqueda in libro[2].lower()]

        encabezados = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
        for i, encabezado in enumerate(encabezados):
            tk.Label(marco, text=encabezado, borderwidth=1, relief="solid", width=25, bg="#d3d3d3").grid(row=1, column=i)

        for fila, libro in enumerate(libros_filtrados, start=2):
            for col, dato in enumerate(libro):
                tk.Label(marco, text=dato, borderwidth=1, relief="solid", width=25).grid(row=fila, column=col)

    tk.Button(marco, text="Buscar", command=buscar_libros, bg="#2196F3", fg="white").grid(row=0, column=2, padx=10, pady=10)

    def borrar_filtros():
        busqueda_entry.delete(0, tk.END)
        buscar_libros()

    tk.Button(marco, text="Borrar Filtros", command=borrar_filtros, bg="#b32428", fg="white").grid(row=0, column=3, padx=10, pady=10)

    buscar_libros()

    tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)
