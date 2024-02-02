# Comprobar si un elemento existe en una tupla.
def ContartuplaE(tupla):
    numero = (int(input("Ingrese el numero que quiere buscar ")))
    if numero not in tupla : 
            print(f"El elemento no existe en la tupla")
    else : 
        if numero in tupla : 
            print (f"El elemento existe en la tupla: {numero}")


tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


ContartuplaE(tupla1)

