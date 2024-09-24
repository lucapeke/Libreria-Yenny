from usuario import Usuario

class Gerente(Usuario):
    def init(self, nombre_usuario, contraseña, nombre, apellido, dni):
        super().init(nombre_usuario, contraseña, "Gerente")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    # Función para modificar el inventario
    def modificar_inventario(self, inventario, nuevo_libro):
        inventario.append(nuevo_libro)
        print(f"Libro '{nuevo_libro.titulo}' añadido al inventario.")