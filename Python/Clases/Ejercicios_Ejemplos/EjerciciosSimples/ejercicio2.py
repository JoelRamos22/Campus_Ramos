# Clasificador de Números: Crea un programa que clasifique un número ingresado como 'positivo', 'negativo' o 'cero'.

#preguntamos un numero al usuario 
numero = (int(input("ingrese un numero: ")))

# Despues de preguntarle al usuario el numero iniciamos un ciclo if para determinar que clase es 
if numero > 0:
    print("El numero es positivo")
elif numero < 0 :
    print ("El numero es negativo")
else :
    print ("cero")
