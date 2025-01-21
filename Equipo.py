from Usuario import Usuario
from Fecha import Fecha

#listaEquipos = []
class Equipo():
        
    def __init__(self, nombre, numeroPlaca, valorCompra):
        self.__nombre = nombre
        self.__numeroPlaca = numeroPlaca
        self.__fechaCompra = Fecha
        self.__valorCompra = valorCompra
        self.__empAsociado = Usuario
        #listaEquipos.append(self)
 

    def setNombre(self, n):
        self.__nombre = n
    
    def setNumeroPlaca(self, np): 
        self.__numeroPlaca = np
    
    def setFechaCompra(self, Fecha):
        self.__fechaCompra = Fecha
        
    def setValorCompra(self, vc):
        self.__valorCompra = vc
        
    def setEmpAsociado(self, Usuario):
        self.__empAsociado = Usuario
        
    def getNombre(self):
        return self.__nombre
    
    def getNumeroPlaca(self):
        return self.__numeroPlaca
    
    def getFechaCompra(self):
        return self.__fechaCompra
    
    def getValorCompra(self):
        return self.__valorCompra
    
    def getEmpAsociado(self):
        return self.__empAsociado
    
    def setEmpAsociado(self, Usuario):
        self.__empAsociado = Usuario
    
    #def getListaEquipos(self):
        #return self.__listaEquipos 
    
    
    def __str__(self):
        return str(self.__nombre) +" "+ str(self.__numeroPlaca) +" "+ str(self.__fechaCompra) +" "+ str(self.__valorCompra)