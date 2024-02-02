# el nombre de usuario y con una funcion imprimir un mensaje de hola nombre etc y una funcion extra para calcular el area de un cuadrado y solo devolver el area del cuadrado 

def Hola(nombre):
    print ("Hola usuario :")
    return nombre

def  AreaCuadrado(lados):
    area = lados * lados
    print (f"El area del cuadrado es : ")
    return area
    

nombre = (str(input("Escriba su nombre : ")))

lados = (int(input("digite los lados del cuadrado : ")))

print (Hola(nombre))
print (AreaCuadrado(lados))