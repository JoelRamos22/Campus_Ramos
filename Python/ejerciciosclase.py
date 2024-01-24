 #Pregunta a una persona su edad y utiliza una declaración if para determinar si es mayor de 18 años y puede votar.
print ("\n Bienvenido al sistema de edades del gobierno")
edad = (int(input("porfavor digite su edad")))

if edad >= 18 :
    print ("Usted esta habilitado para votar en las elecciones")
else : 
    print ("Usted no tiene la mayoria de edad aun no puede votar")


# sistema de notas

print ("\ Bienvenido a su sistema de notas personal")
nota = (int(input("Porfavor digite su nota")))

if nota >= 80 and nota <= 100 :
    print ("Su nota es : A ")
    print ("¡FELICITACIONES!")
elif nota > 65 and nota < 80 : 
    print (" Su nota es : B ")
    print ("BASTANTE BIEN")
elif nota < 65 and nota > 45 : 
    print (" Su nota es : C ")
    print ("LO HARAS MEJOR LA PROXIMA")
elif nota < 45 and nota > 0 : 
    print ("Su nota es : D")
    print ("estudia mas la proxima :C")
else : 
    print ("Su nota no esta entre los rangos adecuados porfavor intente de nuevo")


# Permítele a alguien elegir un tipo de comida y utiliza condicionales if para recomendar un restaurante según la elección (por ejemplo, comida italiana, mexicana o china).

print ("\n Bienvenido a nuestro sistema de recomendaciones de restaurantes")
comida = (int(input("Porfavor digite el tipo de comida que desea : 1 : italiana, 2 :mexicana o 3:  china :")))
comidaItaliana = "SANVIRGINOMONTIER"
comidaMexicana = "THE WEYES"
comidachin = "chaungFOOD"

if comida == 1: 
    print (f"Los mejores restaurantes en la zona para probar comida italian son : {comidaItaliana}")
elif comida == 2 : 
    print (f"Los mejores restaurantes en la zona para probar comida mexiana son : {comidaMexicana}")
elif comida == 3 :
    print (f"Los mejores restaurantes en la zona para probar comida china son : {comidachin}")
else : 
    print (" Lo sentimos no tenemos recomendaciones para ese tipo de comida por el momento, gracias por usar nuestro servicio") 

#Solicita una contraseña y utiliza una declaración if para verificar si coincide con una contraseña predefinida antes de permitir el acceso.

print ("Porfavor escriba su contraseña")
contraseña = (int(input("CONTRASEÑA : ")))

if contraseña : 
    print ("Hola usuario Porfavor vuelva a escribir su contraseña")
    recordatorio = (int(input("Ingrese su contraseña de nuevo")))
    if contraseña == recordatorio : 
        print (" Bienvenido de nuevo usuario ")
    elif contraseña != recordatorio : 
        print ("su contraseña es incorrecta porfavor intentelo de nuevo")