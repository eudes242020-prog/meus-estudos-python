# TÓPICO: 02 Operadores Aritmeticos

# ==============================================================================
# ORIGINAL: Revisoes/revisao10.py
# ==============================================================================

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz '
print(a_dez_vezes)
print(tres_vezes_luiz)

# ==============================================================================
# ORIGINAL: Revisoes/revisao11.py
# ==============================================================================

'''
Precedência
1. (n + n)
2. **
3. * / // %
4. + -
'''
conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

# ==============================================================================
# ORIGINAL: Revisoes/revisao13.py
# ==============================================================================

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2
linha1= f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'
print(linha1)
print(linha2)
print(linha3)

# ==============================================================================
# ORIGINAL: Revisoes/revisao15.py
# ==============================================================================

#nome = input('Qual seu nome? ')
numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

#print(f'O seu nome é {nome}')
print(f'A soma dos números é: {numero1+numero2}')

# ==============================================================================
# ORIGINAL: Revisoes/revisao25.py
# ==============================================================================

'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X -Hexadecimal(ABCDEF0123456789)
'''
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' %(1500, 1500))

# ==============================================================================
# ORIGINAL: Revisoes/revisao26.py
# ==============================================================================

'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:0^10}')
preco = 1000.95897643
print(f'{1000.95897643:,.1f}')

# ==============================================================================
# ORIGINAL: Revisoes/revisao3.py
# ==============================================================================

'''
Python =  Linguagem de programação
Tipo de ipagem = Dinânmica / Forte
str -> string -> texto
Strings são textos ue estão denro de aspas
'''

#Aspas simples
print('Luiz Otávio')
print('Luiz "Otávio"')
#Aspas duplas
print("Luiz Otávio")
print("Luiz 'Otávio'")
#Escape
print("Luiz \"Otávio\"")
#r
print(r"Luiz \"Otávio\"")

# ==============================================================================
# ORIGINAL: Revisoes/revisao4.py
# ==============================================================================

'''
Tipos int e float
int -> Número inteiro
O tipo int representa qualquer número
positivo ou negativo. int sem sinal é considerado positivo.
'''
print(11) #int
print(-11) #int
print(0) 
'''float -> Número com ponto flutuante
O tipo float representa qualquer número
positivo ou neativo com ponto flutuante.
float sem sinal é considerado positivo'''
print(1.1, 10.11) #float
print(0.0, -1.5)
'''A função type mostra o tipo que o Python
inferiu ao valor
'''
print(type(1.5),type(-1.1),type(0.0))
print(type(1))
print(type('Otávio'))
print(type(-1))

# ==============================================================================
# ORIGINAL: Revisoes/revisao51.py
# ==============================================================================

'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
'''
lista_a = ['Eudes', 'Victoria']
lista_b = lista_a
lista_a[0] = 'Outra coisa'
print(lista_b)

# ==============================================================================
# ORIGINAL: Revisoes/revisao55.py
# ==============================================================================

'''
Imprecisão de ponto flutuante
'''
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(round(numero_3, 2))

# ==============================================================================
# ORIGINAL: Revisoes/revisao6.py
# ==============================================================================

'''
Conversão de tipo, coerção
type convertion, typecasting, coercion
é o ato de converter um tipo em outro
tipo imutáveis e primitivos:
str, int, float, bool
'''
print(1 + 1)
print('a' + 'b')
print(int('1'), type(int('1')))
print(int('1')+ 1)
print(type(float('1')+ 1))
print(bool(''))
print(str(11) + 'b')

# ==============================================================================
# ORIGINAL: Revisoes/revisao85.py
# ==============================================================================

# Módulos padrao do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# partes - from nome_modulo import objeto1, objeto2 
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# from sys import exit as ex, platform as pf
# print(pf)
# ex()

# má prática - from nome_modulo import *
# Vantagens: import tudo de um módulo
# Desvantagens: Importa tudo de um módulo

# from sys import *
# print(platform)

# ==============================================================================
# ORIGINAL: Revisoes/revisao9.py
# ==============================================================================

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10 
print('Multiplicação', multiplicacao)

divisao = 10 / 3
print('Divisão', divisao)

divisao_inteira = 10 // 2.2
print('Divisão interira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2 #resto da divisão
print('Módulo', modulo)

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex2(12).py
# ==============================================================================

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso/(altura*altura)
print(f'{nome} tem {altura:.2f} de altura')
print(f'pesa {peso} quilos e seu IMC é \n{imc:.2f}')

