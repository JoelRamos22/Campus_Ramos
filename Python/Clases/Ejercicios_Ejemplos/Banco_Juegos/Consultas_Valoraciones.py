import json
def Consultas_opciones(opcion):
    while True :
        if opcion == 1 :
            Consultar_Juego()
            break
        elif opcion == 2 :
            Realizar_Valoraciones()
            break
        elif opcion == 3 :
            mostrar_top_juegos_mas_valorados()
            break
        elif opcion == 4 : 
            print ("\n Volviendo al menu principal...")
            break

def Consultar_Juego(): 
    with open ('Juegos.json', 'r') as juegos_file : 
        juegos = json.load(juegos_file) 
    while True:
        respuesta = input ("\n ¿Desea consultar algun juego? : ")
        if respuesta.lower() == "si" : 
            tiempo_promedio = int (input("\n Ingrese el tiempo promedio de juego en valores de minutos (120 = 2 horas) : "))
            for i, juego in enumerate(juegos): 
                if tiempo_promedio >= juego["tiempo_por_partida"]: 
                    print ("\n tus opciones disponibles son : ")
                    print(f" {i+1}. {juego['nombre']} ")
        elif respuesta.lower() == "no" : 
            print (" Volviendo al menu principal... ")
            break 
    return

def Realizar_Valoraciones(): 
    with open('Juegos.json', 'r') as juegos_file: 
        juegos = json.load(juegos_file)

    while True: 
        respuesta = input("\n¿Desea realizar una valoración? (si/no): ")
        if respuesta.lower() == "si": 
            for i, juego in enumerate(juegos): 
                print(f"{i+1}. {juego['nombre']}")

            opcion = int(input("\n¿Qué juego desea valorar? Ingrese el número correspondiente: "))
            if 1 <= opcion <= len(juegos): 
                nombre_juego = juegos[opcion - 1]['nombre']
                valoracion = int(input(f"\n¿Qué valoración del 1 al 5 le daría a '{nombre_juego}'? "))
                if 1 <= valoracion <= 5:
                    with open('Valoraciones.txt', 'a') as valoraciones_file:
                        valoraciones_file.write(f"{nombre_juego}: {valoracion}/5 estrellas\n")
                        print("¡Valoración registrada exitosamente!")
                else:
                    print("La valoración debe ser un número entre 1 y 5.")

        elif respuesta.lower() == "no": 
            print("Volviendo al menú principal...")
            break 

def mostrar_top_juegos_mas_valorados():

    valoraciones_por_juego = {}

    with open('Valoraciones.txt', 'r') as valoraciones_file:
        lineas = valoraciones_file.readlines()
        for linea in lineas:

            nombre_juego, valoracion = linea.strip().split(': ')

            valoraciones_por_juego[nombre_juego] = valoraciones_por_juego.get(nombre_juego, 0) + 1

    juegos_ordenados = sorted(valoraciones_por_juego.items(), key=lambda x: x[1], reverse=True)

    top_1 = top_2 = top_3 = None

    for juego, num_valoraciones in juegos_ordenados:
        if top_1 is None:
            top_1 = (juego, num_valoraciones)
        elif top_2 is None and num_valoraciones < top_1[1]:
            top_2 = (juego, num_valoraciones)
        elif top_3 is None and num_valoraciones < top_2[1]:
            top_3 = (juego, num_valoraciones)
        else:
            break

    print(" Top 3 de juegos más valorados : ")
    if top_1:
        print(f"\n 1. {top_1[0]}: {top_1[1]} valoraciones")
    if top_2:
        print(f" 2. {top_2[0]}: {top_2[1]} valoraciones")
    if top_3:
        print(f" 3. {top_3[0]}: {top_3[1]} valoraciones")

