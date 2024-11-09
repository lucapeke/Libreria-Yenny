import unittest
from unittest.mock import patch, MagicMock
from tkinter import messagebox


from app.models import (
    iniciar_sesion,
    registrar_usuario,
    on_register,
    confirmar_agregar,
    confirmar_editar
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
    @patch('tkinter.messagebox.showerror')
    @patch('app.models.registrar_usuario')
    def test_on_register_exitoso(self, mock_registrar_usuario, mock_showerror):
        mock_ventana = MagicMock()
        mock_ventana_login = MagicMock()
        entry_usuario = MagicMock(get=MagicMock(return_value="nuevo_usuario_test"))
        entry_contrasena = MagicMock(get=MagicMock(return_value="Contrasena123"))
        entry_rol = MagicMock(get=MagicMock(return_value="empleado"))
        entry_nombre = MagicMock(get=MagicMock(return_value="Juan"))
        entry_apellido = MagicMock(get=MagicMock(return_value="Perez"))
        entry_dni = MagicMock(get=MagicMock(return_value="12345678"))

        on_register(mock_ventana, mock_ventana_login, entry_usuario, entry_contrasena, entry_rol,
                    entry_nombre, entry_apellido, entry_dni)

        mock_registrar_usuario.assert_called_once_with(
            "nuevo_usuario_test", "Contrasena123", "empleado", "Juan", "Perez", "12345678"
        )
        mock_ventana.destroy.assert_called_once()
        mock_ventana_login.deiconify.assert_called_once()

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.registrar_usuario')
    def test_on_register_dni_no_numerico(self, mock_registrar_usuario, mock_showerror):
        entry_dni = MagicMock(get=MagicMock(return_value="DNI12345"))
        
        on_register(MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), entry_dni)

        mock_showerror.assert_called_once_with("Error", "El DNI debe contener solo números.")
        mock_registrar_usuario.assert_not_called()  

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.registrar_usuario')
    def test_on_register_contrasena_invalida(self, mock_registrar_usuario, mock_showerror):
        entry_contrasena = MagicMock(get=MagicMock(return_value="abc123"))
        
        on_register(MagicMock(), MagicMock(), MagicMock(), entry_contrasena, MagicMock(), MagicMock(), MagicMock(), MagicMock())

        mock_showerror.assert_called_once_with("Error", "La contraseña debe tener al menos 6 caracteres y una letra mayúscula.")
        mock_registrar_usuario.assert_not_called()  

    @patch('tkinter.messagebox.showinfo')
    @patch('app.models.agregar_libro')
    @patch('app.models.nav_gestionar_inventario')
    def test_confirmar_agregar_exitoso(self, mock_nav_gestionar_inventario, mock_agregar_libro, mock_showinfo):
        titulo = MagicMock(get=MagicMock(return_value="Libro de Prueba"))
        autor = MagicMock(get=MagicMock(return_value="Autor Prueba"))
        genero = MagicMock(get=MagicMock(return_value="Ficción"))
        precio = MagicMock(get=MagicMock(return_value="19.99"))
        stock = MagicMock(get=MagicMock(return_value="10"))

        mock_ventana = MagicMock()

        confirmar_agregar(mock_ventana, titulo, autor, genero, precio, stock)

        mock_agregar_libro.assert_called_once_with(
            "Libro de Prueba", "Autor Prueba", "Ficción", 19.99, 10
        )

        mock_showinfo.assert_called_once_with("Éxito", "El libro se añadió correctamente.")
        
        mock_nav_gestionar_inventario.assert_called_once_with(mock_ventana)

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.agregar_libro')
    def test_confirmar_agregar_error_precio_no_numerico(self, mock_agregar_libro, mock_showerror):
        precio = MagicMock(get=MagicMock(return_value="no_numérico"))
        stock = MagicMock(get=MagicMock(return_value="10"))

        confirmar_agregar(MagicMock(), MagicMock(), MagicMock(), MagicMock(), precio, stock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        mock_agregar_libro.assert_not_called()  

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.agregar_libro')
    def test_confirmar_agregar_error_stock_no_numerico(self, mock_agregar_libro, mock_showerror):
        precio = MagicMock(get=MagicMock(return_value="19.99"))
        stock = MagicMock(get=MagicMock(return_value="no_numérico"))

        confirmar_agregar(MagicMock(), MagicMock(), MagicMock(), MagicMock(), precio, stock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        mock_agregar_libro.assert_not_called()  

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.agregar_libro')
    def test_confirmar_agregar_error_precio_y_stock_no_numerico(self, mock_agregar_libro, mock_showerror):
        precio = MagicMock(get=MagicMock(return_value="no_numérico"))
        stock = MagicMock(get=MagicMock(return_value="no_numérico"))

        confirmar_agregar(MagicMock(), MagicMock(), MagicMock(), MagicMock(), precio, stock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        mock_agregar_libro.assert_not_called()  

    @patch('tkinter.messagebox.showinfo')
    @patch('app.models.editar_libro')
    @patch('app.models.nav_gestionar_inventario')
    def test_confirmar_editar_exitoso(self, mock_nav_gestionar_inventario, mock_editar_libro, mock_showinfo):
        id_libro = 1  
        nuevo_titulo = MagicMock(get=MagicMock(return_value="Nuevo Título"))
        nuevo_autor = MagicMock(get=MagicMock(return_value="Nuevo Autor"))
        nuevo_genero = MagicMock(get=MagicMock(return_value="Nuevo Género"))
        nuevo_precio = MagicMock(get=MagicMock(return_value="29.99"))
        nuevo_stock = MagicMock(get=MagicMock(return_value="20"))

        mock_ventana = MagicMock()

        confirmar_editar(mock_ventana, id_libro, nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_precio, nuevo_stock)

        mock_editar_libro.assert_called_once_with(
            1, "Nuevo Título", "Nuevo Autor", "Nuevo Género", 29.99, 20
        )

        mock_showinfo.assert_called_once_with("Éxito", "El libro se ha editado correctamente.")
        
        mock_nav_gestionar_inventario.assert_called_once_with(mock_ventana)

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.editar_libro')
    def test_confirmar_editar_error_precio_no_numerico(self, mock_editar_libro, mock_showerror):
        nuevo_precio = MagicMock(get=MagicMock(return_value="no_numérico"))
        nuevo_stock = MagicMock(get=MagicMock(return_value="20"))

        confirmar_editar(MagicMock(), 1, MagicMock(), MagicMock(), MagicMock(), nuevo_precio, nuevo_stock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        mock_editar_libro.assert_not_called()  

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.editar_libro')
    def test_confirmar_editar_error_stock_no_numerico(self, mock_editar_libro, mock_showerror):
        nuevo_precio = MagicMock(get=MagicMock(return_value="29.99"))
        nuevo_stock = MagicMock(get=MagicMock(return_value="no_numérico"))

        confirmar_editar(MagicMock(), 1, MagicMock(), MagicMock(), MagicMock(), nuevo_precio, nuevo_stock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        mock_editar_libro.assert_not_called()  

    @patch('tkinter.messagebox.showerror')
    @patch('app.models.editar_libro')
    def test_confirmar_editar_error_precio_y_stock_no_numerico(self, mock_editar_libro, mock_showerror):
        nuevo_precio = MagicMock(get=MagicMock(return_value="no_numérico"))
        nuevo_stock = MagicMock(get=MagicMock(return_value="no_numérico"))

        confirmar_editar(MagicMock(), 1, MagicMock(), MagicMock(), MagicMock(), nuevo_precio, nuevo_stock)

        mock_showerror.assert_called_once_with("Error", "Por favor, ingrese valores numéricos válidos para el Precio y el Stock.")
        mock_editar_libro.assert_not_called()  

if __name__ == '__main__':
    unittest.main()
