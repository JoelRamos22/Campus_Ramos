#Crea una función que calcule cuánto de propina dejar en un restaurante basado en la calidad del servicio. La función debe aceptar el monto de la cuenta y la calidad del servicio (buena, aceptable, mala) y retornar el monto de la propina.

def propina(monto, calidad):
    if calidad == "buena":
        return monto * 0.15
        
    elif calidad == "aceptable":
        return monto * 0.1
    else :
        print ("lamentamos que no le haya gustado el servicio")


monto = (float(input("Escriba el costo de su cuenta ")))

calidad = (str(input("Escriba la calidad del servicio ")))

total = (propina(monto, calidad))

print (f"Nos serviria que nos dejara una propina de :  {total} muchas gracias")

