#Validación de Contraseña: Escribe un programa que verifique si una contraseña ingresada cumple con los criterios de tener al menos 8 caracteres, una mayúscula, una minúscula y un número.
# INTENTE HACER EL CODIGO EN INGLES 


# Definimos funciones para las distintas cosas que necesitamos 

    # 1 funcion para saber si la contraseña tiene una mayuscula 
def HaveUpper (password) :
    for character in password :
        if character.isupper() :
            return True
    return False    
    # 2 funcion para saber si la contraseña tiene una minúscula
def Havelower (password) :
    for character in password : 
        if character.islower() :
            return True 
    return False
    # 3 funcion para saber si la contraseña tiene un número
def HaveDigit (password):
    for character in password:
        if character.isdigit() :
            return True
    return False    
    
# Pedimos una contraseña al usuario         
password = (str(input("ingrese una contraseña")))

#Contamos el numero de caracteres de la cadena 
len1 = len (password)

#Iniciamos un ciclo para saber si la cadena de caracteres cumple con las condiciones e imprimimos distintos mensajes 
if len1 > 8 and HaveUpper(password) and Havelower(password) and HaveDigit(password) :
    print ("\n your new password has been update as :  ")
    print (password)
else : 
    print ("your password is to weak, please try adding one lower character, one upper character and one digit in the password :D")