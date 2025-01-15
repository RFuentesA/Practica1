from Usuario import Usuario
from Equipo import Equipo
from FechaHora import *
from Solicitud import Solicitud
import json
from Direccion import *

class investigador(Usuario):
    def __init__(self, nombre, id, ciudadNacimiento, telefono, email, contraseña, inventario = None):
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
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def setFechaNacimiento(self, Fecha):
        self.__fechaNacimiento = Fecha
        
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
            
    def getDir(self):
        return self.__dir
    
    def setDir(self, Direccion):
        self.__dir = Direccion
    
    def getPss(self):
        return self.__contraseña

    def generarSolicitud(self):
        nombreInvestigador = input("Ingrese su nombre: ")
        tipo = input("Ingrese (Agregar Equipo) si desea adicionar un equipo a su inventario o (Quitar Equipo) si desea eliminar un equipo de su inventario: ")
        equipo = int(input("Ingrese el numero de placa de su Equipo: "))
        estado = input("Escriba (Pendiente): ")

        for pcs in range(self.__listaEquipos):
            if isinstance(self.__listaEquipos[pcs], Equipo):
                if self.__listaEquipos[pcs].getNumeroPlaca() == equipo:
                    equipo = pcs
            else:
                print("El equipo buscado no se encuentra.")
        
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
                elemento = elemento.__str__()
                archivo.write(f"{elemento}\n")
        print(f"Lista guardada correctamente como: {nombreArchivo}")
    
    def verSolicitudes(self): #Método para mostrar las solicitudes que tenga el investigador.
        nombreInvestigador = self.__nombre #Damos el nombre del investigador.
        numeroPlaca = int(input("Ingrese el numero de placa del Equipo: ")) #El investigador ingresa el numero de su equipo.

        resultadoBusqueda = Solicitud.buscarSolicitud(nombreInvestigador, numeroPlaca) #Variable que llama al método de la clase Solicitud y luego esta apunta a una instancia de la clase Solicitud.
          
        if resultadoBusqueda != None: #Verificamos que lo que hayamos pasado no este vacio.
            with open("archivoSolicitudes.json", "w") as archivo: 
                json.dump(resultadoBusqueda.paraDictar(), archivo) #Usamos a JSON para guardar el objeto como un diccionario.
            print("El objeto ha sido guardado con exito")
        else:
            print("La solicitud se encuentra vacia ")
    
        with open("archivoSolicitudes.json", "r") as archivo: #Luego leemos el archivo
            data = json.load(archivo) 
    
        leerSolicitud = Solicitud.delDiccionario(data) #Usando el método delDiccionario reconstruimos el objeto desde el diccionario creado anteriormente.
        print("Ya puede visualizar la solicitud. ")
        print(leerSolicitud) #El investigador ya puede leer sus solicitudes.

    def __str__(self):
        return str(self.__nombre)+","+str(self.__id)+","+str(self.getFechaNacimiento())+","+str(self.__ciudadNacimiento)+","+str(self.__telefono)+","+str(self.__email)+","+str(self.getDir())