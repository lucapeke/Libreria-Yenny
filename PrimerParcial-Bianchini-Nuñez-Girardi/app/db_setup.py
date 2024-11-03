import sqlite3

def inicializar_db():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libro (
            id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT,
            precio REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            nombre_usuario TEXT PRIMARY KEY,
            contrasena TEXT NOT NULL,
            rol TEXT NOT NULL
        )
    ''')

    cursor.execute("INSERT OR IGNORE INTO usuario VALUES ('gerente', 'admin123', 'gerente')")
    
    conn.commit()
    conn.close()

inicializar_db()
