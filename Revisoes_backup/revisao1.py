import os

secreta = 'computador'
letras_acertadas = ''
tentativas = 0

print('--- INICIANDO JOGO (DEBUG MODE) ---')

while True:
    letra_digitada = input('Digite uma letra: ').lower().strip() # Resolve maiúsculas e espaços
    tentativas += 1

    # --- Validações ---
    if len(letra_digitada) > 1:
        print('ERRO: Digite apenas uma letra.')
        continue
    
    if letra_digitada.isdigit():
        print('ERRO: Não digite números.')
        continue

    # --- O Segredo: Guardar a letra ---
    if letra_digitada in secreta:
        letras_acertadas += letra_digitada
        # Print espião para confirmar que salvou
        print(f'>> ACERTOU! Letras que você já tem: {letras_acertadas}')
    
    # --- O Scanner (Montar a palavra) ---
    palavra_formada = ''
    for letra_secreta in secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    # --- O Resultado Visual ---
    print('--------------------------------')
    print(f'PALAVRA: {palavra_formada}')
    print('--------------------------------')
    
    # --- Vitória ---
    if palavra_formada == secreta:
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela no final
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', secreta)
        print('Tentativas:', tentativas)
        break