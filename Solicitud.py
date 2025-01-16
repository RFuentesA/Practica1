from Equipo import *
from FechaHora import *
from Investigador import *

class Solicitud():
    def __init__(self, nombreInvestigador, tipo, estado, listaSolicitudes = []):
        self.__nombreInvestigador = nombreInvestigador
        self.__tipo = tipo
        self.__equipo = Equipo
        self.__fechaSolicitud = FechaHora
        self.__estado = estado
        self.__listaSolicitudes = listaSolicitudes
    
    def getNombreInvestigador(self):
        return self.__nombreInvestigador
    
    def setNombreInvestigador(self, nombreInvestigador):
        self.__nombreInvestigador = nombreInvestigador
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def getEquipo(self):
        return Equipo
    
    def getFechaSolicitud(self):
        return FechaHora
    
    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado
    
    def getListaSolicitudes(self):
        return self.__listaSolicitudes
    
    def setListaSolicitudes(self, listaSolicitudes):
        self.__listaSolicitudes = listaSolicitudes
    
    def paraDictar(self): #Creamos el diccionario que contenga los atributos de las solicitudes.
        return {"nombreInvestigador": self.__nombreInvestigador, "Tipo": self.__tipo, "Equipo": self.__equipo, "FechaSolicitud": self.__fechaSolicitud, "Estado": self.__estado}
    
    @classmethod
    def delDiccionario(cls, data): #Método que convierte el objeto en un diccionario.
        return cls(data["nombreInvestigador"], data["Tipo"], data["Equipo"], data["FechaSolicitud"], data["Estado"])
    
    def buscarSolicitud(self, nombreInvestigador, numeroPlaca): #Método para buscar la solicitud.
        for solicitudBuscada in self.__listaSolicitudes: #Iteramos en la lista de las solicitudes y hacemos la comparación 
            if solicitudBuscada.getNombreInvestigador() == nombreInvestigador and solicitudBuscada.getNumeroPlaca() == numeroPlaca:
                return solicitudBuscada #Al encontrar la solicitud o solicitudes retornamos dicha solicitud
        return None #De lo contrario retornamos vacio.
    
    def ejecutarSolicitud(self, inventarioGlobal):
        idInvestigador = investigador.getId()
        tipoSolicitud = self.getTipo()
        equipo = self.getEquipo()

        if idInvestigador not in inventarioGlobal:
            print("El investigador no tiene su inventario registrado")
        
        inventario = inventarioGlobal[idInvestigador]

        if tipoSolicitud == "Agregar Equipo":
            if equipo is None:
                print("No se puede agregar algo vacio")
            if equipo in inventario:
                print("El equipo ya pertenece al inventario.")
            inventario.append(equipo)
            print(f"Equipo: {equipo} se ha agregado exitosamente al inventario del investigador: {idInvestigador}. ")
        
        elif tipoSolicitud == "Eliminar equipo":
            if equipo not in inventario:
                print("El equipo no esta en el inventario. ")
            inventario.remove(equipo)
            print(f"Equipo: {equipo} eliminado del inventario del investigador: {idInvestigador}. ")
        
        else:
            print("Tipo de solicitud desconocido. ")
        
        self.setEstado("Cumplida")
            
