nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é pequeno!")

    if tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é médio")

    if tamanho_nome > 6:
        print("Seu nome é muito grande!")     

else:
    print("Por favor, digite mais de uma letra")