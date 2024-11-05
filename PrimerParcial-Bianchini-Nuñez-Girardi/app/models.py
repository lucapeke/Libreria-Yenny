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
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    # Verificar disponibilidad
    cursor.execute("SELECT cantidad FROM libro WHERE id_libro = ?", (id_libro,))
    resultado = cursor.fetchone()
    if not resultado or resultado[0] < int(cantidad):
        conn.close()
        return False  # No hay suficiente stock

    # Realizar la venta (restar cantidad)
    nueva_cantidad = resultado[0] - int(cantidad)
    cursor.execute("UPDATE libro SET cantidad = ? WHERE id_libro = ?", (nueva_cantidad, id_libro))
    conn.commit()
    conn.close()
    return True
