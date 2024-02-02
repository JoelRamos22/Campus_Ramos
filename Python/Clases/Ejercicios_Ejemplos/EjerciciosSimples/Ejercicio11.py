# Sistema de Reservas: Crea un programa que gestione reservas para un evento, donde ciertas condiciones (edad, membresía) determinan el precio del boleto.

precioBoleto = 10000 

edad = (int(input("Porfavor ejecute su edad ")))
Membresia = (bool(input("Diga T or F si tiene membresia (Escriba True o False) ")))

# voy a poner un descuento para los niños 
if edad < 14 and Membresia == True: 
    print ("\n Su descuento sera igual a un 5% por ser menor de 14 años, y un 10% por tener la membresia")
    preciototal = precioBoleto - (precioBoleto * 0.15)
    print (f"\n el precio total sera : {preciototal}")
    
elif edad > 14 and Membresia == True: 
    print (f"\n Su descuento sera igual un 10% por tener la membresia")
    preciototal = precioBoleto - (precioBoleto * 0.1)
    print (f"\n el precio total sera : {preciototal}")
    
elif edad > 14 and  Membresia == False : 
    print (f"\n usted no tendra descuento :D ")
    print (f"\n Su total es : {precioBoleto}")