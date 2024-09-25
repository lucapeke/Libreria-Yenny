from usuario import Usuario

class Gerente(Usuario):
    def __init__(self, nombre_usuario, contrasena, nombre, apellido, dni):
        super().__init__(nombre_usuario, contrasena, "Gerente") 
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def ver_inventario(self, inventario):
        print("Inventario actual:")
        for libro in inventario:
            print(f"- {libro.titulo} por {libro.autor} (${libro.precio})")

    def modificar_inventario(self, inventario, libro_nuevo):
        inventario.append(libro_nuevo)
        print(f"Libro '{libro_nuevo.titulo}' añadido al inventario.")
