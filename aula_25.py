"""Imagine que você tem que pagar uma divida de R$ 2200.00, mas só tem R$ 300.00 na conta.
Crie uma função onde o usuario possa usar até R$ 300.00 para pagar a divida, e 
mostre o valor que resta ser pago"""

print('Você tem que pagar uma divida de R$ 2200.00, mas só tem R$ 300.00 na conta.' '\n'
'Escolha qual o valor você deseja inseris para pagar sua divida')

print()

value = float(input('Digite um valor de até R$ 300.00 para pagar sua divida: '))

if value <= 300:
    print(f'O valor pago foi {value}')
    rest = 2200 - value
    print(f'Você ainda deve {rest}')
else:
    print('Saldo insuficiente')