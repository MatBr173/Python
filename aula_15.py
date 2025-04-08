while True:
    print('Escolha uma história: terror, aventura ou romance')
    print('Escolha apenas um deles')
    historia = input('')

    try:
        terror = "terror".lower()
        aventura = "aventura".lower()
        romance = "romance".lower()
        temas = terror, romance, aventura
    except:
        terror_true = True
        aventura_true = True
        romance_true = True
        temas = True

    if historia is None:
        print('esse tema não existe')
    elif historia is None:
        print('esse tema não existe')


    if historia == terror:
        print('era uma vez...')
    elif historia == aventura:
        print('era uma vez...')
    elif historia == romance:
        print('era uma vez...')
    else:
        print('inpossivel isso aparecer. tá aqui porque sim')


    sair = input('Deseja sair? '
                 'digite "s" para sim, e qualer letra para não ').lower().startswith('s')
    if sair is True:
        break