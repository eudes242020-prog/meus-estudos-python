'''
iterando strings com while
'''
i=0
nome = 'Luiz Otávio'
tamanho_nome = len (nome)
nova_string = ''
while i < tamanho_nome:
    letra = nome[i]
    nova_string += '*' + letra
    i += 1
print(nova_string)