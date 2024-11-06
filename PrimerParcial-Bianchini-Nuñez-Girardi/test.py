import unittest
from unittest.mock import patch, MagicMock
from tkinter import messagebox
import sqlite3

# Importar las funciones del archivo donde las tienes
from app.models import (
    iniciar_sesion,
    registrar_usuario,
    obtener_libros,
    realizar_venta,
    agregar_libro,
    editar_libro,
    eliminar_libro
)

class TestLibreria(unittest.TestCase):

    # Test para la función iniciar_sesion
    def test_iniciar_sesion_exitoso(self):
        # Ahora probamos iniciar sesión con los datos que insertamos
        rol = iniciar_sesion('Juan123', 'pass123')
        self.assertEqual(rol, 'empleado')

    def test_iniciar_sesion_fallido(self):
        # Intentamos iniciar sesión con un usuario inexistente
        rol = iniciar_sesion('usuario_inexistente', 'contrasena_incorrecta')
        self.assertIsNone(rol)

    # Test para la función registrar_usuario
    @patch('tkinter.messagebox.showinfo')
    def test_registrar_usuario_exitoso(self, mock_showinfo):
        registrar_usuario('nuevo_usuario_test', 'NuevaPass1', 'empleado', 'Nuevo', 'Usuario', '12345679')
        mock_showinfo.assert_called_once_with("Registro", "Usuario registrado exitosamente")

    @patch('tkinter.messagebox.showerror')
    def test_registrar_usuario_existente(self, mock_showerror):
        # Intentar registrar un usuario con un nombre de usuario que ya existe
        registrar_usuario('Juan123', 'Contrasena123', 'empleado', 'Juan', 'Pérez', '12345678')
        mock_showerror.assert_called_once_with("Error", "El usuario ya existe")

    # Test para la función obtener_libros
    def test_obtener_libros(self):
        conn = sqlite3.connect("libreria.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_libro, titulo, autor, genero, precio, stock FROM libro")
        libros = cursor.fetchall()
        self.assertGreater(len(libros), 0)  # Asegura que haya al menos un libro en la base de datos
        conn.close()
    

if __name__ == '__main__':
    unittest.main()
