# Desarrolla una función que simule un sistema de monitoreo para un refrigerador. Esta función debe recibir la temperatura actual del refrigerador y retornar un mensaje de alerta si la temperatura es menor a 2°C (riesgo de congelación) o mayor a 4°C (riesgo de descomposición).

def temperatura(temperatura):
    temperatura = (int(input("Ingrese la temperatura del refrigerador (Grados Celcius) ")))
    if temperatura <= 2 : 
        print ("\n ¡El refrigerador tiene un riesgo de congelar los elementos en su interior! ")
    elif temperatura >= 4 :
        print ("\n ¡El refrigerador tiene un riesgo de descongelarse dañando sus elementos adentro! ")
    else : 
        print ("\n El refrigerador se encuentra en perfectas condiciones :D  ")
    print (f"\n con temperatura de : {temperatura}")

Temperatura = 0 

print (temperatura(Temperatura))

