lista = [
    [7, 5, 3, 3, 1, 7],
    [1, 5, 8, 8, 6, 9],
    [5, 3, 3, 9, 4, 1],
    ]

def primeiro_valor_duplicado(lista):
    numeros_checados = set()
    primeira_duplicada = -1

    for numeros in lista:
        if numeros in numeros_checados:
                primeira_duplicada = numeros
                break

        numeros_checados.add(numeros)

    return primeira_duplicada

for valores in lista:
    print(
         valores,
         primeiro_valor_duplicado(valores)
         )