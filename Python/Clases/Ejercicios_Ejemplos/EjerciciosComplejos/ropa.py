# Escribe una función que recomiende qué tipo de ropa vestir basado en la temperatura exterior actual. Por ejemplo, por encima de 25°C recomienda ropa ligera, entre 15°C y 25°C sugiere una camiseta y pantalón, etc.

def ropa(temperatura): 
    temperatura = (int(input("\n Ingrese la temperatura a la que nos encontramos en grados celcius ")))
    if temperatura >= 25 : 
        print (f"\n Mi recomendacion es que use una ropa clara, excluyendo colores oscuros, y pantalones olgados, tonos del amarillo al blanco que seria el conjunto ideal para usar con {temperatura}")
    elif temperatura >= 15 and temperatura <=25 :
        print (f"\n Mi recomendacion es que use cualquier tipo de ropa ya que estamos en la temperatura perfecta : {temperatura} ")
    else : 
        print (f"\n Mi recomendacion es que use ropa abrigada que es ropa abrigada, con chalecos o abrigos con gorros y guantes para resguardarse del frio ya que la temperatura es : {temperatura}")

Temperatura = 0

ropa(Temperatura)

