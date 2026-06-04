# TÓPICO: 06 Lacos De Repeticao While

# ==============================================================================
# ORIGINAL: Exercicios/exercicio7.py
# ==============================================================================

'''Desafio: O Contador de Letras "A" Quero que você escreva um código que:

    Tenha uma frase: frase = "O rato roeu a roupa do rei de Roma".

    Use um while para percorrer letra por letra (igual você fez agora).

    Dentro do while, use um if para ver se a letra atual é "r" (minúsculo) ou "R" (maiúsculo).

    Se for, aumente um contador (contador_r += 1).

    No final, mostre: "Achei X letras R".

Dica:

    Você vai precisar de um índice i = 0.

    Você vai precisar de um contador qtd_r = 0.

    Lembre-se: while i < len(frase):.'''

frase = "O rato roeu a roupa do rei de Roma"
frase_tamanho = len(frase)
i = 0
qtd_r = 0
while i < frase_tamanho:
    letra = frase[i]
    i += 1
    if letra in'rR':
        qtd_r += 1
print(f'Achei {qtd_r}')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio8.py
# ==============================================================================

''' Vamos manter o while, mas agora aumentar a pressão.

Regras:

    A senha é '1234'.

    O usuário tem apenas 3 tentativas.

    Use um contador (variável, ex: tentativas = 0) para controlar isso.

    O while deve continuar rodando enquanto a senha estiver errada E (and) o número de tentativas for menor que 3.

    Se acertar, imprima "Acesso permitido".

    Se gastar as 3 tentativas e errar, imprima "Conta bloqueada".

Dica: Você vai precisar incrementar o contador (tentativas = tentativas + 1 ou += 1) dentro do loop.'''
senha_secreta = '1234'
senha = input('Digite sua senha: ')
tentativa = 0
while senha_secreta != senha and tentativa < 2:
    tentativa+=1
    print('Senha incorreta! Tente novamente!')
    senha = input('Digite sua senha: ')
if senha == senha_secreta:
    print('Acesso permitido!')
elif tentativa <= 3:
    print('Conta Bloqueada')

# ==============================================================================
# ORIGINAL: Revisoes/revisao34.py
# ==============================================================================

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
condicao = True
while condicao:
    nome = input('Qual é seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break
print('Acabou')

# ==============================================================================
# ORIGINAL: Revisoes/revisao35.py
# ==============================================================================

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
contador = 0
while contador <= 10:
    print(contador)
    contador+=1
print('Acabou!!!')

# ==============================================================================
# ORIGINAL: Revisoes/revisao36.py
# ==============================================================================

"""
Operadores de atribuição
= += -= *= /= //= **= %="""

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
contador = 0
while contador <= 10:
    print(contador)
    contador+=1
print('Acabou!!!')

# ==============================================================================
# ORIGINAL: Revisoes/revisao37.py
# ==============================================================================

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
contador = 0
while contador <= 100:
    contador+=1
    if contador == 6:
        continue
    print(contador)
    if contador == 40:
        break
print('Acabou!!!')

# ==============================================================================
# ORIGINAL: Revisoes/revisao38.py
# ==============================================================================

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
qtd_linhas = 5
qtd_colunas = 5
linha = 1

while linha <= qtd_linhas:
    colunas= 1 
    while colunas <= qtd_colunas:
        print(f'{linha=} {colunas=}')
        colunas += 1
    linha += 1
    
print('Acabou')

# ==============================================================================
# ORIGINAL: Revisoes/revisao39.py
# ==============================================================================

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

