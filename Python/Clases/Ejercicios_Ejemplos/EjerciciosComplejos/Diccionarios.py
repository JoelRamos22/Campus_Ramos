# Escribe un algoritmo para una lista de diccionarios y ordenarlos por un valor de diccionarios . 

def diccionarios ():
    global listaD
    listaD = [
        {'nombre': "Juan", 'edad': 25},
        {'nombre': "Pedro", 'edad': 20},
        {'nombre': "Maria", 'edad': 22},
        {'nombre': "Jose", 'edad': 21}, ]

def leerLista():
    diccionarios ()
    Ordenados = sorted (listaD ,key=lambda x:x['edad'],reverse=False)
    for i in Ordenados : 
        print(f" -- nombre {i['nombre']} -- edad {i['edad']} ")

leerLista()



