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
        self.__inventarioGlobal = {}
    
    def setInventario(self, inventario):
        self.__inventario = inventario
    
    def getInventario(self):
        return self.__inventario
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def setFechaNacimiento(self, Fecha):
        self.__fechaNacimiento = Fecha
        
    def getDir(self):
        return self.__dir
    
    def setDir(self, Direccion):
        self.__dir = Direccion
        
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
        
    def getPss(self):
        return self.__contraseña
    
    def getNombre (self):
        return self.__nombre
    
    def getInventarioGlobal(self):
        return self.__inventarioGlobal
    
    """Registrar Nuevos usuarios, cambiar contraseñas, eliminar usuarios, Solicitudes de nuevo equipo, Lo mismo para eliminar equipo"""
    """Generar txt segun el investigador y txt de todos los investigadores ordenado de menor a mayor segun la placa"""
    """txt´s de control de cambios, solicitudes agregar y eliminar"""  
    #Métodos lista global
    def registrarInventarioInvestigador(self, idInvestigador, inventario):
        if idInvestigador in self.__inventarioGlobal:
            print(f"El investigador con ID {idInvestigador} ya tiene un inventario registrado.")
        else:
            print(f"Registrando nuevo inventario para el investigador con ID {idInvestigador}.")
        
        self.__inventarioGlobal[idInvestigador] = inventario
        print(f"Inventario registrado exitosamente.")

    def verInventarioGlobal(self):
        if not self.__inventarioGlobal:
            print("El inventario global esta vacio ")
            return
        print("Inventario Global: ")
        for idInvestigador, inventario in self.__inventarioGlobal.items():
            print(f"Id investigador: {idInvestigador}")
            print(f"Inventario: {inventario}")
    
    def verInventarioInvestigador(self, idInvestigador):
        if idInvestigador in self.__inventarioGlobal:
            print(f"Inventario del investigador: {idInvestigador}")
            print(self.__inventarioGlobal[idInvestigador])
        else:
            print(f"No se encontro un inventario para el investigador {idInvestigador}")

    #Lista de solicitudes 
    
    def generarInventario(self, lista, nombreArchivo):
        with open("Textos/" + nombreArchivo, "w") as archivo:
            for elemento in lista:
                elemento = elemento.__str__()
                archivo.write(f"{elemento}\n")
        print(f"Lista guardada correctamente como: {nombreArchivo}")
    
    def cumplirSolicitud(self, solicitud):
        if not isinstance(solicitud, Solicitud):
            raise TypeError("El objeto proporcionado no es un solicitud valida")
        
        Solicitud.ejecutarSolicitud(self.__inventarioGlobal)
        print(f"La solicitud del tipo {solicitud.getTipo()} ha sido cumplida.")

        with open("Textos/EquiposTodos", "a") as archivo:
            archivo.writelines(f"{solicitud}\n")


        
    def __str__(self):
        return str(self.__nombre)+","+str(self.__id)+","+str(self.getFechaNacimiento())+","+str(self.__ciudadNacimiento)+","+str(self.__telefono)+","+str(self.__email)+","+str(self.getDir())