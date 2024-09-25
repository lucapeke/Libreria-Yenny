from usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre_usuario, contrasena, nombre, apellido, dni, id_empleado):
        super().__init__(nombre_usuario, contrasena, "Empleado") 
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.id_empleado = id_empleado

    # Función para ver inventario
    def ver_inventario(self, inventario):
        print("Inventario actual:")
        for libro in inventario:
            print(f"- {libro.titulo} por {libro.autor} (${libro.precio})")
