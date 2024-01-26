#Calculadora de Impuestos: Haz un programa que calcule el impuesto aplicado a un ingreso ingresado, donde el impuesto varía según diferentes rangos de ingresos.

IngresoI = (float(input("\n Ingrese algun valor")))

if IngresoI >= 100000 : 
    print ("\n El valor inicial es de : ", IngresoI)
    print ("\n El valor de impuesto aplicado sera de un 4%")
    valorimpuesto = 0.04 
    valortotal = IngresoI + (IngresoI * valorimpuesto)
    print ("\n El valor total a pagar es de: ", valortotal, " $ ")
elif IngresoI >= 200000 : 
    print ("\n El valor inicial es de : ", IngresoI)
    print ("\n El valor de impuesto aplicado sera de un 8%")
    valorimpuesto = 0.08
    valortotal = IngresoI + (IngresoI * valorimpuesto)
    print ("\n El valor total a pagar es de: ", valortotal, " $ ")
elif IngresoI >= 300000 : 
    print ("\nEl valor inicial es de : ", IngresoI)
    print ("\n El valor de impuesto aplicado sera de un 12%")
    valorimpuesto = 0.12
    valortotal = IngresoI + (IngresoI * valorimpuesto)
    print ("\nEl valor total a pagar es de: ", valortotal, " $ " )
else : 
    print ("No aplicamos impuestos a valores por debajo de 100000$")