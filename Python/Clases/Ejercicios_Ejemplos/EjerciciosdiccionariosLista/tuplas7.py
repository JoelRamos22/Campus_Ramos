# Contar cuántas veces aparece un elemento en una tupla.
def ContarTupla(tupla1): 
    contador = 0
    numero = (int(input("Ingrese el numero que quiere contar ")))
    for i in tupla1:
        if numero == i :
            contador += 1
            
    print(f"La tupla contiene {contador} veces el elemento : {numero}") 
    return contador

tupla1 = (1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"la tupla es : {tupla1}")
ContarTupla(tupla1)