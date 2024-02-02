# Crear una tupla con nombres de frutas y acceder a un elemento específico.

def EntrarEnFruta(frutas):
    nombre = input("Digite un elemento en la tupla fruta ")
    for i in frutas : 
        if nombre == i:
            print("El elemento es: ", i)
        




frutas = ("manzana", "pera", "kiwi", "melón")
print(f"\n la tupla fruta contiene : {frutas}")

EntrarEnFruta(frutas) 