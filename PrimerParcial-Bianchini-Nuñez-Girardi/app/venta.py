import tkinter as tk
from tkinter import messagebox, ttk
from app.models import obtener_libros, realizar_venta, obtener_stock_libro  

def ventana_venta(ventana_anterior):
    ventana = tk.Toplevel()
    ventana.title("Realizar Venta")
    ventana.geometry("1100x700")

    carrito = []  

    titulo = tk.Label(ventana, text="VENTA", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    marco_inventario = tk.Frame(ventana)
    marco_inventario.pack(expand=True, pady=10)

    columnas = ["ID", "Título", "Autor", "Género", "Precio", "Stock"]
    tree = ttk.Treeview(marco_inventario, columns=columnas, show="headings", selectmode="browse")
    for col in columnas:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=150, anchor="center")
    tree.grid(row=0, column=0, columnspan=5, sticky="nsew")
    
    scrollbar = ttk.Scrollbar(marco_inventario, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=5, sticky="ns")

    libros = obtener_libros()
    for libro in libros:
        tree.insert("", "end", values=libro)

    tk.Label(ventana, text="Cantidad a Vender").pack(pady=5)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.pack(pady=5)

    marco_carrito = tk.Frame(ventana)
    marco_carrito.pack(pady=10)

    columnas_carrito = ["ID", "Título", "Precio", "Cantidad", "Total"]
    tree_carrito = ttk.Treeview(marco_carrito, columns=columnas_carrito, show="headings")
    for col in columnas_carrito:
        tree_carrito.heading(col, text=col, anchor="center")
        tree_carrito.column(col, width=100, anchor="center")
    tree_carrito.grid(row=0, column=0, columnspan=4)

    def actualizar_carrito():
        for item in tree_carrito.get_children():
            tree_carrito.delete(item)
        
        for item in carrito:
            id_libro, titulo, precio, cantidad = item
            total = precio * cantidad
            tree_carrito.insert("", "end", values=(id_libro, titulo, f"${precio:.2f}", cantidad, f"${total:.2f}"))

    def agregar_al_carrito():
        selected_item = tree.selection()
        if selected_item:
            libro = tree.item(selected_item)["values"]
            cantidad_texto = entry_cantidad.get().strip()

            if cantidad_texto.isdigit():
                cantidad = int(cantidad_texto)
                if cantidad > 0:
                    stock_actual = obtener_stock_libro(libro[0])  

                    if cantidad > stock_actual:
                        messagebox.showerror("Error", f"No hay suficiente stock para el libro '{libro[1]}'. Stock disponible: {stock_actual}")
                    else:
                        carrito.append((libro[0], libro[1], float(libro[4]), cantidad))  
                        actualizar_carrito()  
                        entry_cantidad.delete(0, tk.END)  
                else:
                    messagebox.showerror("Error", "La cantidad debe ser mayor a cero.")
            else:
                messagebox.showerror("Error", "Ingrese una cantidad válida (número entero).")
        else:
            messagebox.showerror("Error", "Seleccione un libro para añadir al carrito.")

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    tk.Button(
        frame_botones, 
        text="Agregar al Carrito", 
        command=agregar_al_carrito,
        bg="#2196F3", 
        fg="white"
    ).pack(side="left", padx=10)

    def eliminar_del_carrito():
        selected_item = tree_carrito.selection()
        if selected_item:
            item = tree_carrito.item(selected_item)["values"]
            id_libro_a_eliminar = item[0]
            carrito[:] = [item for item in carrito if item[0] != id_libro_a_eliminar] 
            actualizar_carrito() 
        else:
            messagebox.showerror("Error", "Seleccione un libro para eliminar del carrito.")

    tk.Button(
        frame_botones, 
        text="Eliminar del Carrito", 
        command=eliminar_del_carrito,
        bg="#b32428", 
        fg="white"
    ).pack(side="left", padx=10)

    def confirmar_venta():
        if carrito:
            total_costo = 0
            detalles_venta = ""
            for item in carrito:
                id_libro, titulo, precio, cantidad = item
                exito, libro_vendido = realizar_venta(id_libro, cantidad)

                if exito:
                    costo_total = precio * cantidad
                    total_costo += costo_total
                    detalles_venta += f"{titulo} - Cantidad: {cantidad}, Total: ${costo_total:.2f}\n"
                else:
                    messagebox.showerror("Error", f"No hay suficiente stock para el libro '{titulo}'.")
                    return

            messagebox.showinfo("Venta Exitosa", f"Venta realizada con éxito\n\n{detalles_venta}\nTotal de la venta: ${total_costo:.2f}")
            carrito.clear()
            actualizar_carrito()
            ventana.destroy()
            ventana_anterior()
        else:
            messagebox.showerror("Error", "El carrito está vacío. Agregue libros para realizar la venta.")

    frame_confirmar_cancelar = tk.Frame(ventana)
    frame_confirmar_cancelar.pack(pady=10)

    tk.Button(
        frame_confirmar_cancelar, 
        text="Confirmar Venta", 
        command=confirmar_venta,
        bg="#0b6730", 
        fg="white"
    ).pack(side="left", padx=10)

    tk.Button(
        frame_confirmar_cancelar, 
        text="Cancelar", 
        command=lambda: [ventana.destroy(), ventana_anterior()],
        bg="red", 
        fg="white"
    ).pack(side="left", padx=10)
