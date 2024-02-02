# producto 
#valor por unidad 
PañalesU = (1000)
CantidadRegalo = 0 
CantidadCompra = (int(input("porfavor ingrese la unidades que desea llevar")))

if CantidadCompra > 1 and CantidadCompra < 36 : 
    totalC = CantidadCompra * PañalesU
    print (f"Total cantidad compra : {totalC}")
else : 
    if CantidadCompra < 0 : 
        print (F"no puede ingresar ¨{CantidadCompra}")
        
if CantidadCompra <= 36 : 
    totalC = CantidadCompra * PañalesU
    Descuento = CantidadCompra * PañalesU * 0.1
    totalDes = totalC - Descuento
    print (f"Total cantidad despues del descuento es compra : {totalDes}")
elif CantidadCompra > 36 and CantidadCompra <= 48 :
    totalC = CantidadCompra * PañalesU
    Descuento = CantidadCompra * totalC * 0.15
    totalDes = totalC - Descuento
    print (f"Total cantidad despues del descuento es compra : {totalDes}")
else : 
    if CantidadCompra >= 60:
        for CantidadCompra in range (1, CantidadCompra + 1):
            if CantidadCompra >= 60 and CantidadCompra % 12 == 0:
                CantidadRegalo += 1

        totalC = CantidadCompra * PañalesU
        Descuento = CantidadCompra * PañalesU * 0.15
        totalDes = totalC - Descuento
        print (f"\n La cantidad que usted compro fue : {CantidadCompra} y le regalamos una unidad de regalo por cada docena entonce se lleva {CantidadRegalo}, entonces se termina llevando :", CantidadCompra + CantidadRegalo )
        print (f"\n el total a pagar era : {totalC}")
        print (f"\nTotal cantidad despues del descuento es compra : {totalDes}")
    
        
