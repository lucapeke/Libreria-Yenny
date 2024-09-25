class Usuario:
    def __init__(self, nombre_usuario, contrasena, rol):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol
        
    def iniciar_sesion(self, nombre_usuario, contrasena):
        if self.nombre_usuario == nombre_usuario and self.contrasena == contrasena:
            print(f"Inicio de sesión exitoso para {self.nombre_usuario} como {self.rol}.")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False
