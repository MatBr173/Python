while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+, -, *, /): ')
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
       numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos')
        continue

    if len(operador) > 1:
        print('Você digitou mais de um operador. Digite apenas um')
        continue    

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print('O operador digitado é invalido')
        continue

    print('O resultado de sua conta foi:')    
    if operador == '+':
        print(f"{numero_1_float} + {numero_2_float} = ", numero_1_float + numero_2_float)
    elif operador == '-':
        print(f"{numero_1_float} - {numero_2_float} = ", numero_1_float - numero_2_float)
    elif operador == '*':
        print(f"{numero_1_float} * {numero_2_float} = ", numero_1_float * numero_2_float)
    elif operador == '/':
        print(f"{numero_1_float} / {numero_2_float} = ", numero_1_float / numero_2_float)
    else:
        print('Se isso apareceu é porque ou você é burro' "\n"
'ou eu sou um pessimo programador')

    sair = input('Você quer sair?' "\n"
'digite [s] para sim, e qualquer tecla rapar não: ').lower().startswith('s')
    
    if sair is True:
        break