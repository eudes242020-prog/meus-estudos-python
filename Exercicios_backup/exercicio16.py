'''Tente adivinhar o número entre 0 e 100!
Digite seu chute: 50
O número secreto é MAIOR que 50.

Digite seu chute: 75
O número secreto é MENOR que 75.

Digite seu chute: 60
VOCÊ ACERTOU! O número era 60.
Tentativas: 3'''
import os
import random
import time
numero_secreto = random.randint(0, 100)
tentativas = 0
try:
    while True:
        os.system('cls')
        chute = int(input('Digite um numero: '))
        if chute > 100:
            print('Apaenas é permitido números entre 0 e 100')
            continue
        if chute < 0 :
            print('Apaenas é permitido números entre 0 e 100')
            continue
        if chute < numero_secreto:
            print(f'O número secreto é Maior que {chute}')
            tentativas += 1
            time.sleep(4)
        elif chute > numero_secreto:
            print(f'O número secreto é Menor que {chute}')
            tentativas += 1
            time.sleep(4)
        else:
            print(f'Você acertou!!! o número era {numero_secreto}')
            print(f'Tentativas: {tentativas}')
            break
except ValueError:
    print('Apenas número pode ser digitado')