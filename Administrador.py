from Usuario import *
from Equipo import *
from FechaHora import *
from Solicitud import *
from Investigador import *

class Administrador(Usuario):
    def __init__(self, nombre, id, fechaNacimiento, ciudadNacimiento, telefono, email, dir, contraseña, inventario = None):
        super().__init__(nombre, id, fechaNacimiento, ciudadNacimiento,telefono, email, dir)
        self.__contraseña = contraseña
        self.__inventario = inventario if inventario is not None else []
    
    """Registrar Nuevos usuarios, cambiar contraseñas, eliminar usuarios, Solicitudes de nuevo equipo, Lo mismo para eliminar equipo"""
    """Generar txt segun el investigador y txt de todos los investigadores ordenado de menor a mayor segun la placa"""
    """txt´s de control de cambios, solicitudes agregar y eliminar"""   