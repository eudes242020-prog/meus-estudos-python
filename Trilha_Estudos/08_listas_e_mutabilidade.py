# TÓPICO: 08 Listas E Mutabilidade

# ==============================================================================
# ORIGINAL: Exercicios/exercicio15(2).py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio22.py
# ==============================================================================

'''Exercício
exiba os índices da lista
0 maria
1 helena
2 luiz
'''

lista = ['Maria', 'Helena', 'Luiz']
vezes = 0
for nome in lista:
    print(f'{vezes} {nome}')
    vezes += 1

# ==============================================================================
# ORIGINAL: Revisoes/revisao48(list).py
# ==============================================================================

'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
COnhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create, Read, Update,  Delete
Criar,  ler,  alterar, apagar = lista[i](CRUD)
'''
lista = ['Victoria', 'Eudes', 'Dora', 'Isla', 'Yasmim']
lista.append(10)
lista.pop()
lista.pop()
lista.append(20)
print(lista)

# ==============================================================================
# ORIGINAL: Revisoes/revisao48.py
# ==============================================================================

'''
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - ídices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
'''
lista = [123, True, 'Luiz Otávio', 1.2, []]

# ==============================================================================
# ORIGINAL: Revisoes/revisao49.py
# ==============================================================================

'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido (primeiro argumente é onde vc quer inserir e o segundo é qual valor vc quer inserir)
    pop - Adiciona um item no índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i](CRUD)
'''
lista=[10, 20, 30, 40, 50, 60]
lista.append(90)
lista.insert(0, 100)
del lista[-1] #nesse caso funciona igual ao comando pop()

print(lista)

# ==============================================================================
# ORIGINAL: Revisoes/revisao50.py
# ==============================================================================

'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido (primeiro argumente é onde vc quer inserir e o segundo é qual valor vc quer inserir)
    pop - Adiciona um item no índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i](CRUD)
'''
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b #faz a concatenação das lista
lista_a.extend(lista_b) # junta as lista dentro da primeira colocando o valor da variavel na lista

# ==============================================================================
# ORIGINAL: Revisoes/revisao54.py
# ==============================================================================

'''
enumerate - enumera iteráveis
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
#lista_enumerada = enumerate(lista)
for indice, nome in enumerate(lista):
    print(indice, nome)

# ==============================================================================
# ORIGINAL: Revisoes/revisao57.py
# ==============================================================================

'''lista de listas e seus índices
'''
salas = [
      #0       #1
    ['Maria', 'Helena'],#0
     #0
    ['Elaine'],#1
     #0       1       2
    ['Luiz', 'João', 'Victoria',]#2
]
#print(salas[2][3][2])
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

# ==============================================================================
# ORIGINAL: Revisoes/revisao74.py
# ==============================================================================

lista=[]
for x in range (3):
    for y in range (3):
        lista.append((x,y))
lista = [
    (x, y) 
    for x in range(3) 
    for y in range(3)
]
print(lista)

# ==============================================================================
# ORIGINAL: Revisoes/revisao76.py
# ==============================================================================

#isinsace - para saber se objeto é de deteminado tipo
lista = [
    'a',1, 1.1, True, [0,1,2], (1,2),
    {0,1},{'nome': 'Luiz'}
]
for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item,isinstance(item, set))
    elif isinstance(item, str):
        print(item.upper(),isinstance(item, set))
    elif isinstance(item, (int,float)):
        print(item, item * 2)
    else:
        print('outro ', item)

