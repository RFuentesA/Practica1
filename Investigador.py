from Usuario import Usuario
from Equipo import Equipo
from FechaHora import *
from Solicitud import Solicitud
import json
from Direccion import *

class investigador(Usuario):
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

    def generarSolicitud(self, Solicitud):
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

        solicitudes = Solicitud(nombreInvestigador, tipo, equipo, fechahora, estado)

        if isinstance(solicitudes, Solicitud):
            self.__listaSolicitudes.append(solicitudes)
            print("Solicitud creada y agregada con exito")
        else:
            print("Ha ocurrido un error en el proceso")

    def generarInventario(self, lista, nombreArchivo):
        with open(nombreArchivo, "w") as archivo:
            for elemento in lista:
                archivo.write(f"{elemento}\n")
        print(f"Lista guardada correctamente como: {nombreArchivo}")
    
    def verSolicitudes(self):
        nombreInvestigador = self.__nombre
        numeroPlaca = int(input("Ingrese el numero de placa del Equipo: "))

        """resultadoBusqueda = Solicitud.buscarSolicitud(nombreInvestigador, numeroPlaca)"""

            
    if resultadoBusqueda != None:
        with open("archivoSolicitudes.json", "w") as archivo:
            json.dump(resultadoBusqueda.paraDictar(), archivo)
        
        print("El objeto ha sido guardado con exito")

    else:
        print("La solicitud se encuentra vacia ")
    
    with open("archivoSolicitudes.json", "r") as archivo:
        data = 

    def __str__(self):
            return "Objeto creado :)"


            
        
