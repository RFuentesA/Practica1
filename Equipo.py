from Usuario import Usuario
from Fecha import Fecha
class Equipo():
    def __init__(self, nombre, numeroPlaca, valorCompra):
        self.__nombre = nombre
        self.__numeroPlaca = numeroPlaca
        self.__fechaCompra = Fecha
        self.__valorCompra = valorCompra
        self.__EmpAsociado = Usuario
    
    def setNombre(self, n):
        self.__nombre = n
    
    def setNumeroPlaca(self, np):
        self.__numeroPlaca = np
    
    def setFechaCompra(self, Fecha):
        self.__fechaCompra = Fecha
        
    def setValorCompra(self, vc):
        self.__valorCompra = vc
        
    def setEmpAsociado(self, Usuario):
        self.__EmpAsociado = Usuario
        
    def getNombre(self):
        return self.__nombre
    
    def getNumeroPlaca(self):
        return self.__numeroPlaca
    
    def getFechaCompra(self):
        return self.__fechaCompra
    
    def getValorCompra(self):
        return self.__valorCompra
    
    def getEmpAsociado(self):
        return self.__EmpAsociado