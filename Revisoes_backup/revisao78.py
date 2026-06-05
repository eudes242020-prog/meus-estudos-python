# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe')
    print(getattr(string, metodo)())
else:
    print('Não existe método', metodo)