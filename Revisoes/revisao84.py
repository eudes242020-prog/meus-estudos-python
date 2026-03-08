# raise - lançndo exceções(erros
# https://docs.python.org/3/library/exceptions.html)
def nao_aceito_zero(d):
    if d ==0:
        raise ZeroDivisionError('Divisão por zero não é permitida')
    return True

def numeros_inteiros_ou_floats(n,d):
    if not isinstance(n, (int,float)) or not isinstance(d, (int,float)):
        raise TypeError('Apenas números inteiros')
def divide(n, d):
    numeros_inteiros_ou_floats(n,d)
    nao_aceito_zero(d)
    return n/d

print(divide('8', 1)) 