questoes = [{
            'pergunta': 'Quanto é 1 - 1?',
            'opções': ['1', '3', '0'],
            'resposta': '0'
},
             {
            'pergunta': 'Quanto é 2 + 2?',
            'opções': ['4', '7', '11'],
            'resposta': '4'
             }]

total_de_acertos = 0

for questao in questoes:
    pergunta = questao['pergunta']
    opcoes = questao['opções']
    resposta = questao['resposta']

    print(pergunta)
    print('opções:')
    
    for alternativa in opcoes:
        print(alternativa)

    escolha = input('Escolha uma das respostas acima: ')   

    if escolha == resposta:
        total_de_acertos += 1
        print('Pabens você acertou')
    else:
        print('Você errou') 

print(f'Você acertou {total_de_acertos} / {len(questoes)}')