# Crear un diccionario anidado con información de contactos.

diccionario1 = {
    "Juan": {
        "Nombre": "Juan",
        "Edad": 25,
        "Correo": "<EMAIL>",
    },
    "Pedro": {
        "Nombre": "Pedro",
        "Edad": 30,
        "Correo": "<EMAIL>",
    },
    "María": {
        "Nombre": "María",
        "Edad": 28,
        "Correo": "<EMAIL>",
    },
}
print(diccionario1["Pedro"]["Edad"], diccionario1["Pedro"]["Correo"])