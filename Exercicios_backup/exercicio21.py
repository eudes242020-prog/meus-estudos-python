'''Abra o while True.
Peça a senha (input).
Verificação 1: Se o tamanho for menor que 6 -> Mostre erro e continue.

Verificação 2: (A parte difícil):

    Crie uma variável tem_numero = 0 (ou um contador).

    Faça um for para passear pela senha.

    Se achar um dígito (.isdigit()), aumente o contador.

    Depois do for acabar, verifique: o contador ainda é 0? Se for -> Mostre erro "Precisa ter número" e continue.

Se passou por tudo isso: Mostre "Senha criada com sucesso!" e dê o break'''
import time
import os
while True:
    os.system('cls')
    tem_numero = 0
    senha=input('Escolha uma senha: ')
    if len(senha)<6:
        print('Erro: Senha fraca. coloque mais de 6 digitos')
        time.sleep(2)
        continue
    for letra in senha:
        if letra.isdigit():
            tem_numero += 1
    if tem_numero == False:
        print('Erro: Precisa ter pelo menos um número')
        time.sleep(2)
        continue
    
    print('Senha criada com sucesso!')
    break       

