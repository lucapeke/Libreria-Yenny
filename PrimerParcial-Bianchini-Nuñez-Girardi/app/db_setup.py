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
        precio REAL NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0 
    )
''')

usuarios_iniciales = [
    ("Juan123", "pass123", "empleado", "Juan", "Pérez", "12345678"),
    ("Ana456", "admin123", "gerente", "Ana", "Gómez", "87654321")
]

libros_iniciales = [
    ("El Principito", "Antoine de Saint-Exupéry", "Infantil", 15.0, 10),
    ("Cien Años de Soledad", "Gabriel García Márquez", "Novela", 20.0, 20),
    ("Don Quijote", "Miguel de Cervantes", "Clásico", 25.0, 1),
    ("1984", "George Orwell", "Distopía", 18.5, 5),
    ("Matar a un Ruiseñor", "Harper Lee", "Novela", 17.0, 8),
    ("Orgullo y Prejuicio", "Jane Austen", "Romance", 12.5, 12),
    ("Fahrenheit 451", "Ray Bradbury", "Ciencia Ficción", 16.0, 7),
    ("La Odisea", "Homero", "Épico", 22.0, 3),
    ("Crimen y Castigo", "Fyodor Dostoyevsky", "Novela", 19.5, 9),
    ("Drácula", "Bram Stoker", "Horror", 21.0, 6),
    ("El Gran Gatsby", "F. Scott Fitzgerald", "Novela", 14.0, 15),
    ("Los Miserables", "Victor Hugo", "Drama", 23.0, 2),
    ("La Metamorfosis", "Franz Kafka", "Ficción", 13.0, 14),
    ("El Guardián entre el Centeno", "J.D. Salinger", "Novela", 12.0, 10),
    ("La Isla del Tesoro", "Robert Louis Stevenson", "Aventura", 18.0, 4),
    ("Frankenstein", "Mary Shelley", "Horror", 20.0, 11),
    ("Ulises", "James Joyce", "Clásico", 26.0, 5),
    ("El Retrato de Dorian Gray", "Oscar Wilde", "Ficción", 17.5, 8),
    ("Hamlet", "William Shakespeare", "Tragedia", 15.0, 13),
    ("El Nombre de la Rosa", "Umberto Eco", "Misterio", 19.0, 6)
]


cursor.executemany('''
    INSERT OR IGNORE INTO usuario (nombre_usuario, contrasena, rol, nombre, apellido, dni)
    VALUES (?, ?, ?, ?, ?, ?)
''', usuarios_iniciales)

cursor.executemany('''
    INSERT OR IGNORE INTO libro (titulo, autor, genero, precio, stock)
    VALUES (?, ?, ?, ?, ?)
''', libros_iniciales)

conn.commit()
conn.close()

print("Base de datos inicializada con datos de prueba.")
