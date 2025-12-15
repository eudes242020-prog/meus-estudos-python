'''
Faça um programa que peça ao usuário oara digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro
, informe que não é um número inteiro
'''
try:
    numero = input ('Digite um número inteiro: ')
    numero_int = int(numero)
    par = numero_int % 2 == 0

    if par:
        print('O número informado é PAR!')
    else:
        print('O número informado é ÍMPAR')
except:
    print('O que foi digitado não é um número inteiro')