from Usuario import *
from Equipo import *
from FechaHora import *
from Solicitud import *
from Investigador import *

class Administrador(Usuario):
    def __init__(self, nombre, id, ciudadNacimiento, telefono, email, contraseña, inventario = None):
        """super().__init__(nombre, id, fechaNacimiento, ciudadNacimiento,telefono, email, dir)"""
        self.__nombre = nombre
        self.__id = id
        self.__fechaNacimiento = Fecha
        self.__ciudadNacimiento = ciudadNacimiento
        self.__telefono = telefono
        self.__email = email
        self.__dir = Direccion
        self.__contraseña = contraseña
        self.__inventario = inventario if inventario is not None else []
    
    def setInventario(self, inventario):
        self.__inventario = inventario
    
    def getInventario(self):
        return self.__inventario
    
    """Registrar Nuevos usuarios, cambiar contraseñas, eliminar usuarios, Solicitudes de nuevo equipo, Lo mismo para eliminar equipo"""
    """Generar txt segun el investigador y txt de todos los investigadores ordenado de menor a mayor segun la placa"""
    """txt´s de control de cambios, solicitudes agregar y eliminar"""  
    
    def generarInventario(self, lista, nombreArchivo):
        with open(nombreArchivo, "w") as archivo:
            for elemento in lista:
                elemento = elemento.__str__()
                archivo.write(f"{elemento}\n")
        print(f"Lista guardada correctamente como: {nombreArchivo}")
        
    def __str__(self):
                return "Objeto creado :)"