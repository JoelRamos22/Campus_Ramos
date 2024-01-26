#Clasificador de Palabras: Escribe un programa que clasifique una palabra ingresada como 'corta' (menos de 5 caracteres), 'media' (entre 5 y 10 caracteres) o 'larga' (más de 10 caracteres).

palabra = (str(input("Ingrese una palabra : ")))

contador = (len(palabra))

if contador < 5 :

    print ("\n la palabra es corta")
    
elif contador >= 5 and contador < 10 :
    
    print ("\n la palabra es media")

else : 
    
    print ("\n la palabra es larga")