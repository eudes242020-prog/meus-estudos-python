# TÓPICO: 07 Lacos De Repeticao For

# ==============================================================================
# ORIGINAL: Exercicios/exercicio15.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio17.py
# ==============================================================================

'''O Desafio: Contador de Vogais

Seu objetivo é criar um código que:

    Peça para o usuário digitar uma frase qualquer.

    Use um for para passar letra por letra.

    Conte quantas vogais (a, e, i, o, u) existem nessa frase.

    Mostre o total no final.

Dica de lógica: Você vai precisar de uma variável contador = 0. Dentro do for, você pergunta: if letra in 'aeiou': -> Se for verdade, contador += 1.'''
frase = input('Digite uma frase: ').lower()
contador = 0
for letra in frase:
    if letra in 'aeiou':
        contador += 1
print(f'A frase escrita tem {contador} vogais')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio18.py
# ==============================================================================

frase =  'o rato roeu a roupa do rei de roma'
nova_frase=''
for letra in frase:
    if letra in 'aeiou':
        nova_frase += '*'
    else:
        nova_frase+=letra
print(nova_frase)

# ==============================================================================
# ORIGINAL: Exercicios/exercicio19.py
# ==============================================================================

frase= input('Digite uma frase ou palavra: ')
nova_frase = ''
for letra in frase:
    nova_frase += letra +'-'
print(nova_frase)

# ==============================================================================
# ORIGINAL: Exercicios/exercicio20.py
# ==============================================================================

'''Desafio: O Espelho (Inverter a Palavra)
Esse é um clássico de entrevistas de emprego para iniciantes. Quero ver se você consegue usar a lógica do for, mas mudando a ordem das coisas.
O Objetivo: O usuário digita uma palavra e o programa mostra ela ao contrário.
Exemplo:
    Entrada: AMOR
    Saída: ROMA
A Dica de Ouro (Lógica): No exercício anterior, você fez nova_frase += letra (que é igual a nova_frase = nova_frase + letra). Ou seja: o novo entra no final da fila.
Para inverter, você precisa colocar a letra nova no começo da fila.

    A equação muda: nova_frase = letra + nova_frase

Tente implementar isso! Sem usar +=, usando a soma manual para controlar a ordem.'''
frase = input('Digite uma palavra: ')
nova_frase  =''
for letra in frase:
    nova_frase = letra + nova_frase
print(nova_frase)

# ==============================================================================
# ORIGINAL: Exercicios/exercicio21.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio_duplicado32.py
# ==============================================================================

pessoas=[
    {'nome': 'Ana',
    'idade': 28,
    'profissão': 'Designer'}
]
for pessoa in pessoas:
    print(f'p')
print(f"Nome:{pessoas[0]['nome']}")
print(f"Idade: {pessoas[0]['idade']}")
print(f"Profissão: {pessoas[0]['profissão']}")

# ==============================================================================
# ORIGINAL: Revisoes/estudos_teoricos/validar_cpf.py
# ==============================================================================

import time
import os
while True:
    os.system('cls')
    cpf_limpo = ''
    cpf_sujo =input('Informe seu cpf: ')
    for valor in cpf_sujo:
        if valor.isnumeric():
            cpf_limpo += valor
    if len(cpf_limpo) == 0:
        print('Você não digitou números.')
        time.sleep(2)
        continue
    primeiro_caractere = cpf_limpo[0]
    sequencia_repetida = primeiro_caractere * len(cpf_limpo)
    if cpf_limpo == sequencia_repetida:
        print('Você digitou dados sequenciais!')
        continue
    nove_digitos = cpf_limpo[:9] 
    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1-=1
    verificador_1 = (resultado_digito_1*10) % 11
    if verificador_1 >9:
        verificador_1 = 0
    dez_digitos = nove_digitos + str(verificador_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2+=int(digito) * contador_regressivo_2
        contador_regressivo_2-=1
    verificador_2 = (resultado_digito_2 *10) % 11
    if verificador_2 >9:
        verificador_2 = 0
    cpf_calculado = f'{nove_digitos}{verificador_1}{verificador_2}'
    if cpf_limpo == cpf_calculado:
        print(f'O CPF {cpf_sujo} é VÁLIDO ')
    else:
        print(f'O CPF {cpf_sujo} é INVÁLIDO ')
    sair=input('Deseja sair do programa: [s]im ou [n]ão: ').lower()
    if sair =='sim':
        print('Saindo do programa!')
        break

# ==============================================================================
# ORIGINAL: Revisoes/revisao1.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Revisoes/revisao42(ex).py
# ==============================================================================

frase = 'O Python é uma linguagem de programação '\
    'multiparadiga. '\
    'Python foi criado por Guido van Rossum.'

recorde = 0
vencedora = ''

for letra in frase:
    if letra == ' ':
        continue
    qtd_atual = frase.count(letra)
    if qtd_atual > recorde:
        recorde = qtd_atual      
        vencedora = letra  
print(f'A letra "{vencedora}" venceu com {recorde} aparições.')

# ==============================================================================
# ORIGINAL: Revisoes/revisao43.py
# ==============================================================================

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
print(novo_texto)

# ==============================================================================
# ORIGINAL: Revisoes/revisao44.py
# ==============================================================================

'''
For + Range
range -> range (start, stop, step)'''
numeros = range(0, 10, 2)
for valor in numeros:
    print(valor)

# ==============================================================================
# ORIGINAL: Revisoes/revisao46.py
# ==============================================================================

for i in range(10):
    if i == 2:
        print('i é 2, pulando..')
        continue
    if i == 8:
        print('i é 8, seu else não executará')
        break
    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso')

# ==============================================================================
# ORIGINAL: Revisoes/revisao47(ex).py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Revisoes/revisao56.py
# ==============================================================================

'''
split e join com list e str
split - divide uma string
join - une uma string
'''
frase =' olha so que, coisa interessante'
lista_frase = frase.split()

for i, frase in enumerate(lista_frase):
    lista_frase[i] = lista_frase[i].strip()
print(lista_frase)
p = 'Python'
frase_juntas = '*'.join(p)
print(frase_juntas)

# ==============================================================================
# ORIGINAL: Revisoes/revisao66.py
# ==============================================================================

#manipulando o dicionario
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# for chave in pessoa:
    # print(chave, pessoa[chave])
chave = 'nome'

pessoas={}
pessoas[chave] = 'Eudes Goncalves'
del pessoa['sobrenome']
if pessoas.get('sobrenome') is None:
    print('Não existe')
    
print(pessoas)

