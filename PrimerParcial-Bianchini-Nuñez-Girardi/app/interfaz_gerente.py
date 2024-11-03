import tkinter as tk
from app.models import obtener_libros, agregar_libro

def ventana_gerente():
    ventana = tk.Toplevel()
    ventana.title("Panel de Gerente")

    tk.Label(ventana, text="Inventario").pack()
    libros = obtener_libros()
    for libro in libros:
        tk.Label(ventana, text=f"{libro[1]} - {libro[2]} - {libro[3]} - ${libro[4]}").pack()

    tk.Label(ventana, text="Título").pack()
    entry_titulo = tk.Entry(ventana)
    entry_titulo.pack()

    tk.Label(ventana, text="Autor").pack()
    entry_autor = tk.Entry(ventana)
    entry_autor.pack()

    tk.Label(ventana, text="Género").pack()
    entry_genero = tk.Entry(ventana)
    entry_genero.pack()

    tk.Label(ventana, text="Precio").pack()
    entry_precio = tk.Entry(ventana)
    entry_precio.pack()

    def on_agregar_libro():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        genero = entry_genero.get()
        precio = float(entry_precio.get())
        agregar_libro(titulo, autor, genero, precio)
        ventana.destroy()
        ventana_gerente()  # Refresca la ventana

    tk.Button(ventana, text="Agregar Libro", command=on_agregar_libro).pack()
