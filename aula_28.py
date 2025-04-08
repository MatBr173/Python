string = 'Nome'
metodo_1 = 'upper'
metodo_2 = 'azul'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper)

if hasattr(string, metodo_1):
    print('Existe upper')
    print(getattr(string, metodo_1))
else:
    print('Não existe', metodo_1)

if hasattr(string, metodo_2):
    print('Existe upper')
    print(getattr(string, metodo_2))
else:
    print('Não existe', metodo_2)