import menu 
import Gestion_Juegos 
import Consultas_Valoraciones
while True : 
    try : 
        opc = menu.Menu_Principal()
        if opc == 1: 
            opc_Gestion_Juegos = menu.Menu_Gestion_Juegos()
            Gestion_Juegos.Opciones_Gestion_Juegos(opc_Gestion_Juegos)
        elif opc == 2: 
            opc_Consultas_Valoraciones = menu.Menu_Consultas_Valoracione()
            Consultas_Valoraciones.Consultas_opciones(opc_Consultas_Valoraciones)
        elif opc == 3: 
            confirmacion = input("\n ¿Desea salir del sistema? : ")
            if confirmacion.lower() == "si" : 
                print ("\n saliendo...")
                break 
            elif confirmacion.lower() == "no" : 
                continue 
    except Exception : 
        print ("\n Error en el programa... ")
        continue
