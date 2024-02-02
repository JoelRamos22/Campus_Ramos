# Analizador de Redes Sociales: Crea un programa que analice datos de un perfil de redes sociales (como número de amigos, publicaciones, etc.) y clasifique el perfil en diferentes categorías.

def AnalisisCuenta(cuenta):
    if cuenta == "si":
        print ("Bienvenido Vamos a empezar con el analisis de tu cuenta")
        usuario = (str(input("Digite su nombre de usuario ")))
        fechaA = (str(input("Digite la fecha desde la que esta activo ejemplo --/--/-- ")))
        Amigos = (int(input("Digite la cantidad de amigos que tiene" )))
        Publicaciones = (int(input("Digite la cantidad de publicaciones que tiene")))
        promedioSu = Amigos + Publicaciones 
        promedioP = promedioSu / (Publicaciones / 2)
        if Amigos <= 300 and Publicaciones <= 20 : 
            print (f"bienvenido : {usuario} Usted tiene una cuenta bastante pequeña con poca cantidad de interacciones")
            interaccionesP = promedioP
            print (f"sus interacciones promedio estan dentro del rango de : {interaccionesP}")
        elif Amigos >= 300 and Amigos <= 600 and Publicaciones >= 20 and Publicaciones <= 50:
            print (f"bienvenido : {usuario} Usted tiene una cuenta moderada con poca cantidad de interacciones")
            interaccionesP = promedioP
            print (f"sus interacciones promedio estan dentro del rango de : {interaccionesP}")
        elif Amigos >= 600 and Amigos <= 1000  and Publicaciones <= 100 and Publicaciones >= 50 :  
            print (f"bienvenido : {usuario} Usted tiene una cuenta bastante grande con una cantidad media de interacciones")
            interaccionesP = promedioP
            print (f"sus interacciones promedio estan dentro del rango de : {interaccionesP}")
        elif Amigos>= 1000 and Amigos <= 3000 and Publicaciones>= 100 and Publicaciones <= 300: 
            print (f"bienvenido : {usuario} Usted tiene una cuenta muy grande apunto de ser famosa con una cantidad grande de interacciones")
            interaccionesP = promedioP
            print (f"sus interacciones promedio estan dentro del rango de : {interaccionesP}")
        elif Amigos>= 3000 and Amigos <=4000 and Publicaciones>=300 and  Publicaciones >= 500 : 
            print (f"bienvenido : {usuario} Usted es considerado como un influencer Felicidades! cuenta con una gran cantidad de interacciones ")
            interaccionesP = promedioP
            print (f"sus interacciones promedio estan dentro del rango de : {interaccionesP}")
        

def CreacionCuenta(Cuenta): 
    if Cuenta == "no" :
        print ("Hola Vamos a empezar con la creacion de tu cuenta")
        usuario = (str(input("Escriba el nombre de usuario que desea tener ")))
        contraseña = (str(input("Escriba una contraseña ")))
        len1 = len(contraseña)
        while len1 < 6 :
            print ("La contraseña debe tener al menos 6 en adelante caracteres")
            contraseña = (str(input("Digite una nueva contraseña "))) 
            if len1 >= 6 :
                break 
        Informaction = ("su nombre de usuaro es : ", usuario, " y su contraeña es : ", contraseña) 
        print (f"Su cuenta ha sido creada con los siguientes datos : {Informaction} ")

print ("¿Cuenta usted con una cuenta de bookface?")

cuenta = (str(input("si o no ")))

if cuenta == "no":
    CreacionCuenta(cuenta)
    if CreacionCuenta == True :
            print ("Su cuenta ha sido creada con exito")
            print ("si ahora desea analizar su cuenta presione 2 ")
            cuenta = (str(input("")))
            if cuenta == "2" :
                AnalisisCuenta(cuenta)
elif cuenta == "si" : 
    AnalisisCuenta(cuenta) 
    
