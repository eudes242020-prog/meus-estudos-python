
import os
secreta = 'computador'
letras_acertadas = ''
tentativas = 0
while True:
    letra_digitada=input('Digite uma letra: ').lower()
    tentativas += 1
    if len(letra_digitada) > 1:
        print('Não é possivel coloca mais que uma letra!!') 
        continue
    if letra_digitada.isdigit():
        print('Erro, não é possivel escrever número')
        continue
    if letra_digitada in secreta:
        letras_acertadas += letra_digitada    
    palavra_formada = ''
    for letra_secreta in secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)
    if palavra_formada == secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', secreta)
        print('Tentativas:', tentativas)
        break
      

