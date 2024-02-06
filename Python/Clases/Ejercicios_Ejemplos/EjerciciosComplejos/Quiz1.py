# Ejercicio numero 1 Stock para tienda 

# Hacemos un import time para hacer que en su ejecucion el codigo se vea mucho mas pulcro y agradable a la vista
import time 

# definimos la funcion que usaremos para el menu de opciones
def menu(opciones,Producto):
    # Iniciamos un bucle while para el menu con una condicion definida para como != 5 que sera nuestra opcion para salir 
    while opciones != 5 : 
        # hacemos que al entrar a cada opcion haga su respectiva funcion 
        if opciones == 1 : 
            print (" Entrando al menu del stock ")
            print ("")
            time.sleep(1)
            AñadirProducto(Producto)
        elif opciones == 2 : 
            print (" Entrando al menu de actualizacion ")
            print ("")
            time.sleep(1)
            ActualizarProducto(Producto)
        elif opciones == 3 : 
            print (" Entrando al menu de eliminacion ")
            print ("")
            time.sleep(1)
            EliminarProducto(Producto)
        elif opciones == 4 :
            print (" Mostrando Stock ")
            print ("")
            time.sleep(1)
            mostrarStock(Producto)
        time.sleep(1)
        # al llegar a esta parte solo repetimos el ciclo si el usuario no ha pulsado 5 mostrandole de nuevo las opciones
        print (" ¿ Que desea hacer ? ")
        opciones = int(input("\n1. Añadir Producto\n2. Actualizar Producto\n3. Eliminar Producto\n4. Ver stock\n5. salir del sistema\n"))
        # si el usuario escoge la opcion 5 solo se imprimira un mensaje de saliendo del sistema
        if opciones == 5 : 
            time.sleep(1)
            print ("\n saliendo...")
            break

# Empezamos nuestra funcion de añadir producto 
def AñadirProducto(Producto):
    # le decimos al usuario que digite el nombre con el que quiere agregar el producto, su precio y su cantidad 
    nombre = input("\n Ingrese el nombre del producto: ")
    time.sleep(1)
    precio = int(input(" Ingrese el precio del producto: "))
    time.sleep(1)
    cantidad = int(input(" Ingrese la cantidad del producto: "))
    time.sleep(1) 
    # hacemos una condicion if que busque el nombre del producto registrado si este ya esta dentro del diccionario le pedira que registre un nuevo nombre al final de la busqueda de valores 
    if nombre in Producto : 
        print (" Este producto ya se encuentra registrado porfavor indica un nuevo nombre e intente subir los datos de nuevo")
    else : 
        # guardamos el producto como una clave, cuyos valores seran una lista de precio y cantidad
        Producto[nombre] = [precio, cantidad]
        time.sleep(0.95)
        # imprimimos un mensaje para cuando el producto este añadido 
        print("\n Producto añadido con éxito")
        print (Producto)
        print ("")
    
# iniciamos la funcion para actualizar la cantidad de algun producto existente 
def ActualizarProducto(Producto): 
    # le pedimos que ingrese el nombre del producto y hacemos un ciclo for para buscarlo 
    nombre = input("\n Ingrese el nombre del producto: ")
    for i in Producto : 
        if nombre in Producto : 
            # si el nombre esta dentro de producto le pedimos que ingrese su nuevo precio y cantidad y guardamos estos datos 
            precio = int(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            Producto[nombre] = [precio, cantidad]
            time.sleep(1)
            # le mostramos un mensaje para decirle el que el producto se añadio con exito 
            print("\n Producto actualizado con éxito")
            # imprimimos sus nuevos datos
            print (Producto)
            break
        elif nombre not in Producto : 
            # si el nombre no esta en el producto solo vamos a decir que no se ha encontrado el producto con ese nombre
            time.sleep(1)
            print("\n No se encontró ningún producto con ese nombre.")
            print ("")
            
# iniciamos la funcion para eliminar productos  
def EliminarProducto(producto):
    # buscamos el producto por nombre e iniciamos un ciclo
    nombre = input(" Ingrese el nombre del producto: ")
    for i in producto : 
        # si el nombre esta dentro del diccionario haremos producto.pop ("nombre") para eliminar la clave y su contenido 
        if nombre in producto : 
            producto.pop(nombre)
            time.sleep(0.80)
            # imprimimos un mensaje para mostrarle que se ha completado la eliminacion exitosamente 
            print("\n Producto eliminado con éxito")
            print ("")
            break
        elif nombre not in producto : 
            #como manejo de errores si el producto no esta dentro del diccionario imprimiremos que no se ha encontrado el producto 
            time.sleep(1)
            print("\n No se encontró ningún producto con ese nombre.")
            print ("")

# iniciamos la funcion para mostrar el stock de productos y sus precios totales 
def mostrarStock(producto):
    # mostramos el stock que tenemos actualmente 
    print("Stock de productos:")
    print ("")
    # como manejo de error para cuando no hay productos almanacenados en el diccionario solamente usamos una condicion if que cuente si la cantidad de valores dentro de "productos" es mayor a 0 usamos para esto un len 
    if len(producto) > 0 :
        # si la cantidad de productos es mayor a 0 usamos un for con el nombre, datos que sera nuestro iterable in producto.items para obtener los items de producto
        for nombre, datos in producto.items():
            # iniciamos que precio = datos [0] y cantidad [1] hacemos esto para que a la hora de imprimirlo sea mas facil para el usuario poder leerlo 
            precio = datos[0]
            cantidad = datos[1]
            time.sleep(0.95)
            # gracias a esto podemos realizar un impresion del resultado mucho mas ordenada 
            print(f"\n Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")
            print ("")
            # llamamos la funcion calcular precio total del producto para mostrar cuanto es el valor del total del stock que llevamos hasta el momento 
            total = calcularTotalPrecio(producto)
            time.sleep(1)
            # imprimimos el precio total 
            print (" El precio total de los productos es : ", total)
            print ("")
            time.sleep(0.95)
    else : 
        # si la cantiad de productos es menor a 0 solamente imprimimos que no hay producto en el stock
        time.sleep(1)
        print("\n No se encontraron productos")
        print ("")

# iniciamos la funcion para calcular el precio total del stock 
def calcularTotalPrecio(producto):
    # iniciamos una variable como total_precio dentro de nuestra funcion , usamos el metodo suma con (datos[0]) y for para datos in producto.values() que nos dara los valores de cada clave dentro de producto y datos que era nuestro iterable mas arriba
    total_precio = sum(datos[0] for datos in producto.values())
    # al final solo retornamos el precio total 
    return total_precio

# para nuestro algoritmo solamente imprimimos el mensaje hola usuario junto con las opciones y un diccionario vacio que sera nuestro Producto 
print (" Hola usuario ")
print ("")
opciones = int(input("\n1. Añadir Producto\n2. Actualizar Producto\n3. Eliminar Producto\n4. Ver stock\n5. salir del sistema\n"))
Producto = {}
# llamamos a la primera funcion menu 
menu(opciones,Producto)