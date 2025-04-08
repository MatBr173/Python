senha = int(input('Digite a senha para entrar no sistema: '))
senha_do_sistema = 1234

if senha == senha_do_sistema:
    print('Você entrou no sistema')
elif senha != senha_do_sistema:
    print('Você não digitou a senha')