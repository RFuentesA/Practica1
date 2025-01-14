from Investigador import *;from Direccion import *; from Equipo import *;from FechaHora import *
from Fecha import *; from Hora import *; from List import *; from ListaDoble import *;from Nodo import *; from NodoDoble import*
from Solicitud import *;from Usuario import *; from Administrador import *

#Cargue de empleados
emp = List(None,None,0)
with open("Textos/Empleados.txt", "r") as empleados:
    for i in empleados:
        x = i.split(",")
        xi = x[6].strip()
        x.pop()
        x.append(xi)
        emp.addLast(x)

#Cargue de contraseñas
pss = List(None,None,0)
with open("Textos/Password.txt", "r") as contraseñas:
    for i in contraseñas:
        x = i.split()
        pss.addLast(x)
    
print("*** Bienvenido al sistema ***")
NumId = input("ID: ")
contra = input("Contraseña: ")

#menu de opciones
def OpcionesInvestigador():
    print("***********MENU***********")
    print("1.txt inventario")
    print("2.Adicionar equipo")
    print("3.Eliminar equipo")
    print("4.txt Estado Solicitudes")
    op = int(input())
    if op == 1:
        n = IV.getNombre()
        id = str(IV.getId())
        IV.generarInventario(IV.getInventario(), n + " " + id)
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        pass
        
    else:
        print("Opcion incorrecta")

def OpcionesAdministrador():
    print("***********MENU***********")
    print("1.txt inventario")
    print("2.Agregar usuario")
    print("3.Eliminar usuario")
    print("4.Cambiar contraseña")
    print("5.Solicitudes Agregar equipo")
    print("6.Solicitudes Eliminar equipo")
    print("7.Inventario segun investigador(txt)")
    print("8.Inventario general(txt)")
    print("9.Control de cambios(txt)")
    print("10.Solicitudes agregar(txt)")
    print("11.Solicitudes eliminar(txt)")
    op = int(input())
    if op == 1:
        n = AD.getNombre()
        id = str(AD.getId())
        AD.generarInventario(AD.getInventario(), n + " " + id)
    elif op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        pass
    elif op == 9:
        pass
    elif op == 10:
        pass
    elif op == 11:
        pass
    else:
        print("Opcion incorrecta")
    
#apuntadores para la sesion iniciada, investigador o admin
IV = None
AD = None

#Ciclo para verificar id y contraseña ingresados vf = verificacion
vf = False
temp = pss.First()
while temp != None and temp.getNext() != None:
    if temp.getData()[0] == NumId and temp.getData()[1] == contra:
        vf = True
        #en caso de investigador relaciono id de la contraseña con id en la lista de empleados
        if temp.getData()[2] == "investigador":
            temp1 = emp.First()
            while temp1 != None and temp1.getNext() != None:
                #creacion objeto Investigador
                if temp.getData()[0] == temp1.getData()[1]:
                    IV = investigador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                    j = temp1.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    IV.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = temp1.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    IV.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    print("empleado encontrado", IV)
                    OpcionesInvestigador()
                    
                    
                temp1 = temp1.getNext()
            #tail de la lista de empleados
            #Creación de objeto investigador
            if temp.getData()[0] == temp1.getData()[1]:
                    IV = investigador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                    j = temp1.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    IV.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = temp1.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    IV.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    print("empleado encontrado", IV)
                    OpcionesInvestigador()
        
        #en caso de Administrador relaciono id de la contraseña con id en la lista de empleados
        if temp.getData()[2] == "administrador":
            temp1 = emp.First()
            while temp1 != None and temp1.getNext() != None:
                #Creacion objeto administrador
                if temp.getData()[0] == temp1.getData()[1]:
                    AD = Administrador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                    j = temp1.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    AD.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = temp1.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    AD.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    print("Admin encontrado", AD)
                    OpcionesAdministrador()
                temp1 = temp1.getNext()
            #tail lista empleados
            if temp.getData()[0] == temp1.getData()[1]:
                    AD = Administrador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                    j = temp1.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    AD.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = temp1.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    AD.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    print("Admin encontrado", AD)
                    OpcionesAdministrador()
    temp = temp.getNext()
    
#este es el tail de la lista de contraseña
if temp.getData()[0] == NumId and temp.getData()[1] == contra:
    vf = True
    
    #en caso de investigador 
    if temp.getData()[2] == "investigador":
            temp1 = emp.First()
            while temp1 != None and temp1.getNext() != None:
                #Creación de objeto investigador
                if temp.getData()[0] == temp1.getData()[1]:
                    IV = investigador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                    j = temp1.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    IV.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = temp1.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    IV.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    print("empleado encontrado", IV)
                    OpcionesInvestigador()
                     
                    
                temp1 = temp1.getNext()
            #tail de la lista de empleados
            #Creación de objeto investigador
            if temp.getData()[0] == temp1.getData()[1]:
                    IV = investigador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                    j = temp1.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    IV.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = temp1.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    IV.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    print("empleado encontrado", IV)
                    OpcionesInvestigador()
    
    #en caso de Administrador relaciono id de la contraseña con id en la lista de empleados
    if temp.getData()[2] == "administrador":
        temp1 = emp.First()
        while temp1 != None and temp1.getNext() != None:
            #Creacion objeto administrador
            if temp.getData()[0] == temp1.getData()[1]:
                AD = Administrador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                j = temp1.getData()[2].split()
                dd = j[0]
                mm = j[1]
                aa = j[2]
                AD.setFechaNacimiento(Fecha(dd,mm,aa))
                k = temp1.getData()[6].split()
                calle = k[0]
                nomn = k[1]
                brr = k[2]
                ciudad = k[3]
                edfc = k[4]
                apto = k[5]
                AD.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                print("Admin encontrado", AD)
                OpcionesAdministrador()
            temp1 = temp1.getNext()
        #tail lista empleados
        if temp.getData()[0] == temp1.getData()[1]:
                AD = Administrador(str(temp1.getData()[0]),int(temp1.getData()[1]),None,str(temp1.getData()[3]),int(temp1.getData()[4]),str(temp1.getData()[5]),None,)
                j = temp1.getData()[2].split()
                dd = j[0]
                mm = j[1]
                aa = j[2]
                AD.setFechaNacimiento(Fecha(dd,mm,aa))
                k = temp1.getData()[6].split()
                calle = k[0]
                nomn = k[1]
                brr = k[2]
                ciudad = k[3]
                edfc = k[4]
                apto = k[5]
                AD.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                print("Admin encontrado", AD)
                OpcionesAdministrador()

if vf == False: 
    print("Acceso incorrecto")