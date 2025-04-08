def ordered_list(lista: list):
    n = len(lista)
    for i in range(n):
        for j in range(n - i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


list = [7, 2, 5, 1]
print(ordered_list(list))