'''Tente escrever o código seguindo exatos passos abaixo:
    Configuração Inicial: Defina a palavra secreta, a lista de acertos (string vazia), erros (0) e o limite de vidas.
    Entrada no While:
        Passo 1 (Visual): Mande limpar a tela (os.system).

        Passo 2 (Renderização): Monte a "palavra formada" (aquela lógica do for com *).

        Passo 3 (HUD): Dê o print na palavra_formada e mostre quantas vidas restam.

        Passo 4 (Checagem de Vitória): Se a palavra formada for igual à secreta -> Avisa que ganhou e dá break.

        Passo 5 (Checagem de Derrota): Se o número de erros estourou o limite -> Avisa que perdeu (mostra a secreta) e dá break.

        Passo 6 (Input): Só agora peça o input do usuário.

        Passo 7 (Validação): Verifique se é número ou se tem mais de uma letra (use continue).

        Passo 8 (Lógica):

            Se a letra está na secreta: Adicione aos acertos.

            Se NÃO está: Aumente o contador de erros.'''
import os
import time
secreta = 'computador'
palavra_acertada = ''
tentativas = 0
limite_max = 5
while True:
    os.system('cls')
    palavra_formada=''
    for letra in secreta:
        if letra in palavra_acertada:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(f'Palavra: {palavra_formada}')
    print(f'Vidas restantes: {limite_max - tentativas}')
    print('---------------------------')
    if palavra_formada == secreta:
        print('VOCÊ GANHOU!!! PARABÉNS!')
        break
    letra_digitada = input('Digite uma letra: ').lower
    if len(letra_digitada)>1:
        print('Não é possivel escrever mais de uma letra')
        time.sleep(2)
        continue
    if letra_digitada.isdigit():
        print('Somente letra pode ser digitada!')
        time.sleep(2)
        continue
    if letra_digitada in secreta:
        palavra_acertada += letra_digitada
    else:
        tentativas+=1
        if tentativas >= limite_max:
            os.system('cls') 
            print('GAME OVER!! Você perdeu.')
            print(f'A palavra secreta era: {secreta}')
            break
