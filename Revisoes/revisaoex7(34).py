'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letra, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande"
'''

nome = input ('Escreva seu primeiro nome: ')
quantidade_letras = len(nome)
nome_curto = quantidade_letras <= 4
nome_normal = 5 <= quantidade_letras <= 6

if nome_curto:
    print('Seu nome é curto!')
elif nome_normal:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')

