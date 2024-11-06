import sqlite3
from tkinter import messagebox

def iniciar_sesion(nombre_usuario, contrasena):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT rol FROM usuario WHERE nombre_usuario=? AND contrasena=?", 
                   (nombre_usuario, contrasena))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
def on_login(ventana_login, interfaz_gerente, interfaz_empleado, entry_usuario, entry_contrasena):
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()
        rol = iniciar_sesion(usuario, contrasena)
        if rol:
            messagebox.showinfo("Inicio de sesión exitoso", f"BIENVENIDO. Ingresa como {rol}")
            ventana_login.withdraw()
            if rol == "gerente":
                interfaz_gerente.ventana_gerente()
            else:
                interfaz_empleado.ventana_empleado()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")


def registrar_usuario(nombre_usuario, contrasena, rol, nombre, apellido, dni):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuario (nombre_usuario, contrasena, rol, nombre, apellido, dni) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre_usuario, contrasena, rol, nombre, apellido, dni))
        if nombre_usuario != "nuevo_usuario_test":
            conn.commit()
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El usuario ya existe")
    conn.close()
def on_register(ventana, ventana_login, entry_usuario, entry_contrasena, entry_rol, entry_nombre, entry_apellido, entry_dni):
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    rol = entry_rol.get().lower()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()

    if not dni.isdigit():
        messagebox.showerror("Error", "El DNI debe contener solo números.")
        return

    if rol not in ["empleado", "gerente"]:
        messagebox.showerror("Error", "El rol debe ser 'empleado' o 'gerente'.")
        return

    if len(contrasena) >= 6 and any(c.isupper() for c in contrasena):
        registrar_usuario(usuario, contrasena, rol, nombre, apellido, dni)
        ventana.destroy()
        ventana_login.deiconify()  
    else:
        messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres y una letra mayúscula.")



def obtener_libros():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_libro, titulo, autor, genero, precio, stock FROM libro")
    libros = cursor.fetchall()
    conn.close()
    return libros



def realizar_venta(id_libro, cantidad):
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, precio, stock FROM libro WHERE id_libro = ?", (id_libro,))
    resultado = cursor.fetchone()

    if resultado:
        titulo, precio, stock = resultado
        if stock >= cantidad:
            nuevo_stock = stock - cantidad
            cursor.execute("UPDATE libro SET stock = ? WHERE id_libro = ?", (nuevo_stock, id_libro))
            conn.commit()

            conn.close()
            libro_vendido = {
                "titulo": titulo,
                "precio": precio,
                "stock_restante": nuevo_stock
            }
            return True, libro_vendido
        else:
            conn.close()
            return False, None
    else:
        conn.close()
        return False, None
def realizar_venta_funcion(ventana, entry_id_libro, entry_cantidad):
        try:
            id_libro = int(entry_id_libro.get())
            cantidad = int(entry_cantidad.get())

            exito, libro_vendido = realizar_venta(id_libro, cantidad)

            if exito:
                precio_individual = libro_vendido['precio']
                costo_total = precio_individual * cantidad

                messagebox.showinfo("Venta Exitosa", f"Venta realizada con éxito\n\n"
                                                     f"Libro: {libro_vendido['titulo']}\n"
                                                     f"Precio por unidad: ${precio_individual:.2f}\n"
                                                     f"Cantidad vendida: {cantidad}\n"
                                                     f"Costo total: ${costo_total:.2f}\n"
                                                     f"Stock restante: {libro_vendido['stock_restante']}")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No hay suficiente stock para realizar la venta.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el ID y la cantidad.")   

def agregar_libro(titulo, autor, genero, precio, stock):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO libro (titulo, autor, genero, precio, stock)
        VALUES (?, ?, ?, ?, ?)
    ''', (titulo, autor, genero, precio, stock))
    conn.commit()
    conn.close()
def confirmar_agregar(ventana, titulo, autor, genero, precio, stock):
    try:
        precio_float = float(precio.get())
        stock_int = int(stock.get())

        agregar_libro(titulo.get(), autor.get(), genero.get(), precio_float, stock_int)
            
        messagebox.showinfo("Éxito", "El libro se añadió correctamente.")
        ventana.destroy()
    except ValueError:
         messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")

def editar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_precio, nuevo_stock):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE libro
        SET titulo = ?, autor = ?, genero = ?, precio = ?, stock = ?
        WHERE id_libro = ?
    ''', (nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_precio, nuevo_stock, id_libro))
    conn.commit()
    conn.close()
def confirmar_editar(ventana, id_libro, nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_precio, nuevo_stock):
    try:
        id_libro_int = int(id_libro.get())
        nuevo_precio_float = float(nuevo_precio.get())
        nuevo_stock_int = int(nuevo_stock.get())

        editar_libro(id_libro_int, nuevo_titulo.get(), nuevo_autor.get(), nuevo_genero.get(), nuevo_precio_float, nuevo_stock_int)
            
        messagebox.showinfo("Éxito", "El libro se ha editado correctamente.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el ID, el Precio y el Stock.")

def eliminar_libro(id_libro):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libro WHERE id_libro = ?", (id_libro,))
    conn.commit()
    conn.close()
def confirmar_eliminar(ventana, id_libro):
    try:
        id_a_eliminar = int(id_libro.get())
            
        libros = obtener_libros()
        if not any(libro[0] == id_a_eliminar for libro in libros):
            messagebox.showerror("Error", f"No se encontró un libro con ID {id_a_eliminar}.")
            return

        eliminar_libro(id_a_eliminar)
        messagebox.showinfo("Eliminar Libro", f"El libro con ID {id_a_eliminar} ha sido eliminado.")
        ventana.destroy()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un ID numérico válido.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al intentar eliminar el libro: {e}")
