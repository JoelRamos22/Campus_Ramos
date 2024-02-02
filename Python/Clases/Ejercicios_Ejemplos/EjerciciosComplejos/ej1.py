def CalculoPrecioD(producto) : 
    if producto == 1 : 
        precio = 100 
        porcentaje = 0.1
    elif producto == 2:
        precio = 200
        porcentaje = 0.05
    else :
        precio = 50
        porcentaje = 0
        
    descuento = precio * porcentaje 
    total = precio - descuento 
    print (f"\n El precio del producto con un descuento : {descuento}, termina siendo un total de {total}")
    return total



def CalculoPrecioI(PrecioDescuento, producto) :
    if producto == 1 :
        PrecioconIm = PrecioDescuento * 0.1
    elif producto == 2 :
        PrecioconIm = PrecioDescuento * 0.15
    else : 
        PrecioconIm = PrecioDescuento * 0.05 
    totalconI = PrecioconIm
    print (f"\n El precio del producto con un impuesto : {PrecioconIm}")
    return totalconI 


def CalculoPrecioT(totalconI, total) :
    print ("\n El precio total es : ")
    totales = (totalconI + total)
    print (f"\n {totales}") 
    

print ("\n Producto 1: precio original $100, descuento 10%, impuesto 15%")
print ("\n Producto 2: precio original $200, descuento 5%, impuesto 10%")
print ("\n Producto 3: precio original $50, descuento 0%, impuesto 5%")
producto = (int(input("Ingrese el producto que quiere comprar ")))


PrecioDescuento = CalculoPrecioD(producto)

Impuesto = CalculoPrecioI(PrecioDescuento, producto)

PrecioTotal = CalculoPrecioT(Impuesto, PrecioDescuento)
