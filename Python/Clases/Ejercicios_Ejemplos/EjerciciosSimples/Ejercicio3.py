#Detector de Año Bisiesto: Escribe un script que determine si un año ingresado es bisiesto o no.

#Definimos una funcion para saber si el año es bisiesto (APRENDI A DEFINIR FUNCIONES POR INTERNET)
def añoBisiesto(año): 
    #observamos si el año ingresado es divisible por 4 y da 0 y si es divisible por 4 es divisible por 400
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0 : 
        return True
    else : 
        return False


AñoActual = (int(input("Escribe cualquier año despues de la fecha ")))

if añoBisiesto(AñoActual) : 
    print ("El año es bisiesto")
else : 
    print ("El año no es bisiesto")



