'''
enumerate - enumera iteráveis
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
#lista_enumerada = enumerate(lista)
for indice, nome in enumerate(lista):
    print(indice, nome)