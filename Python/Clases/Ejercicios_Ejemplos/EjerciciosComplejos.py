

def calcularPrecio (productos1):
    nombre = (str(input("Escriba su nombre ")))
    productos = (int(input("Digite la cantidad de productos ")))
    if productos > 0: 
        precio = productos * 200
        print (f"Hola usuario : {nombre} tienes que pagar es de {precio}")
        return precio 
productos = 0 
calcularPrecio(productos)

def CalcularPrecioP (nombre,Productos,precio): 
    print (f"Hola usuario : {nombre} tienes que pagar una cantidad de productos {Productos} con precio total {precio} $")
    
CalcularPrecioP("joel", 5, 5600)
