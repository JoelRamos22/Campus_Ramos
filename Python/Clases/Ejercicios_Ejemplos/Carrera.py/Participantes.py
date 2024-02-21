import json 

def Registrar_Participantes(opcion) : 
    while True : 
        if opcion == 1 : 
            print (" Entrando al menu de Registro Atletismo ")
            print ("")
            Añadir_Participantes_Atletismo()
            break
        elif opcion == 2 : 
            print (" Entrando al menu de Registro Ciclismo ")
            print ("")
            Añadir_Participantes_Ciclismo()
            break
        elif opcion == 3 : 
            print (" Entrando al menu de Registro Patinaje ")
            print ("")
            Añadir_Participantes_Patinaje()
            break 
        elif opcion == 4 :  
            print (" saliendo ... ")
            break
        else : 
            print (" Opcion incorrecta ")
            print ("")

def Añadir_Participantes_Atletismo() : 
    with open ('Participantes.json', 'r') as participantes_file : 
        data_participantes = json.load(participantes_file)
    
    while True : 
        confirmacion = input (" Desea añadir algun partcipante (s/n) ")
        if confirmacion.lower() == "s" : 
            nombre = input (" Ingrese el nombre del Participante: ")
            edad = int(input (" Ingrese la edad del Participante: "))
            residencia = input (" Ingrese su apartamento de residencia : ")
            for i in data_participantes['Atletismo'] : 
                if nombre.lower() == i['nombre'].lower() : 
                    print ("\n  El participante ya existe ") 
                    return False
            if residencia.lower() != "santander" : 
                print ("\n  Usted no vive en santander, no puede participar ") 
                break
            if edad < 18 : 
                print ("\n  Usted no tiene la mayoria de edad, no puede participar ") 
                break 
            nuevo_participante = {
                "nombre" : nombre,
                "edad" : edad,
                "residencia" : residencia,
            }
            data_participantes['Atletismo'].append(nuevo_participante)
            with open ('Participantes.json', 'w') as f: 
                json.dump(data_participantes, f, indent=4)
            print ("\n Participante Añadido con exito ")
        if confirmacion.lower() == "n" : 
            print ("\n Volviendo al menu principal")
            break 
    return 

def Añadir_Participantes_Ciclismo() : 
    with open ('Participantes.json', 'r') as participantes_file : 
        data_participantes = json.load(participantes_file)
    
    while True : 
        confirmacion = input (" Desea añadir algun partcipante (s/n) ")
        if confirmacion.lower() == "s" : 
            nombre = input (" Ingrese el nombre del Participante: ")
            edad = int(input (" Ingrese la edad del Participante: "))
            residencia = input (" Ingrese su apartamento de residencia : ")
            for i in data_participantes['Atletismo'] : 
                if nombre.lower() == i['nombre'].lower() : 
                    print ("\n  El participante ya existe ") 
                    return False
            if residencia.lower() != "santander" : 
                print ("\n  Usted no vive en santander, no puede participar ") 
                break
            if edad < 18 : 
                print ("\n  Usted no tiene la mayoria de edad, no puedo participar ") 
                break 
            nuevo_participante = {
                "nombre" : nombre,
                "edad" : edad,
            }
            data_participantes['Ciclismo'].append(nuevo_participante)
            with open ('Participantes.json', 'w') as f: 
                json.dump(data_participantes, f, indent=4)
            print ("\n Participante Añadido con exito ")
        if confirmacion.lower() == "n" : 
            print ("\n Volviendo al menu principal")
            break 
    return 

def Añadir_Participantes_Patinaje() : 
    with open ('Participantes.json', 'r') as participantes_file : 
        data_participantes = json.load(participantes_file)
    
    while True : 
        confirmacion = input (" Desea añadir algun partcipante (s/n) ")
        if confirmacion.lower() == "s" : 
            nombre = input (" Ingrese el nombre del Participante: ")
            edad = int(input (" Ingrese la edad del Participante: "))
            residencia = input (" Ingrese su apartamento de residencia : ")
            for i in data_participantes['Atletismo'] : 
                if nombre.lower() == i['nombre'].lower() : 
                    print ("\n  El participante ya existe ") 
                    return False
            if residencia.lower() != "santander" : 
                print ("\n  Usted no vive en santander, no puede participar ") 
                break
            if edad < 18 : 
                print ("\n  Usted no tiene la mayoria de edad, no puedo participar ") 
                break 
            nuevo_participante = {
                "nombre" : nombre,
                "edad" : edad,
            }
            data_participantes['Patinaje'].append(nuevo_participante)
            with open ('Participantes.json', 'w') as f: 
                json.dump(data_participantes, f, indent=4)
            print ("\n Participante Añadido con exito ")
        if confirmacion.lower() == "n" : 
            print ("\n Volviendo al menu principal")
            break 
    return 

