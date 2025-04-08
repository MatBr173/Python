entrada = input("Digite as horas em números inteiros: ")

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print("Bom Dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa Tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa Noite!")
    else:
        print("Não conheço essa hora")
except:
    print("Por favor, digite apenas números inteiros")