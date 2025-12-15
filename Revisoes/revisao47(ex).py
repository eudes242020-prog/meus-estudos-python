"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
A "Memória" do Jogo: Você vai precisar guardar as letras que o usuário acertou. Uma string vazia ou uma lista pode servir?
O "Scanner" (O Loop for): A cada rodada, você tem que reconstruir a palavra na tela.
    Dica mental: "Para cada letra na palavra_secreta: se a letra estiver na minha lista de acertos, eu mostro ela. Se não, mostro um *."
A Condição de Vitória: Como o jogo sabe que acabou? (Talvez quando não tiver mais nenhum * na palavra montada?).
"""
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
        # AQUI É COM VOCÊ:
        # Se a 'letra_secreta' estiver dentro de 'letras_acertadas':
        #     palavra_formada += letra_secreta
        # Senão:
        #     palavra_formada += '*'
         # Apague isso e faça o if/else


#   1. Pede uma letra para o usuário
    
    # 2. Verifica se a letra é válida (se digitou só uma, se é número, etc)
    
    # 3. Processa a lógica (guarda a letra se acertou)
    
    # 4. Verifica se ganhou. Se ganhou -> break (para sair do while)