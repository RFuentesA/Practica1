from Usuario import *
from Equipo import *
from Fecha import *
from Hora import *

class investigador(Usuario):
    def __init__(self, nombre, id, fechaNacimiento, ciudadNacimiento, telefono, email, dir, inventario = None):
        super().__init__(nombre, id, fechaNacimiento, ciudadNacimiento,telefono, email, dir)
        self.__inventario = inventario if inventario is not None else [] 
    
    def setInventario(self, inventario):
        self.__inventario = inventario
    
    def getInventario(self):
        return self.__inventario

    def generarSolicitud(Solicitud):
        nombreInvestigador = input("Ingrese su nombre: ")
        tipo = input("Ingrese (Agregar Equipo) si desea adicionar un equipo a su inventario o (Quitar Equipo) si desea eliminar un equipo de su inventario: ")
        equipo = int(input("Ingrese el numero de placa de su Equipo: "))
        estado = input("Escriba (Pendiente): ")

        for pc in listaEquipos:
            if pc.getNumeroPlaca() != equipo:
                print("Error: equipo no existe")
            else:
                equipo = pc
        
        print("ingrese la fecha que realizo la solicitud: ")
        dd = input("Ingrese el dia: ")
        mm = input("Ingrese el mes: ")
        aa = input("Ingrese el año: ")
        fechaSolictud = Fecha(dd, mm, aa)

        print("Ingrese la hora que realizo la solicitud: ")
        hh = input("Ingrese hora: ")
        nn = input("Ingrese minuto: ")
        ss = input("Ingrese segundo: ")
        horaSolicitud = Hora(hh, nn, ss)
            
        