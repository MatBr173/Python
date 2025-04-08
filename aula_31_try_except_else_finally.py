try:
    number_1 = int(input('Digite um numero: '))
    number_2 = int(input('Digite outro numero: '))
    sum = number_1 + number_2

    print('a soma de ambos os numeros é ', sum)

except ValueError as error_value:
    print('Erro no valor digitado', error_value)

else:
    print("Reinicie caso queira fazer o calculo novamente")

finally:
    print("Programa finalizado")