
# empezamos creando la funcion para añadir tareas y definimos una prioridad de 5 
def AñadirTarea(nombre, prioridad=5):
    # usamos la funcion global para poder acceder una lista que este por fuera de las funciones 
    global tareas
    # definimos un diccionario que tendra las siguientes opciones clave """" nombre  """ y prioridad """" prioridad  """
    tarea = {'nombre': nombre, 'prioridad': prioridad}
    for t in tareas:
        # iniciamos un buble para iterar sobre la lista global 
        if t['nombre'] == nombre:
            # ponemos que si un elemento de la lista con la clave nombre sea igual a uno que ya este nos arroje un error de que la tarea ya fue creada 
            print(f"Error: La tarea '{nombre}' ya existe.")
            return
    # agregamos los valores a la lista tarea
    tareas.append(tarea)
    # imprimimos un mensaje que muestre la tarea junto con su prioridad 
    print(f"Tarea '{nombre}' añadida con prioridad {prioridad}.")

def mostrarTareas():
    global tareas
    # ordenamos la lista con las funciones """" sorted  """ que ordenan la lista de forma junto con (tareas, key=lambda t: t['prioridad'], reverse=True) usamos la lista """ tareas """ junto con key = lambad que lo que va a hacer es definirnos una variable como clave en este caso prioridad 
    tareas_ordenadas = sorted(tareas, key=lambda t: t['prioridad'], reverse=True)
    # imprimimos la lista de tareas 
    for t in tareas_ordenadas:
        print(f"{t['nombre']} - Prioridad {t['prioridad']}")

def EliminarTarea(nombre):
    global tareas
    # buscamos los elementos en tareas con el mismo nombre que queremos eliminar 
    for t in tareas:
        # si el nombre digitado es igual a un nombre dentro de la lista de elementos sera borrado 
        if t['nombre'] == nombre:
            tareas.remove(t)
            print(f"Tarea '{nombre}' eliminada.")
            # imprimiomos el mensaje para confirmar que fue eliminado 
            return
    print(f"Error: La tarea '{nombre}' no se encontró.")
    # si no esta simplemente se mostrar un mensaje despues del bucle diciendo que no se encontro la tarea 

def menu():
    # Iniciamos un bucle while para el menu y lo empezamos como true 
    while True:
        # opciones 
        print("\nMenú:")
        print("1. Añadir una nueva tarea.")
        print("2. Mostrar todas las tareas pendientes.")
        print("3. Eliminar una tarea.")
        print("4. Salir del programa.")
        opciones = int(input("Seleccione una opción: "))
        # if para elegir opciones 
        if opciones == 1:
            # que se pregunten las condiciones de cada funcion 
            nombre = input("Ingrese el nombre de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (por defecto 5): "))
            AñadirTarea(nombre, prioridad)
        elif opciones == 2:
            mostrarTareas()
        elif opciones == 3:
            nombre = input("Ingrese el nombre de la tarea a eliminar: ")
            EliminarTarea(nombre)
        elif opciones == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# iniciamos una lista de tareas vacia como lo pide el ejercicio 
tareas = []
menu()