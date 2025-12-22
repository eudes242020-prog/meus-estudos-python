'''Função serve para agrupar uma ação em um lugar,
dar um nome para essa ação,
e poder executá-la quando eu quiser,
sem repetir código'''
import time
import os
perguntas = [
    {
        'Pergunta': 'Qual é o tipo do valor retornado por input() em Python?',
        'Opções': ['int', 'float', 'str', 'bool'],
        'Resposta': 'str',
    },
    {
        'Pergunta': 'Qual operador usamos para comparar igualdade?',
        'Opções': ['=', '==', '!=', '==='],
        'Resposta': '==',
    },
    {
        'Pergunta': 'Qual estrutura usamos para repetir um bloco enquanto uma condição for verdadeira?',
        'Opções': ['for', 'if', 'while', 'def'],
        'Resposta': 'while',
    },
    {
        'Pergunta': 'Qual palavra-chave usamos para criar uma função em Python?',
        'Opções': ['function', 'def', 'fun', 'lambda'],
        'Resposta': 'def',
    },
    {
        'Pergunta': 'Qual método adiciona um item ao final de uma lista?',
        'Opções': ['add()', 'insert()', 'append()', 'push()'],
        'Resposta': 'append()',
    }
]
contador=0
def mostra_perguntas(pergunta_atual): # o codigo para rodar o programa começa aqui, estamos definindo uma função para rodar tudo com base
    print(f'{pergunta_atual["Pergunta"]}')          
    lista=pergunta_atual['Opções']
    for i, opcao in enumerate(lista,start=1):
        print(f'{i} {opcao}')
    opcoes = pergunta_atual["Opções"]
    try:
        escolha = int(input('Escolha uma opção: '))
        if escolha < 1:#as decições dentro do try sao as mais importantes pois elas evitam do programa quebra, oq seria horrivel para o usuario
            return False
        if escolha >len(opcoes):
            return False
        escolha_certa= escolha - 1
        if opcoes[escolha_certa] == pergunta_atual ['Resposta']:              
            return True
        return False
    except ValueError:
        return False

for numero,pergunta in enumerate(perguntas,start=1):#sim nossas repetições estão dentro do for, tanto na def quanto fora dela.
    print(f'Pergunta {numero} de {len(perguntas)}')
    if mostra_perguntas(pergunta):  #pensando em execução do codigo acho que é essa aqui, pois ele executa a def que agente crio(verifica se a definição do def é verdadeira ou falsa)
        print('Você acertouuuu!!!')
        time.sleep(2)
        contador+=1
        os.system('cls')
    else:
        print(f'A resposta correta é {pergunta["Resposta"]}')
        time.sleep(2)
        os.system('cls')
print(f'Você acertou {contador} de {len(perguntas)}')# o programa finaliza aqui dando o feedback de quanto o usuario acertou

'''1️⃣ Definir função
  • recebe uma pergunta
  • mostra pergunta
  • mostra opções
  • pede escolha
  • retorna True/False

2️⃣ Programa principal
  • loop nas perguntas
  • chama a função
  • recebe True/False
  • soma contador
  • decide prints'''