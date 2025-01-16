from Investigador import *;from Direccion import *; from Equipo import *;from FechaHora import *
from Fecha import *; from Hora import *; from List import *; from ListaDoble import *;from Nodo import *; from NodoDoble import*
from Solicitud import *;from Usuario import *; from Administrador import *

#listadobleusuarios 

ListaTodos= ListaDoble(None, None, 0)

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


def añadidor():
    #ciclo en password para saber si IV o AD
    temp = pss.First()
    while temp != None and temp.getNext() != None:
        if temp.getData()[2] == "investigador":
            #busqueda de id en el txt de empleados 
            idBuscado = temp.getData()[0]
            empleadoT = emp.First()
            while empleadoT != None and (empleadoT == emp.Last() or empleadoT != emp.Last()):
                if idBuscado == empleadoT.getData()[1]:
                    IV = investigador(str(empleadoT.getData()[0]),int(empleadoT.getData()[1]),None,str(empleadoT.getData()[3]),int(empleadoT.getData()[4]),str(empleadoT.getData()[5]),None,)
                    j = empleadoT.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    IV.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = empleadoT.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    IV.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    ListaTodos.addLast(IV)
                    
                if empleadoT == None:
                    pass
                else:
                    empleadoT = empleadoT.getNext()
        else:
            #busqueda de id en el txt de empleados 
            idBuscado = temp.getData()[0]
            empleadoT = emp.First()
            while empleadoT != None and (empleadoT == emp.Last() or empleadoT != emp.Last()):
                if idBuscado == empleadoT.getData()[1]:
                    AD = Administrador(str(empleadoT.getData()[0]),int(empleadoT.getData()[1]),None,str(empleadoT.getData()[3]),int(empleadoT.getData()[4]),str(empleadoT.getData()[5]),None,)
                    j = empleadoT.getData()[2].split()
                    dd = j[0]
                    mm = j[1]
                    aa = j[2]
                    AD.setFechaNacimiento(Fecha(dd,mm,aa))
                    k = empleadoT.getData()[6].split()
                    calle = k[0]
                    nomn = k[1]
                    brr = k[2]
                    ciudad = k[3]
                    edfc = k[4]
                    apto = k[5]
                    AD.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                    ListaTodos.addLast(AD)
                    
                if empleadoT == None:
                    pass
                else:
                    empleadoT = empleadoT.getNext()
        
        temp = temp.getNext()
    #tail de password
    if temp.getData()[2] == "investigador":
    #busqueda de id en el txt de empleados 
        idBuscado = temp.getData()[0]
        empleadoT = emp.First()
        while empleadoT != None and (empleadoT == emp.Last() or empleadoT != emp.Last()):
            if idBuscado == empleadoT.getData()[1]:
                IV = investigador(str(empleadoT.getData()[0]),int(empleadoT.getData()[1]),None,str(empleadoT.getData()[3]),int(empleadoT.getData()[4]),str(empleadoT.getData()[5]),None,)
                j = empleadoT.getData()[2].split()
                dd = j[0]
                mm = j[1]
                aa = j[2]
                IV.setFechaNacimiento(Fecha(dd,mm,aa))
                k = empleadoT.getData()[6].split()
                calle = k[0]
                nomn = k[1]
                brr = k[2]
                ciudad = k[3]
                edfc = k[4]
                apto = k[5]
                IV.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                ListaTodos.addLast(IV)
                
            if empleadoT == None:
                pass
            else:
                empleadoT = empleadoT.getNext()
    
    else:
        #busqueda de id en el txt de empleados 
        idBuscado = temp.getData()[0]
        empleadoT = emp.First()
        while empleadoT != None and (empleadoT == emp.Last() or empleadoT != emp.Last()):
            if idBuscado == empleadoT.getData()[1]:
                AD = Administrador(str(empleadoT.getData()[0]),int(empleadoT.getData()[1]),None,str(empleadoT.getData()[3]),int(empleadoT.getData()[4]),str(empleadoT.getData()[5]),None,)
                j = empleadoT.getData()[2].split()
                dd = j[0]
                mm = j[1]
                aa = j[2]
                AD.setFechaNacimiento(Fecha(dd,mm,aa))
                k = empleadoT.getData()[6].split()
                calle = k[0]
                nomn = k[1]
                brr = k[2]
                ciudad = k[3]
                edfc = k[4]
                apto = k[5]
                AD.setDir(Direccion(calle,nomn,brr,ciudad,edfc,apto))
                ListaTodos.addLast(AD)
                
            if empleadoT == None:
                pass
            else:
                empleadoT = empleadoT.getNext()
        
    
    tt = ListaTodos.first()
    while tt != None and tt.getNext() != None:
        print(type(tt.getData()))
        tt = tt.getNext()
    print(type(tt.getData()))
    
    
añadidor()
        
print("*** Bienvenido al sistema ***")
NumId = input("ID: ")
contra = input("Contraseña: ")

#menu de opciones
def OpcionesInvestigador():
    print("***********MENU***********")
    print("1.txt inventario")
    print("2. Agregar equipo")
    print("3. Eliminar equipo")
    print("4.txt Estado Solicitudes")
    op = int(input())
    if op == 1:
        n = IV.getNombre()
        id = str(IV.getId())
        IV.generarInventario(IV.getInventario(), IV.getNombre() + " " + id)
    elif op == 2:
        print("Si elegiste esta opcion es porque necesitas agregar un equipo. Tu informacion es: ")
        print("Tu nombre es" + IV.getNombre() + "y tu id es" + str(IV.getId()))
        respuesta = input("Es correcto?: ")
        if respuesta == "Si" or "si" or "sI" or "SI":
            print("Necesitamos la siguiente informacion del equipo: ")
            
            nombre = input("cual es el nombre del equipo?")
            numeroPlaca = input("numero de la placa del equipo")
            
            dd = input("Dia: ")
            mm = input("Mes:")
            aa = input("Año: ")
            fechaCompra = Fecha(dd, mm, aa)
            
            valorCompra = input("Ingresa el valor de la compra: ")
            
            
            equipo = Equipo(nombre, numeroPlaca, valorCompra)
            equipo.setFechaCompra(fechaCompra)
            equipo.setEmpAsociado(IV)
            
            print("Objeto creado :)")  
            with open("Textos/Solicitudes.txt", "a") as archivo:
                archivo.write("\n" + equipo.__str__())

            with open("Textos/Solicitudes.txt", "a") as i:
                i.write("\n"+str(equipo.getNombre())+" "+ str(equipo.getNumeroPlaca())+ str(equipo.getFechaCompra) + str(equipo.getValorCompra) + str(equipo.setEmpAsociado))
                
            print("Necesitamos la siguiente informacion de la solicitud ")
            nombreInvestigador = IV
            tipo = "Agregar"
            Equipo1 = equipo
            
            
            
            
            
            
            
        pass
    elif op == 3:
        pass
    elif op == 4:
        pass
        
    else:
        print("Opcion incorrecta")

def OpcionesAdministrador():
    print("***********MENU***********")
    print("0.Buscar usuario registrado")
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
    print("12. Salir")
    op = int(input())
    if op == 0:
        idBuscado = input("Id que busca: ")
        temp = emp.First()
        while temp != None and temp.getNext() != None:
            if idBuscado == temp.getData()[1]:
                p = ""
                for x in range(len(temp.getData())):
                    p += str(temp.getData()[x])+" "
                print(p)
            temp = temp.getNext()
        if idBuscado == temp.getData()[1]:
            p = ""
            for x in range(len(temp.getData())):
                p += str(temp.getData()[x])+" "
            print(p)
    elif op == 1:
        n = AD.getNombre()
        id = str(AD.getId())
        AD.generarInventario(AD.getInventario(), n + " " + id)
        OpcionesAdministrador()
    elif op == 2:
        e = int(input("Investigador(1) o Administrador(2)? : "))
        if e == 1:
            nombre = input("nombre: ")
            cedula = input("Cedula: ")
            dd = input("Dia de cumpleaños: ")
            mm = input("Mes de cumpleaños: ")
            aa = input("Año de nacimiento: ")
            f1 = Fecha(dd, mm, aa)
            ciudadNatal = input("Ciudad natal: ")
            tel = input("Telefono: ")
            email = input("email: ")
            c = input("Calle: ")
            nmn = input("Nomenclatura: ")
            br = input("Barrio: ")
            cy = input("Ciudad: ")
            edf = input("Edificio: ")
            apTo = input("Apartamento: ")
            ps = input("Contraseña: ")
            d1 = Direccion(c,nmn,br,cy,edf,apTo)
            IV1 = investigador(nombre,cedula,ciudadNatal,tel,email,ps,None)
            IV1.setFechaNacimiento(f1)
            IV1.setDir(d1)
            print("Objeto creado :)")  
            with open("Textos/Empleados.txt", "a") as archivo:
                archivo.write("\n" + IV1.__str__())

            with open("Textos/Password.txt", "a") as i:
                i.write("\n"+str(IV1.getId())+" "+ str(IV1.getPss())+ " investigador")
            ListaTodos.addLast(IV1)
            
                    
        elif e == 2:
            nombre = input("nombre: ")
            cedula = input("Cedula: ")
            dd = input("Dia de cumpleaños: ")
            mm = input("Mes de cumpleaños: ")
            aa = input("Año de nacimiento: ")
            f1 = Fecha(dd, mm, aa)
            ciudadNatal = input("Ciudad natal: ")
            tel = input("Telefono: ")
            email = input("email: ")
            c = input("Calle: ")
            nmn = input("Nomenclatura: ")
            br = input("Barrio: ")
            cy = input("Ciudad: ")
            edf = input("Edificio: ")
            apTo = input("Apartamento: ")
            ps = input("Contraseña: ")
            d1 = Direccion(c,nmn,br,cy,edf,apTo)
            AD1 = Administrador(nombre,cedula,ciudadNatal,tel,email,ps,None)
            AD1.setFechaNacimiento(f1)
            AD1.setDir(d1)
            print("Objeto creado :)")  
            with open("Textos/Empleados.txt", "a") as archivo:
                archivo.write("\n" + AD1.__str__())
            
            with open("Textos/Password.txt", "a") as i:
                i.write("\n"+str(AD1.getId())+" "+ str(AD1.getPss())+ " administrador")
            ListaTodos.addLast(AD1)
            
        else:
            print("Opcion Incorrecta")
            OpcionesAdministrador()
    elif op == 3:
        IdErase = input("Id a eliminar: ")            
        with open("Textos/Empleados.txt", "r") as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas):
                if IdErase in linea:
                    del lineas[i]
                    break
        with open("Textos/Empleados.txt", "w") as archivo:
                    archivo.writelines(linea for linea in lineas if linea.strip())
            
            
        #Elimino segun ID del txt de password
        with open("Textos/Password.txt", "r") as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas):
                if IdErase in linea:
                    del lineas[i]
                    break
        with open("Textos/Password.txt", "w") as archivo:
                    archivo.writelines(linea for linea in lineas if linea.strip())
                    
        rrr = ListaTodos.first()
        while rrr != None and (rrr == ListaTodos.last() or rrr != ListaTodos.last()):
            obj = rrr.getData()
            if obj.getId() == IdErase:
                ListaTodos.remove(rrr)
            if rrr == None:
                pass
            else:
                rrr = rrr.getNext() 
                    
                        
    elif op == 4:
        IdaCambiar = input("Id a cambiar: ")
        NContraseña = input("Nueva Contraseña: ")
        temp1 = pss.First()
        while temp1 != None and temp1.getNext() != None:
            if temp1.getData()[0] == IdaCambiar:
                with open("Textos/Password.txt", "r") as archivo:
                    lineas= archivo.readlines()
                for i in range(len(lineas)):
                    if IdaCambiar in lineas[i]:
                        if i == len(lineas)-1:
                            lineas[i] = str(IdaCambiar+" "+NContraseña+" "+temp1.getData()[2])
                        else:
                            lineas[i] = str(IdaCambiar+" "+NContraseña+" "+temp1.getData()[2])+"\n"
                with open("Textos/Password.txt", "w") as archivo:
                    archivo.writelines(lineas)
            temp1 = temp1.getNext()
        if temp1.getData()[0] == IdaCambiar:
                with open("Textos/Password.txt", "r") as archivo:
                    lineas= archivo.readlines()
                for i in range(len(lineas)):
                    if IdaCambiar in lineas[i]:
                        if i == len(lineas)-1:
                            lineas[i] = str(IdaCambiar+" "+NContraseña+" "+temp1.getData()[2])
                        else:
                            lineas[i] = str(IdaCambiar+" "+NContraseña+" "+temp1.getData()[2])+"\n"
                with open("Textos/Password.txt", "w") as archivo:
                    archivo.writelines(lineas)
   
    elif op == 5:
        pass
        
        
        
        pass
    elif op == 6:
        pass
    elif op == 7:
        IdIv = str(input("Identificacion: "))
        temp = ListaTodos.first()
        while temp != None and (temp == ListaTodos.last() or temp != ListaTodos.last()):
            if IdIv == str(temp.getData().getId()):
                n = temp.getData().getNombre()
                id = str(temp.getData().getId())
                temp.getData().generarInventario(temp.getData().getInventario(), str(n+" "+id))
                
            if temp == None:
                pass
            else:
                temp = temp.getNext()
   
    elif op == 8:
        pass
    elif op == 9:
        pass
    elif op == 10:
        pass
    elif op == 11:
        pass
    elif op == 12:
        pass
    else:
        print("Opcion incorrecta")
        OpcionesAdministrador()
    
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
                    """print("Admin encontrado", AD)"""
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