from empleado import Empleado
from gerente import Gerente
from inventario import inventario
from libro import Libro

# Crear usuarios
empleado1 = Empleado("Juan123", "pass123", "Juan", "Pérez", "12345678", 101)
gerente1 = Gerente("Ana456", "admin123", "Ana", "Gómez", "87654321")

# Simular inicio de sesión del empleado
if empleado1.iniciar_sesion("Juan123", "pass123"):
    empleado1.ver_inventario(inventario)

# Simular inicio de sesión del gerente
if gerente1.iniciar_sesion("Ana456", "admin123"):
    gerente1.ver_inventario(inventario)
    nuevo_libro = Libro(4, "Don Quijote", "Miguel de Cervantes", "Clásico", 30.0)
    gerente1.modificar_inventario(inventario, nuevo_libro)

empleado1.ver_inventario(inventario)