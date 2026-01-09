'''Exercício 1: Classificação de Triângulos

Crie um programa que determine e imprima o tipo de um triângulo com base nos comprimentos dos seus três lados.

    Colete os comprimentos dos três lados (A, B e C) do usuário.

    Considere que os lados são números inteiros, mas garanta a coerção de tipos correta.

    Implemente a lógica condicional (if/elif/else) para classificar o triângulo:

        Equilátero: Todos os lados são iguais.

        Isósceles: Apenas dois lados são iguais.

        Escaleno: Todos os lados são diferentes.

    Use uma f-string na saída para imprimir o resultado da classificação.'''
# print('Calculo de formação de triângulos!!')
# reta1 = input('Informe o comprimento da primeira reta: ')
# reta2 = input('Informe o comprimento da segunda reta: ')
# reta3 = input('Informe o comprimento da terceira reta: ')
# reta1_float=float(reta1)
# reta2_float=float(reta2)
# reta3_float=float(reta3)
# equi= reta1_float == reta2_float == reta3_float
# iso = reta2_float == reta1_float and reta1_float + reta2_float > reta3_float or reta2_float == reta3_float and reta2_float + reta3_float > reta1_float and reta1_float == reta3_float and reta1_float + reta3_float > reta2_float
# esc = reta1_float + reta2_float > reta3_float and reta2_float + reta3_float > reta1_float and reta3_float + reta1_float > reta2_float 
# if equi:
#     print('Equilátero: Todos os lados são iguais')
# elif iso:
#     print('Isósceles: Apenas dois lados são iguais.')
# elif esc:
#     print('Escaleno: Todos os lados são diferentes.')
# else:
#     print('Os fatores não formam um triângulo.')

# Peça duas notas ao usuário.
# Calcule a média e diga se o aluno está:

# Aprovado (média >= 7)

# Reprovado (média < 7)
import time
import os
def notas():
    try:
        print('*'*30)
        nota1=float(input('Informe a primeira nota: '))
        nota2=float(input('Informe a segunda nota: '))
        return (nota1+nota2)/2
    except ValueError:
        return None
while True:
    nota=notas()
    if nota is None:
        print('Erro de entrada')
    elif nota >=7:
        print('Você foi aprovado!!')
    else:
        print('Você está reprovado')
    saida=input('Deseja sair do programa digite 0')
    if saida =='0':
        print('Saindo do programa!')
        break
    time.sleep(2)
    os.system('cls')