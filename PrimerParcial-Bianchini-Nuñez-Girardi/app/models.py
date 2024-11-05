import sqlite3

def obtener_libros():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_libro, titulo, autor, genero, precio, stock FROM libro")
    libros = cursor.fetchall()
    conn.close()
    return libros

def agregar_libro(titulo, autor, genero, precio):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libro (titulo, autor, genero, precio) VALUES (?, ?, ?, ?)", 
                   (titulo, autor, genero, precio))
    conn.commit()
    conn.close()

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
