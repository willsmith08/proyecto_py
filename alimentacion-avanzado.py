import os
import time
import random
import re
import datetime

let_contra=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9",]
let_may=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cr_especial=[".","?","¡","¿","#","$","&","*"]
programas=["ADSO","GESTION ADMINISTRATIVA","GESTION EMPRESARIAL","ANIMACION 3D","MULTIMEDIA","MODISTERIA","COCINA","GANADERIA"]
menu=["Lunes: Arroz de coco con cerdo", "Martes: Pollo asado", "Miercoles: Carne a la llanera", "Jueves: Arroz trifasico", "Viernes: Chivo"]
dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

ya_entro=[]
nombres=[]
apellidos=[]
cedulas=[]
programas_apre=[]
correos=[]
semanas=[]
usuarios=[]
contraseñas=[]
usu_bloqueados=[]
usu_confirmacion=[]
puede_recibir=[]

semana1=1
semana2=2
semana3=3
semana4=4
semanas_activadas=[semana1]
semanas_desactivadas=[semana2,semana3,semana4]
contador_no_recibir=0

clv_mi = re.compile(r'[a-z]')
clv_may = re.compile(r'[A-Z]')
clv_numer = re.compile(r'[0-9]')
fecha_cambio=datetime.datetime.now()
fecha_mes=datetime.datetime.now().date()

while True:
    if (datetime.datetime.now().date() - fecha_mes).days > 30 :
        contador_no_recibir=0
    os.system("cls")
    print("""--- PROGRAMA DE ALIMENTACIÓN---
(0) Salir
(1) ADMIN
(2) Aprendiz
(3) Invitado""")
    opc_user=input("Elija una opción: ")
    
    #SALIR
    if opc_user == "0":
        break
    
    #Usuario ADMIN
    elif opc_user == "1":
        sesion_ad=False
        w_ini_ad=True
        while w_ini_ad:
            os.system("cls")
            print("--Sesion admin--")
            print("Si desea salir digite el numero 0")
            usu_ad=input("Escriba su usuario: ")
            if usu_ad == "0":
                w_ini_ad=False
            elif usu_ad != "Admin":
                for i in range(3):
                    os.system("cls")
                    print("Usuario incorrecto.")
                    time.sleep(0.5)
            else:
                break
        while w_ini_ad:
            os.system("cls")
            print("--Sesion admin--")
            print("Si desea salir digite el numero 0")
            con_ad=input("Escriba su contraseña: ")
            if con_ad == "0":
                w_ini_ad=False
            elif con_ad != "1234":
                for i in range(3):
                    os.system("cls")
                    print("Contarseña incorrecta.")
                    time.sleep(0.5)
            else:
                sesion_ad=True
                break
        if w_ini_ad == True and sesion_ad == True:
            for i in range(3):
                os.system("cls")
                print("Sesion ininciada.")
                time.sleep(0.5)
            os.system("cls")
            while True:
                os.system("cls")
                print("""--OPCIONES ADMIN--
(0) Salir
(1) Ingresar usuarios
(2) Eliminar usuarios
(3) Actualizar datos y credenciales de acceso
(4) Desbloquear usuario por ingreso erróneo
(5) Actualización de Menú
(6) Reasignación de semanas
(7) Listar aprendices registrados""")
                if (datetime.datetime.now().date() - fecha_mes).days >= 30:
                    fecha_mes=datetime.datetime.now().date()
                    print(f"\nDejaron de ser reclamandas {contador_no_recibir} apoyos alimentarios\n")
                opc_ad=input("Elija una opción: ")
                
                if len(usuarios) == 0 and (opc_ad == "2" or opc_ad == "3" or opc_ad == "4" or opc_ad == "6"):
                    for i in range(3):
                        os.system("cls")
                        print("No hay usuarios registrados.")
                        time.sleep(0.5)
                
                #Salir
                if opc_ad == "0":
                    break
                
                #Para cuando los aprendices esten completos
                if opc_ad == "1" and len(usuarios) > 39:
                    for i in range(3):
                        os.system("cls")
                        print("Cupos completos.")
                        time.sleep(0.5)
                        
                #Registrar usuarios
                elif opc_ad == "1":
                    w_us=True 
    
                    #REGISTRO DEL NOMBRE
                    while w_us:
                        os.system("cls")
                        print("--Registro de usuario--")
                        print("Si desea SALIR digite el  numero 0.")
                        nombre=input("Escriba solo los nombres para registrar. ej: Will Smith: ")
                        if nombre == "0":
                            w_us=False
                        elif nombre == "":
                            for i in range(3):
                                os.system("cls")
                                print(f"\nNombre no puede estar vacio.\n")
                                time.sleep(0.5)
                        elif bool(clv_numer.search(nombre)) == True:
                            for i in range(3):
                                os.system("cls")
                                print(f"\nNombre no incluye numeros.\n")
                                time.sleep(0.5)
                        else:
                            break
                        
                    #REGISTRO DEL APELLIDO
                    while w_us:
                        os.system("cls")
                        print("Si desea SALIR digite el  numero 0.")
                        apellido=input(f"Escriba los apellidos del aprendiz {nombre} para registrar. ej Toncel Mercado: ")
                        if apellido == "0":
                            w_us=False
                        elif apellido == "":
                            for i in range(3):
                                os.system("cls")
                                print(f"\Apellido no puede estar vacio.\n")
                                time.sleep(0.5)
                        elif bool(clv_numer.search(apellido)) == True:
                            for i in range(3):
                                os.system("cls")
                                print("\nApellido incorrecto.\n")
                                time.sleep(0.5)
                        else:
                            break
                        
                    #REGISTRO DEL DOCUMENTO
                    while w_us:
                        try:
                            os.system("cls")
                            print("Si desea SALIR digite el  numero 0.")
                            cedula=int(input(f"Escriba el numero de documento del aprendiz {nombre} para registrar: "))
                            if cedula == 0:
                                w_us=False
                            elif cedula in cedulas:
                                for i in range(3):
                                    os.system("cls")
                                    print("\nNumero de documento ya registrado.\n")
                                    time.sleep(0.5)
                            else:
                                break
                        except ValueError:
                            for i in range(3):
                                    os.system("cls")
                                    print("\nSolo se pueden ingresar numeros.\n")
                                    time.sleep(0.5)
                                    
                    #REGISTRO DEL PROGRAMA
                    if w_us == True:
                        while True:
                            os.system("cls")
                            cont=0
                            print("--Programas que reciben Alimentacion--")
                            for i in programas:
                                cont+=1
                                print(f"({cont}) {i}")
                            opc_pro=input(f"Segun las opciones elija el programa al que pertenece el aprendiz {nombre}: ")
                            if bool(clv_may.search(opc_pro)) == True or bool(clv_mi.search(opc_pro)) == True:
                                for i in range(3):
                                    os.system("cls")
                                    print("\nOpcion incorrecta\n")
                                    time.sleep(0.5)
                            else:
                                opc_pro=int(opc_pro)
                                if opc_pro-1 >= 0 and opc_pro-1 <= 7:
                                    break
                                else:
                                    for i in range(3):
                                        os.system("cls")
                                        print("\nOpcion incorrecta\n")
                                        time.sleep(0.5)
                        #REGISTRO DE LA SEMANA
                        if w_us == True:
                            programa=programas[opc_pro-1]
                            if programas[opc_pro-1] not in programas_apre:
                                if opc_pro == 1 or opc_pro == 2:
                                    semana=1
                                if opc_pro == 3 or opc_pro == 4:
                                    semana=2
                                if opc_pro == 5 or opc_pro == 6:
                                    semana=3
                                if opc_pro == 7 or opc_pro == 8:
                                    semana=4
                            else:
                                cont=0
                                for i in programas_apre:
                                    if i == programa:
                                        semana=semanas[cont]
                                        break
                                    cont+=1

                    #REGISTRO DEL CORREO
                    if w_us == True:
                        while True:
                            os.system("cls")
                            print("Siquiere salir digite el numero 0.")
                            correo=input("Escriba su correo: ")
                            if correo == "0":
                                w_us=False
                                break
                            if correo not in correos:
                                if "@" in correo:
                                    break
                                else:
                                    for i in range(5):
                                        os.system("cls")
                                        print("Corre electronico no permitido.")
                                        time.sleep(0.5)
                            else:
                                for i in range(5):
                                    os.system("cls")
                                    print("Corre electronico ya registrado.")
                                    time.sleep(0.5)

                    ##CREACION DEL USUARIO
                    if w_us == True:
                        usu=""
                        pos=0
                        ape=""
                        w=""
                        for i in apellido.strip():
                            if i == " ":
                                break
                            else:
                                ape+=i
                        for i in nombre.strip():
                            if i == " ":
                                usu+=nombre[pos+1]
                            pos+=1
                        usuario=nombre[0].lower()+usu.lower()+ape.lower()
                        while usuario in usuarios:
                            usuario+=random.choice(cr_especial)
                        contr=""
                        for i in nombre.strip():
                            if i == " ":
                                break
                            else:
                                contr+=i
                                
                        #CREACIÓN DE LA CONTRASEÑA
                        contraseña=random.choice(let_may)
                        while len(contraseña) < 8 or contraseña in contraseñas:
                            contraseña+=random.choice(let_contra)

                    #REGISTRO DATOS DE LOS USUARIOS
                    if w_us == True:
                        usu_confirmacion.append(False)
                        nombres.append(nombre)
                        apellidos.append(apellido)
                        cedulas.append(int(cedula))
                        programas_apre.append(programa)
                        correos.append(correo)
                        usuarios.append(usuario)
                        contraseñas.append(contraseña)
                        semanas.append(semana)
                        if semana in semanas_activadas:
                            puede_recibir.append(True)
                        else:
                            puede_recibir.append(False)
                        for i in range(3):
                            os.system("cls")
                            print("\nAprendiz registrado.\n")
                            time.sleep(0.5)
                        while True:
                            os.system("cls")
                            print(f"Su usuario es: {usuario}")
                            print(f"Su contraseña es: {contraseña}")
                            opc=input("Digite el numero 0 para salir: ")
                            if opc == "0":
                                break
                
                #Eliminar usuarios
                elif opc_ad == "2":
                    w_eliminar=True
                    while w_eliminar:
                        os.system("cls")
                        print("--Eliminar usuarios--")
                        contador=0
                        for i in nombres:
                            print(f"Nombre: {i} / Apellido: {apellidos[contador]} / Cedula: {cedulas[contador]}")
                            contador+=1
                        while w_eliminar:
                            try:
                                print("Si desea salir digite el numero 0.")
                                cc_borr=int(input("Digite el numero de identificacion del aprendiz a eliminar: "))
                                if cc_borr == 0:
                                    w_eliminar=False
                                    break
                                elif cc_borr in cedulas:
                                    indi=cedulas.index(cc_borr)
                                    print("Datos del aprendiz a eliminar")
                                    print(f"Nombre: {nombres[indi]} / Apellido: {apellidos[indi]} / Numero de identificacion: {cedulas[indi]}")
                                    time.sleep(4)
                                    nombres.pop(indi)
                                    apellidos.pop(indi)
                                    cedulas.pop(indi)
                                    programas_apre.pop(indi)
                                    correos.pop(indi)
                                    semanas.pop(indi)
                                    usuarios.pop(indi)
                                    contraseñas.pop(indi)
                                    for i in range(3):
                                        os.system("cls")
                                        print("Eliminando...")
                                        time.sleep(0.5)
                                    os.system("cls")
                                    print("Aprendiz eliminado exitosamente.")
                                    while w_eliminar:
                                        opc_eliminar=input("¿Desea seguir eliminado?: ")
                                        if opc_eliminar.upper() == "SI":
                                            break
                                        elif opc_eliminar.upper() == "NO":
                                            w_eliminar=False
                                else:
                                    for i in range(3):
                                        os.system("cls")
                                        print("Aprendiz no encontrado.")
                                        time.sleep(0.5)
                            except ValueError:
                                for i in range(3):
                                    os.system("cls")
                                    print("Solo de debe escribir numeros.")
                                    time.sleep(0.5)
                            
                #Actualizacion usuarios
                elif opc_ad == "3":
                    w_actua=True
                    while w_actua:
                        os.system("cls")
                        print("""--Actualizacion de datos de los aprendices--
(0) Salir
(1) Nombre
(2) Apellido
(3) Numero de documento
(4) Correo Electronico
(5) Programa
(6) Usuario
(7) Contraseña""")
                        opc_act=input("Elija una opcion: ")
                        if opc_act == "0":
                            break
                        
                        #Actualizacion nombre
                        elif opc_act == "1":
                            val="nombre"
                            lista=nombres
                            while True:
                                try:
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu in cedulas:
                                        ind_actu=cedulas.index(cc_actu)
                                        while True:
                                            nom_act=input(f"Escriba el nuevo {val}: ")
                                            if bool(clv_numer.search(nom_act)) == True:
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("No se aceptan numeros.")
                                                    time.sleep(0.5)
                                            else:
                                                lista[ind_actu]=nom_act
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("Cambio exitoso.")
                                                    time.sleep(0.5)
                                                break
                                        break
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)
                            
                        #Actualizacion apellido
                        elif opc_act == "2":
                            val="apellido"
                            lista=apellidos
                            while True:
                                try:
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu in cedulas:
                                        ind_actu=cedulas.index(cc_actu)
                                        while True:
                                            nom_act=input(f"Escriba el nuevo {val}: ")
                                            if bool(clv_numer.search(nom_act)) == True:
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("No se aceptan numeros.")
                                                    time.sleep(0.5)
                                            else:
                                                lista[ind_actu]=nom_act
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("Cambio exitoso.")
                                                    time.sleep(0.5)
                                                break
                                        break
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)
                        
                        #Actualizacion documento
                        elif opc_act == "3":
                            while True:
                                try:
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu in cedulas:
                                        ind_actu=cedulas.index(cc_actu)
                                        while True:
                                            try:
                                                nom_act=int(input(f"Escriba el nuevo numero de documento: "))
                                                if nom_act in cedulas:
                                                    for i in range(4):
                                                        os.system("cls")
                                                        print("Numero de documento ya registrado.")
                                                        time.sleep(0.5)
                                                else:
                                                    cedulas[ind_actu]=nom_act
                                                    for i in range(4):
                                                        os.system("cls")
                                                        print("Cambio exitoso.")
                                                        time.sleep(0.5)
                                                    break
                                            except ValueError:
                                                for i in range(4):
                                                        os.system("cls")
                                                        print("No se aceptan letras.")
                                                        time.sleep(0.5)
                                        break
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)
                        
                        #Actualizacion correo
                        elif opc_act == "4":
                            while True:
                                try:
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu in cedulas:
                                        ind_actu=cedulas.index(cc_actu)
                                        while True:
                                            nom_act=input(f"Escriba el nuevo correo electronico: ")
                                            if "@" not in nom_act:
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("No es un correo electronico.")
                                                    time.sleep(0.5)
                                            elif nom_act in correos:
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("Correo electronico ya registrado.")
                                                    time.sleep(0.5)
                                            else:
                                                correos[ind_actu]=nom_act
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("Cambio exitoso.")
                                                    time.sleep(0.5)
                                                break
                                        break
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)

                        #Actualizacion programa
                        if opc_act == "5":
                            while True:
                                try:
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu in cedulas:
                                        ind_actu=cedulas.index(cc_actu)
                                        while True:
                                            os.system("cls")
                                            cont=0
                                            print("--Programas que reciben Alimentacion--")
                                            for i in programas:
                                                cont+=1
                                                print(f"({cont}) {i}")
                                            opc_pro=input(f"Segun las opciones elija el nuevo programa al que pertenece el aprendiz: ")
                                            if bool(clv_may.search(opc_pro)) == True or bool(clv_mi.search(opc_pro)) == True:
                                                for i in range(3):
                                                    os.system("cls")
                                                    print("\nOpcion incorrecta\n")
                                                    time.sleep(0.5)
                                            else:
                                                opc_pro=int(opc_pro)
                                                if opc_pro-1 >= 0 and opc_pro-1 <= 7:
                                                    break
                                                else:
                                                    for i in range(3):
                                                        os.system("cls")
                                                        print("\nOpcion incorrecta\n")
                                                        time.sleep(0.5)
                                        if len(usuarios) == 0 or programas_apre.count(programas[opc_pro-1]) == 0:
                                            if opc_pro == 1 or opc_pro == 2:
                                                semana=1
                                            elif opc_pro == 3 or opc_pro == 4:
                                                semana=2
                                            elif opc_pro == 5 or opc_pro == 6:
                                                semana=3
                                            else:
                                                semana=4
                                        else:
                                            if opc_pro == 1 or opc_pro == 2:
                                                pro1="ADSO"
                                                pro2="GESTION ADMINISTRATIVA"
                                            elif opc_pro == 3 or opc_pro == 4:
                                                pro1="GESTION EMPRESARIAL"
                                                pro2="ANIMACION 3D"
                                            elif opc_pro == 5 or opc_pro == 6:
                                                pro1="MULTIMEDIA"
                                                pro2="MODISTERIA"
                                            else:
                                                pro1="COCINA"
                                                pro2="GANADERIA"
                                            for i in programas_apre:
                                                if i == pro1 or i == pro2:
                                                    semana=semanas[programas_apre[i]]
                                                    break
                                        programas_apre[ind_actu]=programas[opc_pro-1]
                                        print(programas_apre[ind_actu])
                                        print(programas[opc_pro-1])
                                        time.sleep(6)
                                        semanas[ind_actu]=semana
                                        for i in range(4):
                                            os.system("cls")
                                            print("Cambio exitoso.")
                                            time.sleep(0.5)
                                        break
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)
                                        
                        #Actualizacion usuario
                        elif opc_act == "6":
                            while True:
                                try:
                                    os.system("cls")
                                    print("Si desea salir digite el numero 0.")
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu == 0:
                                        break
                                    elif cc_actu in cedulas:
                                        ind_actu=cedulas.index(cc_actu)
                                        while True:
                                            nom_act=input(f"Escriba el nuevo usuario: ")
                                            if nom_act in usuarios:
                                                for i in range(4):
                                                    os.system("cls")
                                                    print(f"El usuario {nom_act} ya esta en uso.")
                                                    time.sleep(0.5)
                                            else:
                                                usuarios[ind_actu]=nom_act
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("Cambio exitoso.")
                                                    time.sleep(0.5)
                                                break
                                        break
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)
                                        
                        #Actualizacion contraseña
                        elif opc_act == "7":
                            w_actua_con=True
                            while w_actua_con:
                                try:
                                    os.system("cls")
                                    print("Si desea salir digite el numero 0.")
                                    cc_actu=int(input("Digite el numero de identificacion del aprendiz a editar: "))
                                    if cc_actu == 0:
                                        for i in range(4):
                                            os.system("cls")
                                            print("Cambio cancelado.")
                                            time.sleep(0.5)
                                        w_actua_con=False
                                        break
                                    elif cc_actu in cedulas:
                                        while w_actua_con:
                                            os.system("cls")
                                            print("Si desea salir digite el numero 0.")
                                            con_old=input("Ingrese su contraseña antigua: ")
                                            if con_old == "0":
                                                w_actua_con=False
                                                break
                                            elif con_old in contraseñas and cedulas.index(cc_actu) == contraseñas.index(con_old):
                                                ind_actu=cedulas.index(cc_actu)
                                                contraseña=random.choice(let_may)
                                                while len(contraseña) < 8 or contraseña in contraseñas or bool(clv_numer.search(contraseña)) == False or bool(clv_mi.search(contraseña)) == False:
                                                    contraseña+=random.choice(let_contra)
                                                contraseñas[ind_actu]=contraseña
                                                for i in range(4):
                                                    os.system("cls")
                                                    print(f"La nueva contraseña del usuario {usuarios[ind_actu]} es: {contraseña}")
                                                    time.sleep(0.5)
                                                while True:
                                                    opc_sa=input("Digite el numero 0 para salir: ")
                                                    if opc_sa == "0":
                                                        w_actua_con=False
                                                        break
                                            else:
                                                for i in range(4):
                                                    os.system("cls")
                                                    print("contraseña incorreta")
                                                    time.sleep(0.5)
                                    else:
                                        print("Numero de identificacion no registrado.")
                                except ValueError:
                                    for i in range(4):
                                        os.system("cls")
                                        print("No se aceptan letras")
                                        time.sleep(0.5)
                                        
                #Desbloquear usuarios
                elif opc_ad == "4":
                    w_blo=True
                    while w_blo:
                        os.system("cls")
                        print("--Usuarios bloqueados--")
                        for i in usu_bloqueados:
                            print(i)
                        print("Digite el numero 0 para salir.")
                        usu_blo=input("Digite el usuario del aprendiz a desbloquear: ")
                        if usu_blo == "0":
                            break
                        elif usu_blo in usu_bloqueados:
                            indi=usu_bloqueados.index(usu_blo)
                            usu_bloqueados.pop(indi)
                            for i in range(4):
                                os.system("cls")
                                print("Desbloqueo exitoso.")
                                time.sleep(0.5)
                            while w_blo:
                                seg_des=input("¿Desea seguir?: ")
                                if seg_des.upper() == "SI":
                                    break
                                elif seg_des.upper() == "NO":
                                    w_blo=False
                        else:
                            for i in range(4):
                                os.system("cls")
                                print("Usuario no encontrado.")
                                time.sleep(0.5)
                
                #Actualizacion de menu
                elif opc_ad == "5":
                    os.system("cls")
                    print("--Menú actual--")
                    for i in menu:
                        print(i)
                    l=input("\nEscriba la comida del lunes: ")
                    m=input("Escriba la comida del martes: ")
                    mi=input("Escriba la comida del miercoles: ")
                    j=input("Escriba la comida del jeves: ")
                    v=input("Escriba la comida del viernes: ")
                    menu[0]="Lunes "+l
                    menu[1]="Martes "+m
                    menu[2]="Miercoles "+mi
                    menu[3]="Jueves "+j
                    menu[4]="Viernes "+v
                    for i in range(3):
                        os.system("cls")
                        print("ACTUALIZACION EXITOSA.")
                        time.sleep(0.5)
                        
                #Reasignacion de semana
                elif opc_ad == "6":
                    w_reasig=True
                    while w_reasig:
                        while w_reasig:
                            os.system("cls")
                            cont=0
                            print("--Programas que reciben Alimentacion--")
                            print("(1) ADSO y GESTION ADMINISTRATIVA")
                            print("(2) GESTION EMPRESARIAL y ANIMACION 3D")
                            print("(3) MULTIMEDIA y MODISTERIA")
                            print("(4) COCINA y GANADERIA")
                            print("Si desea salir digite el numero 0.")
                            opc_pro=input(f"Elija el grupo de fichas a la que se le hará la reasignación: ")
                            if opc_pro == "0":
                                w_reasig=False
                            if bool(clv_may.search(opc_pro)) == True or bool(clv_mi.search(opc_pro)) == True:
                                for i in range(3):
                                    os.system("cls")
                                    print("\nOpcion incorrecta\n")
                                    time.sleep(0.5)
                            else:
                                opc_pro=int(opc_pro)
                                if opc_pro > 0 and opc_pro <= 4:
                                    break
                                else:
                                    for i in range(3):
                                        os.system("cls")
                                        print("\nOpcion incorrecta\n")
                                        time.sleep(0.5)
                        while w_reasig:
                            os.system("cls")
                            print("""(0) Salir
(1) Semana uno
(2) Semana dos
(3) Semana tres
(4) Semana cuatro""")
                            while w_reasig:
                                try:
                                    opc_reasig=int(input("Elija una de las opciones: "))
                                    if opc_reasig > 0 and opc_reasig < 5:
                                        break
                                except ValueError:
                                    print("No se permiten letras.")
                            
                            
                            if opc_pro == 1 or opc_pro == 2:
                                pro1="ADSO"
                                pro2="GESTION ADMINISTRATIVA"
                            if opc_pro == 3 or opc_pro == 4:
                                pro1="GESTION EMPRESARIAL"
                                pro2="ANIMACION 3D"
                            if opc_pro == 5 or opc_pro == 6:
                                pro1="MULTIMEDIA"
                                pro2="MODISTERIA"
                            if opc_pro == 7 or opc_pro == 8:
                                pro1="COCINA"
                                pro2="GANADERIA"
                                
                            #Semana anterior
                            cont=0
                            for i in programas_apre:
                                if i == pro1 or i == pro2:
                                    sem_ant=semanas[cont]
                                    break
                                
                            #Pasamos la semana a 0 de los programas seleccionados
                            cont=0
                            for i in programas_apre:
                                if i == pro1 or i == pro2:
                                    semanas[cont]=0
                                cont+=1
                            
                            if opc_reasig in semanas:
                                cont=0
                                for i in semanas:
                                    if i == opc_reasig:
                                        semanas[cont]=sem_ant
                                        if sem_ant == 1:
                                            puede_recibir[cont]=True
                                        else:
                                            puede_recibir[cont]=False
                                    cont+=1
                            
                            #Pasamos de 0 a la semana que es
                            cont=0
                            for i in semanas:
                                if i == 0:
                                    semanas[cont]=opc_reasig
                                    if opc_reasig == 1:
                                        puede_recibir[cont]=True
                                    else:
                                        puede_recibir[cont]=False
                                cont+=1
                                
                            for i in range(3):
                                os.system("cls")
                                print("Reasignacion exitosa.")
                                time.sleep(0.5)
                                
                            while True:
                                opcs=input("Digite el numero 0 para salir: ")
                                if opcs == "0":
                                    w_reasig=False
                                    break
                
                #Listar usuarios
                elif opc_ad == "7":
                    while True:
                        os.system("cls")
                        print("---Usuarios registrados---")
                        cont=0
                        for i in usuarios:
                            print(f"Nombre: {nombres[cont]}  /  Apellidos: {apellidos[cont]}  /  Programa: {programas_apre[cont]}  /  Semana: {semanas[cont]}  /  Cedula: {cedulas[cont]}  /  Correo: {correos[cont]}  /  Usuario: {usuarios[cont]}  /  Contraseña: {contraseñas[cont]}")
                            cont+=1
                        opcs=input("Digite el numero 0 para salir: ")
                        if opcs == "0":
                            break

    #Usuario Aprendiz                          
    elif opc_user == "2":
        while True:
            if datetime.datetime.now().time() == datetime.time(8,0,0):
                for i in semanas:
                    if i in semanas_activadas and puede_recibir[semanas.index(i)] == False:
                        puede_recibir[semanas.index(i)]=True
                
            time.sleep(0.5)
            os.system("cls")
            print("""--OPCIONES APRENDIZ--
(0) Salir
(1) Iniciar sesion
(2) Registrarse""")
            opc_user=input("Elija una opcion: ")
            
            #SALIR
            if opc_user == "0":
                break
            
            #INICAR SESION
            elif opc_user=="1":
                con_bloq=0
                sesion=False
                w_ini_usu=True
                while w_ini_usu:
                    os.system("cls")
                    print("--Inicio de sesion--")
                    print("Si desea cancelar el inicio de sesion digite el numero 0.")
                    ini_usu=input("Escriba su usario: ")
                    if ini_usu == "0":
                        w_ini_usu=False
                    elif ini_usu not in usuarios:
                        for i in range(3):
                            os.system("cls")
                            print("Usuario no registrado.")
                            time.sleep(0.5)
                    elif ini_usu in usu_bloqueados:
                        for i in range(6):
                            os.system("cls")
                            print("Usuario bloqueado, dirijase al admin para que pueda recuperar su cuenta.")
                            time.sleep(0.5)
                    else:
                        sem=semanas[usuarios.index(ini_usu)]
                        break
                while w_ini_usu:
                    os.system("cls")
                    print("--Inicio de sesion--")
                    print("Si desea cancelar el inicio de sesion digite el numero 0.")
                    ini_con=input("Escriba su contraseña: ")
                    if ini_con == "0":
                        w_ini_usu=False
                    elif ini_con not in contraseñas:
                        con_bloq+=1
                        for i in range(3):
                            os.system("cls")
                            print("Contraseña incorrecta.")
                            time.sleep(0.5)
                        w_recu=True
                        while w_recu:
                            opc_recu=input("¿Desea recuperar su contraseña?: ")
                            if opc_recu.upper() == "SI":
                                w_recu_contra=True
                                while w_recu_contra:
                                    while True:
                                        try:
                                            os.system("cls")
                                            print("--Recuperar contraseña--")
                                            print("Si desea salir digite el numero 0")
                                            cc_recu_con=int(input("Digite el numero de identificacion para recuperar su contraseña: "))
                                            if cc_recu_con == 0:
                                                break
                                            elif cc_recu_con in cedulas:
                                                if cedulas.index(cc_recu_con) != usuarios.index(ini_usu):
                                                    for i in range(3):
                                                        os.system("cls")
                                                        print("Numero de identificacion no coincide con el usuario.")
                                                        time.sleep(0.5)
                                                else:
                                                    indice=cedulas.index(cc_recu_con)
                                                    while True:
                                                        print(f"Contraseña {contraseñas[indice]}")
                                                        opc_sa_rec=input("Digite el numero 0 para salir: ")
                                                        if opc_sa_rec == "0":
                                                            break
                                                    w_recu=False
                                                    w_recu_contra=False
                                                    break
                                            else:
                                                for i in range(3):
                                                    os.system("cls")
                                                    print("Numero de identificacion no registrado.")
                                                    time.sleep(0.5)
                                        except ValueError:
                                            for i in range(3):
                                                os.system("cls")
                                                print("Solo debe digitar numeros.")
                                                time.sleep(0.5)
                            elif opc_recu.upper() == "NO":
                                break
                            
                    else:
                        if contraseñas.index(ini_con) == usuarios.index(ini_usu):
                            sesion=True
                            break
                        else:
                            con_bloq+=1
                            for i in range(3):
                                os.system("cls")
                                print("Contraseña incorrecta.")
                                time.sleep(0.5)
                    if con_bloq > 2:
                        usu_bloqueados.append(ini_usu)
                        for i in range(6):
                            os.system("cls")
                            print(f"el usuario {ini_usu} ha sido bloqueado por sobrepasar los intentos.")
                            print("Dirijase al admin para que pueda recuperar su cuenta.")
                            time.sleep(0.5)
                        w_ini_usu = False
                if w_ini_usu == True and sesion == True:
                    indice=usuarios.index(ini_usu)
                    w_ini_usu=True
                    while w_ini_usu:
                        if fecha_cambio != datetime.datetime.now().date():
                            fecha_cambio=datetime.datetime.now().date()
                            for i in semanas:
                                if i not in semanas_desactivadas:
                                    puede_recibir[semanas.index(i)]=True
                        num_dia=datetime.datetime.now().weekday() #para que se guarde el entero donde 0 es para lunes y asi sucesivamente
                        os.system("cls")
                        print("--Sesion iniciada--")
                        print(f"\nSeñor(a) {nombres[indice]} del progama {programas_apre[indice]} su semana de alimentacion es la ({semanas[indice]}) ")
                        if semanas[indice] in semanas_desactivadas and puede_recibir[indice] == True:
                            print("Debido a que alguna persona canceló su apoyo alimentario en este dia, se le ha reasignado a usted")
                        print(f"---MENÚ DE SU SEMANA {semanas[indice]}---")
                        
                        # "datetime.datetime.now().time()" Para saber la hora actual
                        if datetime.datetime.now().time() >= datetime.time(14,0,0) and dias[datetime.datetime.now().weekday()] == "Viernes":
                            semanas_desactivadas.append(semanas_activadas[0])
                            semanas_activadas.append(semanas_desactivadas[0])
                            semanas_desactivadas.pop(0)
                            semanas_activadas.pop(0)
                        for i in menu:
                            print(i)
                        if dias[datetime.datetime.now().weekday()] == "Sabado" or dias[datetime.datetime.now().weekday()] == "Domigo":
                            for i in range(6):
                                os.system("cls")
                                print("Sin servicio.")
                                time.sleep(0.5)
                        if (datetime.datetime.now().time() < datetime.time(8,00,00) or datetime.datetime.now().time() > datetime.time(13,30,00)) and semanas[indice] in semanas_activadas:
                             for i in range(6):
                                os.system("cls")
                                print("Aún no es hora de reclamar el apoyo alimentario")
                                print("Hora de habilidad: 08:00:00 AM a 11:00:00 PM")
                                time.sleep(0.5)
                        elif datetime.datetime.now().time() < datetime.time(8,00,00) or datetime.datetime.now().time() > datetime.time(13,30,00):
                            for i in range(6):
                                    os.system("cls")
                                    print("Aún no es hora de reclamar el apoyo alimentario")
                                    print("Hora de habilidad: 08:00:00 AM a 11:00:00 PM")
                                    time.sleep(0.5)
                        elif puede_recibir[indice] == False and semanas[indice] in semanas_activadas:
                            for i in range(6):
                                os.system("cls")
                                print("Apoyo alimentario ya reclamado.")
                                time.sleep(0.5)
                        elif puede_recibir[indice] == True:
                            while w_ini_usu:
                                    opc_recib=input("¿Desea recibir el almuerzo?: ")
                                    if opc_recib.upper() == "SI":
                                        usu_confirmacion[indice]=True
                                        puede_recibir[indice]=False
                                        for i in range(6):
                                            os.system("cls")
                                            print("PUEDE RECLAMAR SU APOYO ALIMENTARIOS.")
                                            time.sleep(0.5)
                                        if datetime.datetime.now().weekday() == 4:
                                            print("Feliz fin de semana")
                                        elif semanas[indice] in semanas_activadas:
                                            print(f"Le quedan por reclamar los siguientes dias")
                                            for i in menu:
                                                if menu.index(i) > num_dia:
                                                    print(i)
                                        break
                                    elif opc_recib.upper() == "NO":
                                        puede_recibir[indice]=False
                                        for i in usuarios:
                                            if semanas[usuarios.index(i)] == semanas_desactivadas[0] and puede_recibir[usuarios.index(i)] == False:
                                                puede_recibir[usuarios.index(i)]=True
                                                break
                                        break
                        elif semanas[indice] in semanas_desactivadas:
                            print(f"\nEstamos en la semana {semanas_activadas[0]}")
                            print("Debe esperar su semana para reclamar su apoyo alimentario.\n")
                        while True:
                            opc_sal=input("Digite el numero 0 para salir: ")
                            if opc_sal == "0":
                                w_ini_usu=False
                                break
                        
            elif opc_user == "1" and len(usuarios) == 40:
                for i in range(3):
                    os.system("cls")
                    print("Cupos completos.")
                    time.sleep(0.5)   
            #Registrase
            elif opc_user == "2":
                    w_us=True 
    
                    #REGISTRO DEL NOMBRE
                    while w_us:
                        os.system("cls")
                        print("--Registro de usuario--")
                        print("Si desea SALIR digite el  numero 0.")
                        nombre=input("Escriba solo los nombres para registrar. ej: Will Smith: ")
                        if nombre == "0":
                            w_us=False
                        elif nombre == "":
                            for i in range(3):
                                os.system("cls")
                                print(f"\nNombre no puede estar vacio.\n")
                                time.sleep(0.5)
                        elif bool(clv_numer.search(nombre)) == True:
                            for i in range(3):
                                os.system("cls")
                                print(f"\nNombre no incluye numeros.\n")
                                time.sleep(0.5)
                        else:
                            break
                        
                    #REGISTRO DEL APELLIDO
                    while w_us:
                        os.system("cls")
                        print("Si desea SALIR digite el  numero 0.")
                        apellido=input(f"Escriba los apellidos del aprendiz {nombre} para registrar. ej Toncel Mercado: ")
                        if apellido == "0":
                            w_us=False
                        elif apellido == "":
                            for i in range(3):
                                os.system("cls")
                                print(f"\Apellido no puede estar vacio.\n")
                                time.sleep(0.5)
                        elif bool(clv_numer.search(apellido)) == True:
                            for i in range(3):
                                os.system("cls")
                                print("\nApellido incorrecto.\n")
                                time.sleep(0.5)
                        else:
                            break
                        
                    #REGISTRO DEL DOCUMENTO
                    while w_us:
                        try:
                            os.system("cls")
                            print("Si desea SALIR digite el  numero 0.")
                            cedula=int(input(f"Escriba el numero de documento del aprendiz {nombre} para registrar: "))
                            if cedula == 0:
                                w_us=False
                            elif cedula in cedulas:
                                for i in range(3):
                                    os.system("cls")
                                    print("\nNumero de documento ya registrado.\n")
                                    time.sleep(0.5)
                            else:
                                break
                        except ValueError:
                            for i in range(3):
                                    os.system("cls")
                                    print("\nSolo se pueden ingresar numeros.\n")
                                    time.sleep(0.5)
                                    
                    #REGISTRO DEL PROGRAMA
                    if w_us == True:
                        while True:
                            os.system("cls")
                            cont=0
                            print("--Programas que reciben Alimentacion--")
                            for i in programas:
                                cont+=1
                                print(f"({cont}) {i}")
                            print("Digite el numero 0 para salir")
                            opc_pro=input(f"Segun las opciones elija el programa al que pertenece el aprendiz {nombre}: ")
                            if opc_pro == "0":
                                w_us=False
                                break
                            elif bool(clv_may.search(opc_pro)) == True or bool(clv_mi.search(opc_pro)) == True:
                                for i in range(3):
                                    os.system("cls")
                                    print("\nOpcion incorrecta\n")
                                    time.sleep(0.5)
                            else:
                                opc_pro=int(opc_pro)
                                if opc_pro-1 >= 0 and opc_pro-1 <= 7:
                                    if programas_apre.count(programas[opc_pro-1]) < 5 :
                                        break
                                    else:
                                        for i in range(3):
                                            os.system("cls")
                                            print(f"\nEl programa {programas[opc_pro-1]} ya tiene sus aprendices completos.\n")
                                            time.sleep(0.5)
                                else:
                                    for i in range(3):
                                        os.system("cls")
                                        print("\nOpcion incorrecta\n")
                                        time.sleep(0.5)
                        #REGISTRO DE LA SEMANA
                        if w_us == True:
                            programa=programas[opc_pro-1]
                            if programas[opc_pro-1] not in programas_apre:
                                if opc_pro == 1 or opc_pro == 2:
                                    semana=1
                                if opc_pro == 3 or opc_pro == 4:
                                    semana=2
                                if opc_pro == 5 or opc_pro == 6:
                                    semana=3
                                if opc_pro == 7 or opc_pro == 8:
                                    semana=4
                            else:
                                cont=0
                                for i in programas_apre:
                                    if i == programa:
                                        semana=semanas[cont]
                                        break
                                    cont+=1

                    #REGISTRO DEL CORREO
                    if w_us == True:
                        while True:
                            os.system("cls")
                            print("Siquiere salir digite el numero 0.")
                            correo=input("Escriba su correo: ")
                            if correo == "0":
                                w_us=False
                                break
                            if correo not in correos:
                                if "@" in correo:
                                    break
                                else:
                                    for i in range(5):
                                        os.system("cls")
                                        print("Corre electronico no permitido.")
                                        time.sleep(0.5)
                            else:
                                for i in range(5):
                                    os.system("cls")
                                    print("Corre electronico ya registrado.")
                                    time.sleep(0.5)

                    ##CREACION DEL USUARIO
                    if w_us == True:
                        usu=""
                        pos=0
                        ape=""
                        w=""
                        for i in apellido.strip():
                            if i == " ":
                                break
                            else:
                                ape+=i
                        for i in nombre.strip():
                            if i == " ":
                                usu+=nombre[pos+1]
                            pos+=1
                        usuario=nombre[0].lower()+usu.lower()+ape.lower()
                        while usuario in usuarios:
                            usuario+=random.choice(cr_especial)
                        contr=""
                        for i in nombre.strip():
                            if i == " ":
                                break
                            else:
                                contr+=i
                                
                        #CREACIÓN DE LA CONTRASEÑA
                        contraseña=random.choice(let_may)
                        while len(contraseña) < 8 or contraseña in contraseñas:
                            contraseña+=random.choice(let_contra)

                    #REGISTRO DATOS DE LOS USUARIOS
                    if w_us == True:
                        usu_confirmacion.append(False)
                        nombres.append(nombre)
                        apellidos.append(apellido)
                        cedulas.append(int(cedula))
                        programas_apre.append(programa)
                        correos.append(correo)
                        usuarios.append(usuario)
                        contraseñas.append(contraseña)
                        semanas.append(semana)
                        if semana in semanas_activadas:
                            puede_recibir.append(True)
                        else:
                            puede_recibir.append(False)
                        for i in range(3):
                            os.system("cls")
                            print("\nAprendiz registrado.\n")
                            time.sleep(0.5)
                        while True:
                            os.system("cls")
                            print(f"Su usuario es: {usuario}")
                            print(f"Su contraseña es: {contraseña}")
                            opc=input("Digite el numero 0 para salir: ")
                            if opc == "0":
                                break
                
    #Usuario INVITADO        
    elif opc_user == "3":
        while True:
            os.system("cls")
            cont=0
            print("--MENU DEL APOYO ALIMENTARIO--")
            for i in menu:
                print(i)
            while True:
                opcs=input("Digite el numero 0 para salir: ")
                if opcs == "0":
                    break
            break