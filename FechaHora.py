from Fecha import *
from Hora import *

class FechaHora(Fecha, Hora):
    def __init__(self, dd, mm, aa, hh, nn, ss):
        super().__init__(dd, mm, aa, hh, nn, ss)
    
    def getDia(self):
        return self.__dia
    
    def setDia(self, dd):
        self.__dia = dd
    
    def getMes(self):
        return self.__mes

    def setMes(self, mm):
        self.__mes = mm
    
    def getAño(self):
        return self.__año
    
    def setAño(self, aa):
        self.__año = aa
    
    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minuto
    
    def getSegundo(self):
        return self.__segundo
    
    def setHora(self, hh):
        self.__hora = hh
        
    def setMinuto(self, nn):
        self.__minuto = nn
        
    def setSegundo(self, ss):
        self.__segundo = ss