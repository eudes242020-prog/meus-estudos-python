'''Enunciado

Crie uma lista com 4 frutas

Mostre numeradas (1 a 4)

Peça ao usuário para escolher

Se escolher certo índice:

mostre a fruta escolhida

Se errar:

mostre “opção inválida”'''
frutas = ['Morango', 'Laranja', 'Figo', 'Melância']
for i , fruta in enumerate(frutas,start=1):
    print(f'{i} {fruta}')
try:
    escolha=int(input('Escolha uma das frutas: '))
    if  1<= escolha <=len(frutas):
        print(f'A fruta escolhida foi {frutas[escolha-1]}')
    else:
        print('Opção inválida!!')
except ValueError:
    print('Somente números inteiro!!')

