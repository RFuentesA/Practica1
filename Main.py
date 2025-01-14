from Administrador import *; from Investigador import *;from Direccion import *; from Equipo import *;from FechaHora import *
from Fecha import *; from Hora import *; from List import *; from ListaDoble import *;from Nodo import *; from NodoDoble import*
from Solicitud import *;from Usuario import *

#Cargue de empleados
emp = List(None,None,0)
with open("Textos/Empleados.txt", "r") as empleados:
    for i in empleados:
        x = i.split(",")
        xi = x[6].strip()
        x.pop()
        x.append(xi)
        emp.addLast(x)

temp = emp.First()
while temp != None and temp.getNext() != None:
    print (temp.getData())
    temp = temp.getNext()
print(temp.getData())

#Cargue de contraseñas
pss = List(None,None,0)
with open("Textos/Password.txt", "r") as contraseñas:
    for i in contraseñas:
        x = i.split()
        pss.addLast(x)
    
"""temp = pss.First()
while temp != None and temp.getNext() != None:
    print (temp.getData())
    temp = temp.getNext()
print(temp.getData())"""

print("*** Bienvenido al sistema ***")
NumId = input("ID: ")
contra = input("Contraseña: ")

#apuntadores para la sesion iniciada, investigador o admin
IV = None

#Ciclo para verificar id y contraseña ingresados vf = verificacion
temp = pss.First()
vf = False
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
                    
    temp = temp.getNext()
    
#este es el tail de la lista de contraseña
if temp.getData()[0] == NumId and temp.getData()[1] == contra:
    vf = True
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
    

if vf == False: 
    print("Acceso incorrecto")