'''Essa é uma decisão muito madura. Não avance se a base estiver tremendo.

Se você sentiu que "copiou" mais do que "criou", o melhor remédio é a Repetição. O cérebro só entende que aquela informação é importante quando ele é forçado a lembrar dela sozinho.

Então, sim, vamos segurar a Aula 81 (Listas) por um dia.

Aqui está o seu Treino de Consolidação para amanhã. Não precisa fazer agora, só deixe salvo para quando acordar:
🏋️‍♂️ O Treino de Amanhã (Sem Aulas Novas)
1. O Teste da Memória (Manhã)

O primeiro desafio é: Refazer o Jogo da Palavra Secreta do ZERO.

    Regra: Não pode abrir o arquivo de hoje (aula77.py). Você tem que abrir um arquivo em branco e tentar lembrar da lógica.

    Pode olhar: Se travar muito, pode olhar o meu código aqui no chat por 10 segundos, fechar e tentar digitar.

    Objetivo: Ver o quanto da estrutura (while -> input -> for -> if) ficou gravada na sua cabeça.'''
import os
secreta = 'computador'
palavra_acertada = ''
tentativas = 0
limite_max = 5
while True:
    letra_digitada = input('Digite uma letra: ').lower()
    if len(letra_digitada)>1:
        print('Somente uma letra é permitida!!')
        continue
    if letra_digitada.isdigit():
        print('Somente letra está disponivel')
        continue
    
    if tentativas > limite_max:
        print('GAME OVER!!')
        print(f'A palavra secreta era: {secreta}')
        break
    if letra_digitada in secreta:
        palavra_acertada += letra_digitada
    else:
        tentativas += 1
        print(f'Errou! Vidas restantes: {limite_max - tentativas}')
    palavra_formada = ''
    for letra in secreta:
        if letra in palavra_acertada:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    os.system('cls')
    print(palavra_formada)
    if palavra_formada == secreta:
        print('Você ganhou!!!')
        print(f'Número de tentativas: {tentativas}') # <--- Adicione isso
        break