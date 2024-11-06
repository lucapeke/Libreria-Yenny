import unittest
from unittest.mock import patch, MagicMock
from tkinter import messagebox
import sqlite3

from app.models import (
    iniciar_sesion,
    registrar_usuario,
    on_register,
    realizar_venta,
    realizar_venta_funcion,
    confirmar_agregar, 
    confirmar_editar, 
    eliminar_libro, 
    confirmar_eliminar
)

class TestLibreria(unittest.TestCase):

    def test_iniciar_sesion_exitoso(self):
        rol = iniciar_sesion('Juan123', 'pass123')
        self.assertEqual(rol, 'empleado')
    def test_iniciar_sesion_fallido(self):
        rol = iniciar_sesion('usuario_inexistente', 'contrasena_incorrecta')
        self.assertIsNone(rol)



    @patch('tkinter.messagebox.showinfo')
    def test_registrar_usuario_exitoso(self, mock_showinfo):
        registrar_usuario('nuevo_usuario_test', 'NuevaPass1', 'empleado', 'Nuevo', 'Usuario', '12345679')
        mock_showinfo.assert_called_once_with("Registro", "Usuario registrado exitosamente")
    @patch('tkinter.messagebox.showerror')
    def test_registrar_usuario_existente(self, mock_showerror):
        registrar_usuario('Juan123', 'Contrasena123', 'empleado', 'Juan', 'Pérez', '12345678')
        mock_showerror.assert_called_once_with("Error", "El usuario ya existe")
    def setUp(self):
        self.ventana = MagicMock()
        self.ventana_login = MagicMock()
        self.entry_usuario = MagicMock()
        self.entry_contrasena = MagicMock()
        self.entry_rol = MagicMock()
        self.entry_nombre = MagicMock()
        self.entry_apellido = MagicMock()
        self.entry_dni = MagicMock()
    @patch('tkinter.messagebox.showerror')
    def test_on_register_dni_invalido(self, mock_showerror):
        self.entry_dni.get.return_value = "ABC123"
        self.entry_rol.get.return_value = "empleado"
        on_register(self.ventana, self.ventana_login, self.entry_usuario, self.entry_contrasena,
                    self.entry_rol, self.entry_nombre, self.entry_apellido, self.entry_dni)
        mock_showerror.assert_called_once_with("Error", "El DNI debe contener solo números.")
    @patch('tkinter.messagebox.showerror')
    def test_on_register_rol_invalido(self, mock_showerror):
        self.entry_rol.get.return_value = "admin"
        self.entry_dni.get.return_value = "12345678"
        on_register(self.ventana, self.ventana_login, self.entry_usuario, self.entry_contrasena,
                    self.entry_rol, self.entry_nombre, self.entry_apellido, self.entry_dni)
        mock_showerror.assert_called_once_with("Error", "El rol debe ser 'empleado' o 'gerente'.")
    @patch('tkinter.messagebox.showerror')
    def test_on_register_contrasena_invalida(self, mock_showerror):
        self.entry_rol.get.return_value = "empleado"
        self.entry_dni.get.return_value = "12345678"
        self.entry_contrasena.get.return_value = "abc123"
        on_register(self.ventana, self.ventana_login, self.entry_usuario, self.entry_contrasena,
                    self.entry_rol, self.entry_nombre, self.entry_apellido, self.entry_dni)
        mock_showerror.assert_called_once_with("Error", "La contraseña debe tener al menos 6 caracteres y una letra mayúscula.")

    @patch("sqlite3.connect")
    def test_realizar_venta_exitoso(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn
        mock_cursor.fetchone.return_value = ("Libro Prueba", 20.0, 10)
        exito, libro_vendido = realizar_venta(1, 5)
        self.assertTrue(exito)
        self.assertIsNotNone(libro_vendido)
        self.assertEqual(libro_vendido["titulo"], "Libro Prueba")
        self.assertEqual(libro_vendido["precio"], 20.0)
        self.assertEqual(libro_vendido["stock_restante"], 5)
        mock_cursor.execute.assert_called_with("UPDATE libro SET stock = ? WHERE id_libro = ?", (5, 1))
    @patch("sqlite3.connect")
    def test_realizar_venta_sin_stock(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn
        mock_cursor.fetchone.return_value = ("Libro Prueba", 20.0, 3)
        exito, libro_vendido = realizar_venta(1, 5)
        self.assertFalse(exito)
        self.assertIsNone(libro_vendido)
    @patch("sqlite3.connect")
    def test_realizar_venta_libro_no_encontrado(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn
        mock_cursor.fetchone.return_value = None
        exito, libro_vendido = realizar_venta(99, 2)
        self.assertFalse(exito)
        self.assertIsNone(libro_vendido)
    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("app.models.realizar_venta")
    def test_realizar_venta_funcion_exitoso(self, mock_realizar_venta, mock_showerror, mock_showinfo):
        mock_realizar_venta.return_value = (True, {
            "titulo": "Libro Prueba",
            "precio": 15.0,
            "stock_restante": 5
        })
        ventana_mock = MagicMock()
        entry_id_libro_mock = MagicMock()
        entry_cantidad_mock = MagicMock()
        entry_id_libro_mock.get.return_value = "1"
        entry_cantidad_mock.get.return_value = "2"
        realizar_venta_funcion(ventana_mock, entry_id_libro_mock, entry_cantidad_mock)
        mock_showinfo.assert_called_once_with("Venta Exitosa", 
            "Venta realizada con éxito\n\n"
            "Libro: Libro Prueba\n"
            "Precio por unidad: $15.00\n"
            "Cantidad vendida: 2\n"
            "Costo total: $30.00\n"
            "Stock restante: 5"
        )
        ventana_mock.destroy.assert_called_once()
        mock_showerror.assert_not_called()
    @patch("tkinter.messagebox.showerror")
    @patch("app.models.realizar_venta")
    def test_realizar_venta_funcion_sin_stock(self, mock_realizar_venta, mock_showerror):
        mock_realizar_venta.return_value = (False, None)
        ventana_mock = MagicMock()
        entry_id_libro_mock = MagicMock()
        entry_cantidad_mock = MagicMock()
        entry_id_libro_mock.get.return_value = "1"
        entry_cantidad_mock.get.return_value = "10"
        realizar_venta_funcion(ventana_mock, entry_id_libro_mock, entry_cantidad_mock)
        mock_showerror.assert_called_once_with("Error", "No hay suficiente stock para realizar la venta.")
        ventana_mock.destroy.assert_not_called()
    @patch("tkinter.messagebox.showerror")
    def test_realizar_venta_funcion_valores_invalidos(self, mock_showerror):
        ventana_mock = MagicMock()
        entry_id_libro_mock = MagicMock()
        entry_cantidad_mock = MagicMock()
        entry_id_libro_mock.get.return_value = "id_invalido"
        entry_cantidad_mock.get.return_value = "cantidad_invalida"
        realizar_venta_funcion(ventana_mock, entry_id_libro_mock, entry_cantidad_mock)
        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el ID y la cantidad.")
        ventana_mock.destroy.assert_not_called()

    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("app.models.agregar_libro")
    def test_confirmar_agregar_exitoso(self, mock_agregar_libro, mock_showerror, mock_showinfo):
        ventana_mock = MagicMock()
        titulo_mock = MagicMock()
        autor_mock = MagicMock()
        genero_mock = MagicMock()
        precio_mock = MagicMock()
        stock_mock = MagicMock()

        titulo_mock.get.return_value = "Libro Test"
        autor_mock.get.return_value = "Autor Test"
        genero_mock.get.return_value = "Género Test"
        precio_mock.get.return_value = "29.99"
        stock_mock.get.return_value = "10"

        confirmar_agregar(ventana_mock, titulo_mock, autor_mock, genero_mock, precio_mock, stock_mock)

        mock_agregar_libro.assert_called_once_with("Libro Test", "Autor Test", "Género Test", 29.99, 10)
        mock_showinfo.assert_called_once_with("Éxito", "El libro se añadió correctamente.")
        ventana_mock.destroy.assert_called_once()
        mock_showerror.assert_not_called()

    @patch("tkinter.messagebox.showerror")
    def test_confirmar_agregar_valores_invalidos(self, mock_showerror):
        ventana_mock = MagicMock()
        titulo_mock = MagicMock()
        autor_mock = MagicMock()
        genero_mock = MagicMock()
        precio_mock = MagicMock()
        stock_mock = MagicMock()

        precio_mock.get.return_value = "precio_invalido"
        stock_mock.get.return_value = "stock_invalido"

        confirmar_agregar(ventana_mock, titulo_mock, autor_mock, genero_mock, precio_mock, stock_mock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        ventana_mock.destroy.assert_not_called()

    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("app.models.editar_libro")
    def test_confirmar_editar_exitoso(self, mock_editar_libro, mock_showerror, mock_showinfo):
        ventana_mock = MagicMock()
        id_libro_mock = MagicMock()
        nuevo_titulo_mock = MagicMock()
        nuevo_autor_mock = MagicMock()
        nuevo_genero_mock = MagicMock()
        nuevo_precio_mock = MagicMock()
        nuevo_stock_mock = MagicMock()

        id_libro_mock.get.return_value = "1"
        nuevo_precio_mock.get.return_value = "39.99"
        nuevo_stock_mock.get.return_value = "5"

        confirmar_editar(ventana_mock, id_libro_mock, nuevo_titulo_mock, nuevo_autor_mock, nuevo_genero_mock, nuevo_precio_mock, nuevo_stock_mock)

        mock_editar_libro.assert_called_once_with(1, nuevo_titulo_mock.get(), nuevo_autor_mock.get(), nuevo_genero_mock.get(), 39.99, 5)
        mock_showinfo.assert_called_once_with("Éxito", "El libro se ha editado correctamente.")
        ventana_mock.destroy.assert_called_once()
        mock_showerror.assert_not_called()

    @patch("sqlite3.connect")
    def test_eliminar_libro(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn

        eliminar_libro(1)

        mock_cursor.execute.assert_called_once_with("DELETE FROM libro WHERE id_libro = ?", (1,))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    @patch("app.models.eliminar_libro")
    @patch("app.models.obtener_libros")
    def test_confirmar_eliminar_exitoso(self, mock_obtener_libros, mock_eliminar_libro, mock_showerror, mock_showinfo):
        ventana_mock = MagicMock()
        id_libro_mock = MagicMock()
        id_libro_mock.get.return_value = "1"

        mock_obtener_libros.return_value = [(1, "Libro Prueba")]

        confirmar_eliminar(ventana_mock, id_libro_mock)

        mock_eliminar_libro.assert_called_once_with(1)
        mock_showinfo.assert_called_once_with("Eliminar Libro", "El libro con ID 1 ha sido eliminado.")
        ventana_mock.destroy.assert_called_once()
        mock_showerror.assert_not_called()

    @patch("tkinter.messagebox.showerror")
    @patch("app.models.obtener_libros")
    def test_confirmar_eliminar_libro_no_existe(self, mock_obtener_libros, mock_showerror):
        ventana_mock = MagicMock()
        id_libro_mock = MagicMock()
        id_libro_mock.get.return_value = "99"

        mock_obtener_libros.return_value = [(1, "Libro Prueba")]

        confirmar_eliminar(ventana_mock, id_libro_mock)

        mock_showerror.assert_called_once_with("Error", "No se encontró un libro con ID 99.")
        ventana_mock.destroy.assert_not_called()

if __name__ == '__main__':
    unittest.main()
