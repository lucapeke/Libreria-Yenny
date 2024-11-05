import sqlite3
from tkinter import messagebox

def registrar_usuario(nombre_usuario, contrasena, rol, nombre, apellido, dni):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO usuario (nombre_usuario, contrasena, rol, nombre, apellido, dni) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre_usuario, contrasena, rol, nombre, apellido, dni))
        conn.commit()
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El usuario ya existe")
    conn.close()

def obtener_libros():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_libro, titulo, autor, genero, precio, stock FROM libro")
    libros = cursor.fetchall()
    conn.close()
    return libros

def realizar_venta(id_libro, cantidad):
    # Conectar a la base de datos
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    # Verificar el stock disponible
    cursor.execute("SELECT titulo, precio, stock FROM libro WHERE id_libro = ?", (id_libro,))
    resultado = cursor.fetchone()

    if resultado:
        titulo, precio, stock = resultado
        if stock >= cantidad:
            # Realizar la venta restando el stock
            nuevo_stock = stock - cantidad
            cursor.execute("UPDATE libro SET stock = ? WHERE id_libro = ?", (nuevo_stock, id_libro))
            conn.commit()

            # Cerrar la conexión y devolver éxito y detalles del libro
            conn.close()
            libro_vendido = {
                "titulo": titulo,
                "precio": precio,
                "stock_restante": nuevo_stock
            }
            return True, libro_vendido  # Éxito y detalles del libro
        else:
            # No hay suficiente stock
            conn.close()
            return False, None  # Error por falta de stock
    else:
        # Libro no encontrado
        conn.close()
        return False, None  # Error, libro no encontrado
    

# Función para agregar un libro a la base de datos
def agregar_libro(titulo, autor, genero, precio, stock):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO libro (titulo, autor, genero, precio, stock)
        VALUES (?, ?, ?, ?, ?)
    ''', (titulo, autor, genero, precio, stock))
    conn.commit()
    conn.close()


# Función para editar un libro en la base de datos
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

# Función para eliminar un libro de la base de datos
def eliminar_libro(id_libro):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libro WHERE id_libro = ?", (id_libro,))
    conn.commit()
    conn.close()
