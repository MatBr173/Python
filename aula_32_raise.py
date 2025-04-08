def zero(s):
    if s == 0:
        raise ZeroDivisionError('Zero não divide meu querido')
    return True

def nao_multiplicar_zero(n, s):

    zero(s)

    if not isinstance(n, (int, float)):
        raise TypeError('Tem que ser int ou float')
    
    if not isinstance(s, (int, float)):
        raise TypeError('Tem que ser int ou float')
    
nao_multiplicar_zero(8, 0)    

print(nao_multiplicar_zero)

