from Usuario import Usuario
from Equipo import Equipo
from FechaHora import *
from Solicitud import Solicitud
import json
from Direccion import *

Ejemplo = Equipo("HpVoltro", 1529, 800000)

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
        self.__inventario = inventario if inventario is not None else [Ejemplo]
       # self.__listaSolicitudes = []
    
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
   
    def getNombre(self):
        return self.__nombre + " "
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setListaSolicitudes(self, lista):
        self.__listaSolicitudes = lista
    
    def getListaSolicitudes(self):
        return self.getListaSolicitudes 

    def generarSolicitud(self, tipoSolicitud, equipo = None):

        nomInves = input("Ingrese su nombre: ")
        dd = input("Ingrese el día de la solicitud: ")
        mm = input("Ingrese el mes de la solicitud: ")
        aa = input("Ingrese el año de la solicitud: ")
        fechita = Fecha(dd, mm, aa)

        hh = input("Ingrese la hora de la solicitud: ")
        nn = input("Ingrese el minuto de la solicitud: ")
        ss = input("Ingrese el segundo de la solicitud: ")
        horita = Hora(hh, nn, ss)
        fechaDeSolicitud = FechaHora(fechita, horita)
        estado = input("Dado que su solicitud es nueva escriba (Pendiente o pendiente): ")

        if tipoSolicitud == "Agregar Equipo":
            solicitudNueva = Solicitud(nomInves, tipoSolicitud, + " " + estado)
            solicitudNueva.setFechaSolicitud(fechaDeSolicitud)
            solicitudNueva.setEquipo(equipo)
            return solicitudNueva
        elif tipoSolicitud == "Eliminar Equipo":
            print("Agregue los datos del equipo que desee eliminar a continuacion. ")
            Ejemplo = Equipo("HpVoltro", 1529, 800000)



        
    def generarInventario(self, lista, nombreArchivo):
        with open("Textos/" + nombreArchivo, "w") as archivo:
            for elemento in lista:
                elemento = elemento.__str__()
                archivo.write(f"{elemento}\n")
        print(f"Lista guardada correctamente como: {nombreArchivo}")
    
    def verSolicitudes(self): #Método para mostrar las solicitudes que tenga el investigador.
        nombreInvestigador = input("Ingrese su nombre: ") #El investigador ingresa su nombre.
        numeroPlaca = int(input("Ingrese el numero de placa del Equipo: ")) #El investigador ingresa el numero de su equipo.

        resultadoBusqueda = Solicitud.buscarSolicitud(self, nombreInvestigador, numeroPlaca) #Variable que llama al método de la clase Solicitud y luego esta apunta a una instancia de la clase Solicitud.
          
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