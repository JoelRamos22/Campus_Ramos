

# calculadora de Edad de Perros: Implementa un programa que calcule la edad de un perro en años perro basado en la edad humana ingresad




# voy a hacerlo con una formula que me dice que la edad perruna es igual a la edad humana = 16 x ln (edadHumana) + 31
import math
    #investigue para importar matematicas :D




EdadN = (int(input("\n Ingrese la edad en años humanos de su mascota : ")))




#hacemos una condicion para ver si la edad es mayor a 25 años
if EdadN > 25 :
    print ("\n ERROR ")
    print ("\n un perro vive un promedio de 17 años humanos")
else :
    if EdadN < 25 :
        EdadP = 16 * math.log(EdadN) + 31
        print ("\n la edad de su mascota en años perruno es : ", EdadP)