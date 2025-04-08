entrada = input("Digite {sim} para entrar no sistemas: ").lower()

if entrada == "sim":
    print("Você entrou")
elif entrada == "não":
    print("Você saiu do sistema")
else:
    print("Você não digitou nada")