# usuario.py
class Usuario:
    def __init__(self, nombre_usuario, contraseña, rol):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.rol = rol

    def iniciar_sesion(self, nombre_usuario, contraseña):
        if self.nombre_usuario == nombre_usuario and self.contraseña == contraseña:
            print(f"Inicio de sesión exitoso para {self.nombre_usuario} como {self.rol}.")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False