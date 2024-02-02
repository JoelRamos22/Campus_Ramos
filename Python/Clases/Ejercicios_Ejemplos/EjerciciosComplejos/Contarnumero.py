def contar_ocurrencias(lista):
    elementos_unicos = []
    ocurrencias = []

    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
            ocurrencias.append(1)
        else:
            indice = elementos_unicos.index(elemento)
            ocurrencias[indice] += 1

    return elementos_unicos, ocurrencias

mi_lista = [1, 2, 3, 4, 1, 2, 1, 5]
elementos, ocurrencias = contar_ocurrencias(mi_lista)
print("Elementos en la lista y sus ocurrencias:")
for elemento, ocurrencia in zip(elementos, ocurrencias):
    print(f"Elemento {elemento}: {ocurrencia} veces")