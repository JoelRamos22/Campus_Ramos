# Juego Piedra, Papel o Tijera: Escribe un juego de piedra, papel o tijera donde el usuario juega contra la computadora.

import random 

opciones = ["Piedra",  "Tijera", "Papel"]

while True : 
    usuario= (input("Elija :  Piedra, Tijera, Papel "))
    if usuario not in opciones : 
        print("Opción incorrecta")
        continue
    pc = random.choice(opciones)
    print (f"la computadora ha seleccionado : {pc} ")
    if usuario == pc:
        print (f"Empate!, ambos eligieron : {pc} ")
    elif usuario == "Piedra" and pc == "Tijera":
        print (f"El usuario gana ha elegido : {usuario} y la computadora eligio : {pc} ")
    elif usuario == "Piedra" and pc == "Papel": 
        print (f"la computadora gana ha elegido : {pc} y el usuario eligio : {usuario} ")
    elif usuario == "Tijera" and pc == "Piedra": 
        print (f"la computadora gana ha elegido : {pc} y el usuario eligio: {usuario} ")
    elif usuario == "Tijera" and pc == "Papel":
        print (f"El usuario gana ha elegido : {usuario} y la computadora eligio: {pc}")
    elif usuario == "Papel" and pc == "Piedra": 
        print (f"El usuario gana ha elegido : {usuario} y la computadora eligio: {pc}")
    elif usuario == "Papel" and pc == "Tijera":
        print (f"la computadora gana ha elegido : {pc} y el usuario eligio {usuario} ")
    else : 
        print (f"Fin del juego")
    
