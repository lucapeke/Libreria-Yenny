from usuario import Usuario

class Empleado(Usuario):
    def init(self, nombre_usuario, contraseña, nombre, apellido, dni, id_empleado):
        super().init(nombre_usuario, contraseña, "Empleado")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.id_empleado = id_empleado

    # Función para ver inventario
    def ver_inventario(self, inventario):
        print("Inventario actual:")
        for libro in inventario:
            print(f"- {libro.titulo} por {libro.autor} (${libro.precio})")