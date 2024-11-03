import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usuario TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL,
        rol TEXT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        dni TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS libro (
        id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        genero TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')

usuarios_iniciales = [
    ("Juan123", "pass123", "empleado", "Juan", "Pérez", "12345678"),
    ("Ana456", "admin123", "gerente", "Ana", "Gómez", "87654321")
]

libros_iniciales = [
    ("El Principito", "Antoine de Saint-Exupéry", "Infantil", 15.0),
    ("Cien Años de Soledad", "Gabriel García Márquez", "Novela", 20.0),
    ("Don Quijote", "Miguel de Cervantes", "Clásico", 25.0)
]

cursor.executemany('''
    INSERT OR IGNORE INTO usuario (nombre_usuario, contrasena, rol, nombre, apellido, dni)
    VALUES (?, ?, ?, ?, ?, ?)
''', usuarios_iniciales)

cursor.executemany('''
    INSERT OR IGNORE INTO libro (titulo, autor, genero, precio)
    VALUES (?, ?, ?, ?)
''', libros_iniciales)

conn.commit()
conn.close()

print("Base de datos inicializada con datos de prueba.")
