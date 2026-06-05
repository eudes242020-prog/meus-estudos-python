'''Essa é a atitude correta. Não adianta avançar se a base estiver tremendo. Quem domina o while domina a lógica de qualquer linguagem.

Para fechar o caixão do while e provar que você entendeu o erro de lógica do exercício anterior (o else e a indentação), vamos para um desafio que exige muita atenção no fluxo de decisão.
🎲 Desafio "Boss Final": O Jogo da Adivinhação

Dessa vez, não é um menu e não é uma soma. É um jogo de "Quente ou Frio". O computador vai ter um número secreto e o usuário tem que adivinhar. O while só para quando o usuário acertar.

A Lógica (Regras do Jogo):

    Defina um número secreto fixo no código (ex: secreto = 42).

    Crie uma variável para contar as tentativas (começa com 0).

    O programa pede um número (chute).

    O Loop (while): Enquanto o chute for diferente do segredo:

        Se o chute for maior que o segredo -> Avise: "Chute alto! Tente um número menor."

        Se o chute for menor que o segredo -> Avise: "Chute baixo! Tente um número maior."

        Importante: Conte a tentativa (+= 1) e peça outro chute dentro do loop.

    Final: Quando acertar (sair do loop), mostre: "Parabéns! Você acertou em X tentativas."'''

secreto = 42
tentativas = 0
try:
    chute = int(input('Chute um número: '))
    while chute!=secreto:
        tentativas+=1
        if chute > secreto:
            print('Chute alto! tente um número menor.')
        
        else:
            print('Chute baixo! tente um número maior.')
        chute = int(input('Chute um número: '))
    print(f'Parabéns! Você acertou em {tentativas+1} tentativas.')
except:
    print('Erro! Por favor digite um número!!')