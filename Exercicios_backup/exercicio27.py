# def multiplica(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
# multiplicacao = multiplica(1,2 ,3 ,4 ,5 )
# print(multiplicacao)

def verificar(*args):
    lista = []
    for numero in args:
        if numero % 2 !=1:
            lista.append('Par')
        else:
            lista.append('Impar')
    return lista
par_impar = verificar(10, 11, 35, 102)
print(par_impar)