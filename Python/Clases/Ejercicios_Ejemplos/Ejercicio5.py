# Juego de Adivinanzas: Implementa un juego donde el usuario debe adivinar un número generado aleatoriamente, dando pistas si su intento es demasiado alto o bajo. 


# importamos la opcion random 
import random

# ponemos un rando con random.randint entre la cantidad que queremos que el usuario adivine 
NumeroAdivinado = random.randint(0,100)

numero1 = 0 
# ahora iniciamos un bucle while para poner las instrucciones de la cantidad
while NumeroAdivinado != numero1 : 
    numero1 = (int(input("porfavor ingrese un numero 0 - 100")))
    if NumeroAdivinado > numero1 :
        print (f"El numero : {numero1} es menor intente un numero mas alto ")
    elif NumeroAdivinado < numero1 :
        print (f"El numero : {numero1} es mayor intente un numero mas bajo ")
    
    if NumeroAdivinado == numero1 : 
        print ("FELICIDADES ADIVINASTE EL NUMERO")
        break