from Usuario import *
from Equipo import *

class investigador(Usuario):
    def __init__(self, nombre, id, fechaNacimiento, ciudadNacimiento, telefono, email, dir, inventario = None):
        super().__init__(nombre, id, fechaNacimiento, ciudadNacimiento,telefono, email, dir)
        self.__inventario = inventario if inventario is not None else [] 
    
    def setInventario(self, inventario):
        self.__inventario = inventario
    
    def getInventario(self):
        return self.__inventario

    def generarSolicitud(Solicitud):
