from Usuario import *
from Equipo import *
from FechaHora import *

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

        for pcs in range(self.__listaEquipos):
            if isinstance(self.__listaEquipos[pcs], Equipo):
                if self.__listaEquipos[pcs].getNumeroPlaca() != equipo:
                    print("Error: equipo no existe")
            else:
                equipo = pcs
        
        print("ingrese la fecha que realizo la solicitud: ")
        dd = input("Ingrese el dia: ")
        mm = input("Ingrese el mes: ")
        aa = input("Ingrese el año: ")
        fechita = Fecha(dd, mm, aa)

        print("Ingrese la hora que realizo la solicitud: ")
        hh = input("Ingrese hora: ")
        nn = input("Ingrese minuto: ")
        ss = input("Ingrese segundo: ")
        horita = Hora(hh, nn, ss)

        fechahora = FechaHora(fechita, horita)

        soli = Solicitud(nombreInvestigador, tipo, equipo, fechahora, estado)

        while isinstance(soli, Solicitud):
            Solicitudes.append(soli)
            break


            
        