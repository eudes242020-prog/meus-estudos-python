"""Escreve uma função que recebe uma lista de números e retorna a soma apenas dos números ímpares. Sem pesquisar, tenta do zero."""
numeros = [14, 3, 8, 21, 100, 55, 12, 7, 42, 1]
def soma(num):
    novo=0
    for numero in num:
        if numero % 2 == 1:
            novo+=numero
    return novo
print(soma(numeros))        