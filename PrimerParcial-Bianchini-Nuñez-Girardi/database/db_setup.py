import sqlite3
import os

ruta_carpeta = "database"
nombre_bd = "libreria.db"
ruta_bd = os.path.join(ruta_carpeta, nombre_bd)

conn = sqlite3.connect(ruta_bd)
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
    ("El Nombre de la Rosa", "Umberto Eco", "Misterio", 19.0, 6),
    ("La Sombra del Viento", "Carlos Ruiz Zafón", "Misterio", 22.5, 14),
    ("El Código Da Vinci", "Dan Brown", "Suspenso", 25.0, 18),
    ("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 30.0, 12),
    ("Los Pilares de la Tierra", "Ken Follett", "Histórico", 28.0, 9),
    ("El Alquimista", "Paulo Coelho", "Ficción", 15.0, 17),
    ("La Casa de los Espíritus", "Isabel Allende", "Realismo Mágico", 20.0, 13),
    ("Crónica de una Muerte Anunciada", "Gabriel García Márquez", "Crónica", 18.0, 7),
    ("El Perfume", "Patrick Süskind", "Suspenso", 22.0, 10),
    ("El Hobbit", "J.R.R. Tolkien", "Fantasía", 19.0, 15),
    ("Moby Dick", "Herman Melville", "Clásico", 24.0, 8),
    ("La Metamorfosis", "Franz Kafka", "Ficción", 13.0, 6),
    ("El Corazón de las Tinieblas", "Joseph Conrad", "Aventura", 21.0, 10),
    ("En Busca del Tiempo Perdido", "Marcel Proust", "Filosofía", 35.0, 4),
    ("Los hermanos Karamazov", "Fyodor Dostoyevsky", "Filosofía", 27.5, 5),
    ("Rebelión en la Granja", "George Orwell", "Política", 14.0, 12),
    ("El Gran Gatsby", "F. Scott Fitzgerald", "Novela", 14.0, 15),
    ("Cumbres Borrascosas", "Emily Brontë", "Romántico", 21.5, 8),
    ("El Señor de los Anillos: La Comunidad del Anillo", "J.R.R. Tolkien", "Fantasía", 28.0, 10),
    ("La Broma Infinita", "David Foster Wallace", "Ficción", 40.0, 3),
    ("Los Detectives Salvajes", "Roberto Bolaño", "Novela", 19.0, 9)
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

print(f"Base de datos inicializada en la carpeta 'database' con datos de prueba en {ruta_bd}.")
