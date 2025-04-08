def comparar_listas(lista_1, lista_2):
    return [elemento for elemento in lista_1 if elemento in lista_2]

lista_1 = [3, 2, 7]
lista_2 = [2, 5, 7]

print(comparar_listas(lista_1, lista_2))