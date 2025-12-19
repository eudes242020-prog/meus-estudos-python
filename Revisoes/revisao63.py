'''
args - Argumentos não nomeaados
* - *args (empcotamento e desempacotamento)
'''
#Lembre-te de desempacotamento
def soma(*args):
    total = 0
    for numero in args:
        total+=numero
    return total
soma_total=soma(1,3,4,6,8)
print(soma_total)
