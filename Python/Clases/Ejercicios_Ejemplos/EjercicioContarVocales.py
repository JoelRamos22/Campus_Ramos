# Detector de Vocales: Implementa un script que identifique y cuente las vocales en una palabra ingresada.


def ContarVocales (palabra):
    vocales = 0
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" :
            vocales += 1
    return vocales

palabra = (str(input("ingrese una palabra ")))

vocales = ContarVocales (palabra)
print(vocales)