import sqlite3

def obtener_libros():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_libro, titulo, autor, genero, precio FROM libro")
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
