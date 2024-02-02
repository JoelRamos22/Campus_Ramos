import time  
def menu(opciones, reservacion): 
    print("¿Que desea hacer? : ")
    opciones = int(input("\n1. Añadir Reserva\n2. Verificar disponibilidad\n3. Cancelar Reserva\n4. Salir\n"))
    while opciones != 4: 
        if opciones == 1: 
            Reservacion(reservacion)
        elif opciones == 2: 
            ListaR(reservacion)
        elif opciones == 3:
            cancelarR(reservacion)
        time.sleep(2)
        opciones = int(input("\n 1. Añadir Reserva\n2. Verificar disponibilidad\n3. Cancelar Reserva\n4. Salir\n"))
        if opciones == 4 : 
            print("\nSaliendo...")
            time.sleep (0.99)
            break 
def Reservacion(reservacion):
    nombre = str(input("Escriba el nombre con el que quiere guardar la reservacion: "))
    time.sleep(1)
    tipo = str(input("Digite el tipo de habitacion que desea reservar: "))
    time.sleep(1)
    duracion = int(input("Digite la estancia por la que va a rentar la habitacion: "))
    time.sleep(1)
    if tipo == "simple": 
        costo = 100 
        total = duracion * costo 
    elif tipo == "doble": 
        costo = 150 
        total = duracion * costo 
    elif tipo == "suite":
        costo = 200 
        total = duracion * costo 
    else:
        print("Tipo de habitación no válido")
        return
    reservacion.extend([nombre, tipo, duracion, total])
    print("\n", reservacion)
def cancelarR(reservacion):
    nombre = input("\n Ingrese el nombre de la reserva que desea cancelar: ")
    time.sleep(1)
    for i in range(0, len(reservacion), 3):  # Iterar sobre los nombres de las reservas
        if reservacion[i] == nombre:
            reservacion.pop(i)  # Eliminar el nombre
            reservacion.pop(i)  # Eliminar el tipo
            reservacion.pop(i)  # Eliminar la duración
            reservacion.pop(i)  # Eliminar el total
            print("\n Reserva cancelada con éxito.")
            return
    print("\n No se encontró ninguna reserva con ese nombre.")

def ListaR(reservacion):
    print("\n Reservas realizadas:")
    time.sleep(1)
    if len(reservacion) == 0:
        time.sleep(1)
        print("\nNo hay reservas.")
    else:
        for i in range(0, len(reservacion), 3):
            if i + 3 < len(reservacion):
                time.sleep(2)
                print("Nombre:", reservacion[i])
                print("Tipo:", reservacion[i+1])
                print("Duración:", reservacion[i+2])
                print("Total:", reservacion[i+3])
                print("--------")

menu([], [])
