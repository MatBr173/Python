try:
    variavel_1 = float(input('Digite um valor: '))
    variavel_2 = float(input('Digite outro valor: '))
    variavel_3 = variavel_1, variavel_2

    if variavel_1 > variavel_2:
        print("O valor um é maior que o valor dois")
    elif variavel_1 < variavel_2:
        print("O valor um é menor que o valor dois")
    elif variavel_1 == variavel_2:
        print('Os valores são iguais')

except Exception as erro:
    print(f'Erro encontrado {erro.__class__}')
else:
    print(f'os numeros escolhidos foram {variavel_3}')
finally:
    print('O código acaba aqui')