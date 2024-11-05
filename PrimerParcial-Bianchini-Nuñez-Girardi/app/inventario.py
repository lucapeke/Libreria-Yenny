import tkinter as tk
from app.models import obtener_libros

def ventana_inventario():
    ventana = tk.Toplevel()
    ventana.title("Inventario de Libros")
    ventana.geometry("1100x600")

    # Título en grande en la parte superior
    titulo = tk.Label(ventana, text="INVENTARIO", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    # Marco para centrar la tabla
    marco = tk.Frame(ventana)
    marco.pack(expand=True)

    # Campo de búsqueda
    tk.Label(marco, text="Buscar:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    busqueda_entry = tk.Entry(marco, width=25)
    busqueda_entry.grid(row=0, column=1, padx=10, pady=10)

    # Función para buscar libros
    def buscar_libros():
        # Limpiar la tabla existente
        for widget in marco.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:  # Solo limpiar filas de datos
                widget.grid_forget()

        # Obtener el texto de búsqueda
        texto_busqueda = busqueda_entry.get().lower()

        # Obtener y filtrar los libros
        libros = obtener_libros()
        libros_filtrados = [libro for libro in libros if texto_busqueda in libro[1].lower() or texto_busqueda in libro[2].lower()]

        # Mostrar los encabezados de la tabla
        encabezados = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
        for i, encabezado in enumerate(encabezados):
            tk.Label(marco, text=encabezado, borderwidth=1, relief="solid", width=25, bg="#d3d3d3").grid(row=1, column=i)

        # Mostrar los libros filtrados en la tabla
        for fila, libro in enumerate(libros_filtrados, start=2):  # start=2 para dejar espacio para los encabezados
            for col, dato in enumerate(libro):
                tk.Label(marco, text=dato, borderwidth=1, relief="solid", width=25).grid(row=fila, column=col)

    # Botón para buscar libros
    tk.Button(marco, text="Buscar", command=buscar_libros, bg="#2196F3", fg="white").grid(row=0, column=2, padx=10, pady=10)

    # Función para borrar filtros y mostrar todos los libros
    def borrar_filtros():
        busqueda_entry.delete(0, tk.END)  # Limpiar el campo de búsqueda
        buscar_libros()  # Mostrar todos los libros

    # Botón para borrar filtros
    tk.Button(marco, text="Borrar Filtros", command=borrar_filtros, bg="#b32428", fg="white").grid(row=0, column=3, padx=10, pady=10)

    # Obtener y mostrar todos los libros inicialmente
    buscar_libros()

    # Botón para cerrar la ventana
    tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#b32428", fg="white").pack(pady=10)

# Llamar a la función para mostrar la ventana (puedes hacerlo desde otra parte de tu código)
# ventana_inventario()
