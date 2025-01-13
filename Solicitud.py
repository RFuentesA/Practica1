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
    
    def buscarSolicitud(self, nombreInvestigador, numeroPlaca):
        

            
