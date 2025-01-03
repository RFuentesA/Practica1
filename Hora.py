class Hora():
    def __init__(self, hh, mm, ss):
        self.__hora = hh
        self.__minuto = mm
        self.__segundo = ss
    
    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minuto
    
    def getSegundo(self):
        return self.__segundo
    
    def setHora(self, hh):
        self.__hora = hh
        
    def setMinuto(self, mm):
        self.__minuto = mm
        
    def setSegundo(self, ss):
        self.__segundo = ss
    
    def __str__(self):
        return str(self.__hora) + " " + str(self.__minuto) + " " + str(self.__segundo)