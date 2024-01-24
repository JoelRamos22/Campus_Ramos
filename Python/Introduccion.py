# Escribir un programa que pregunte al usuario el nombre, numero de horas trabajadas, costo por hora, y debe mostrar un mensaje por el total de hora

print ("hola bienvenido podria digitar su nombre")
nombre = (str(input("su nombre por porfavor")))

print (" ahora porfavor digite cuantas horas trabajo y su costo por hora")
numeroHoras = (int(input("cuantas horas trabajo")))
CostoPorhora = (int(input("cuantos es el costo de hora de trabajo")))

totalhoras = numeroHoras * CostoPorhora 

print (f"\n Al trabajador : {nombre}, se le deben una cantidad de horas : {numeroHoras}, por un costo total de {totalhoras} ") 