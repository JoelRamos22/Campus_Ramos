# Encontrar el índice de un elemento en una tupla.

def indiceTupla(tupla):
    indice = 0
    acceso = (int(input(f"\n ingreese el elemento de la tupla al que quiere acceder ")))
    for elemento in tupla:
        indice+= 1 
        if acceso ==  elemento : 
            print (f"el indice del elemento : {acceso} es : {indice}")
        
        
tuplas1= (1,2,3,4) 
print (f"Los elementos de las tuplas son :{tuplas1}")       
indiceTupla(tuplas1)