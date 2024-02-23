import json
def Opciones_Gestion_Juegos(opcion): 
    while True: 
        if opcion == 1 : 
            Registrar_Juegos() 
            break 
        elif opcion == 2 : 
            Modificar_Juegos() 
            break 
        elif opcion == 3 : 
            Eliminar_Juegos()  
            break 
        elif opcion == 4 : 
            print ("\n Volviendo al menu principal...")
            break 
    return

def Registrar_Juegos():
    with open ('Juegos.json', 'r') as juego_file : 
        juegos = json.load(juego_file) 
    while True : 
        respuesta = input ("\n ¿Desea registrar algun juego? : ")
        if respuesta.lower() == "si" : 
            nombre = input ("\n Ingrese el nombre del juego : ")
            tiempo_por_partida = int(input (" Ingrese el tiempo minimo de duracion de una partida del juego en terminos de minutos (120 / dos horas) : "))
            cantidad_jugadores = int(input (" Ingrese la cantidad maxima de jugadores que pueden jugar una partida : "))
            ejemplares = int(input (" Ingrese la cantidad de ejemplares del juego : "))
            nuevo_juego = {
                "nombre" : nombre,
                "tiempo_por_partida" : tiempo_por_partida,
                "cantidad_jugadores" : cantidad_jugadores,
                "ejemplares" : ejemplares
            }
            juegos.append(nuevo_juego)
            print ("\n JUEGO REGISTRADO CON EXITO ")
            with open ('Juegos.json', 'w') as juego_file :
                json.dump(juegos, juego_file, indent = 4)
                break
        elif respuesta.lower() == "no" : 
            print (" saliendo...")
            break

def Modificar_Juegos():
    with open ('Juegos.json', 'r') as juego_file : 
        juegos = json.load(juego_file) 
    while True : 
        respuesta = input ("\n ¿Desea modificar algun juego? : ")
        if respuesta.lower() == "si" : 
            for i, juego in enumerate(juegos):
                print(f" {i+1}. {juego['nombre']} ")
            opcion = int (input ("\n ¿Que juego desea modificar? :  "))
            if 1 <= opcion <= len(juegos) : 
                juego_elegido = juegos[opcion-1]
                pregunta = input ("\n Desea modificar:\n- El tiempo por partida\n- La cantidad de jugadores\n- La cantidad de ejemplares\n :")
                if pregunta.lower() == "el tiempo por partida": 
                    juego_elegido['tiempo_por_partida'] = int (input ("\n Ingrese la nueva duracion de una partida : "))
                elif pregunta.lower() == "la cantidad de jugadores":
                    juego_elegido['cantidad_jugadores'] = int (input ("\n Ingrese la nueva cantidad de jugadores : "))
                elif pregunta.lower() == "la cantidad de ejemplares":
                    juego_elegido['ejemplares'] = int (input ("\n Ingrese la nueva cantidad de ejemplares : "))
                else : 
                    print ("\n No se encontro esa categoria dentro del juego")
                with open ('Juegos.json', 'w') as juegos_file : 
                    json.dump(juegos, juegos_file, indent = 4)
                    break
        elif respuesta.lower() == "no" : 
            print (" saliendo...")
            break
    return

def Eliminar_Juegos(): 
    with open ('Juegos.json', 'r') as juego_file : 
        juegos = json.load(juego_file) 
    while True : 
        respuesta = input ("\n ¿Desea eliminar algun juego? : ")
        if respuesta.lower() == "si" : 
            for i, juego in enumerate(juegos):
                print(f" {i+1}. {juego['nombre']} ")
            opcion = int (input ("\n ¿Que juego desea eliminar? :  "))
            if 1 <= opcion <= len(juegos) : 
                juego_elegido = juegos[opcion-1]
                juegos.remove(juego_elegido)
                print ("\n JUEGO ELIMINADO CON EXITO ") 
                with open ('Juegos.json', 'w') as juegos_file : 
                    json.dump(juegos, juegos_file, indent = 4)
                    break
        elif respuesta.lower() == "no" : 
            print (" saliendo...")
            break
    return