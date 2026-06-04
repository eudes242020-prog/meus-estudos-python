# TÓPICO: 18 Tratamento De Excecoes Try Except

# ==============================================================================
# ORIGINAL: Exercicios/correcao2.py
# ==============================================================================

import os
import time
tarefas = [
    {"nome": "Estudar", "feito": False},
    {"nome": "Trabalhar", "feito": False},
]
menu=["Ver tarefas", 'Marcar tarefa como concluída', 'Desmarcar tarefa como concluída', ]
def mostrar_menu():
    print('------------')
    for item, tarefa in enumerate(menu, start=1):
        print(f'[{item}] {tarefa}')
    print('[0] Para sair')
def processa_opcao():
    mostrar_menu()
    try:
        numero=int(input('Qual opção deseja: '))
        if numero==0:
            return 'sair'
        if 1<= numero <=len(menu):
            if numero==1:
                mostrar_tarefa()
            elif numero==2:
                status = marcar_tarefa()
                mensagem=traduzir_status(status)
                return mensagem
            elif numero==3:
                status = desmarcar_tarefa()
                mensagem = traduzir_status(status)
                return mensagem
            else:
                return 'erro'
    except ValueError:
        return 'erro'       
def mostrar_tarefa():
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["feito"] else "❌"
        print(f'{i} {tarefa["nome"]} {status}')
def desmarcar_tarefa():
    if not tarefas:
        return 'vazio'
    mostrar_tarefa()
    try:
        escolha=int(input('Qual tarefa deseja desmarcar como concluida: '))
        if 1<=escolha<=len(tarefas):
            tarefas[escolha-1]['feito']=False
            return 'ok'
        return 'erro'
    except ValueError:
        return 'erro'
def marcar_tarefa():
    if not tarefas: 
            return 'vazio'
    mostrar_tarefa() 
    try:  
        escolha=int(input('Qual tarefa deseja marcar como concluida: '))
        if 1<=escolha<=len(tarefas):
            tarefas[escolha-1]['feito'] = True 
            return 'ok'
        return 'erro'
    except ValueError:
        return 'erro'
def traduzir_status(status):
    if status=='ok': return 'Sucesso!'
    if status=='vazio': return 'Lista vazia'
    if status=='erro': return 'Opção inválida / digite um número'
    if status is None: return 'Erro inesperado'
def pausar_e_limpar_tela():
    time.sleep(2)
    os.system('cls')
def main():
    while True:
        verificar=processa_opcao()
        if  verificar=='sair':
            print('Saindo')
            break
        if verificar:
            print(verificar)
        pausar_e_limpar_tela()
if __name__ == "__main__":
    main()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio13.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio16.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio2.py
# ==============================================================================

'''Exercício 1: Classificação de Triângulos

Crie um programa que determine e imprima o tipo de um triângulo com base nos comprimentos dos seus três lados.

    Colete os comprimentos dos três lados (A, B e C) do usuário.

    Considere que os lados são números inteiros, mas garanta a coerção de tipos correta.

    Implemente a lógica condicional (if/elif/else) para classificar o triângulo:

        Equilátero: Todos os lados são iguais.

        Isósceles: Apenas dois lados são iguais.

        Escaleno: Todos os lados são diferentes.

    Use uma f-string na saída para imprimir o resultado da classificação.'''
# print('Calculo de formação de triângulos!!')
# reta1 = input('Informe o comprimento da primeira reta: ')
# reta2 = input('Informe o comprimento da segunda reta: ')
# reta3 = input('Informe o comprimento da terceira reta: ')
# reta1_float=float(reta1)
# reta2_float=float(reta2)
# reta3_float=float(reta3)
# equi= reta1_float == reta2_float == reta3_float
# iso = reta2_float == reta1_float and reta1_float + reta2_float > reta3_float or reta2_float == reta3_float and reta2_float + reta3_float > reta1_float and reta1_float == reta3_float and reta1_float + reta3_float > reta2_float
# esc = reta1_float + reta2_float > reta3_float and reta2_float + reta3_float > reta1_float and reta3_float + reta1_float > reta2_float 
# if equi:
#     print('Equilátero: Todos os lados são iguais')
# elif iso:
#     print('Isósceles: Apenas dois lados são iguais.')
# elif esc:
#     print('Escaleno: Todos os lados são diferentes.')
# else:
#     print('Os fatores não formam um triângulo.')

# Peça duas notas ao usuário.
# Calcule a média e diga se o aluno está:

# Aprovado (média >= 7)

# Reprovado (média < 7)
import time
import os
def notas():
    try:
        print('*'*30)
        nota1=float(input('Informe a primeira nota: '))
        nota2=float(input('Informe a segunda nota: '))
        return (nota1+nota2)/2
    except ValueError:
        return None
while True:
    nota=notas()
    if nota is None:
        print('Erro de entrada')
    elif nota >=7:
        print('Você foi aprovado!!')
    else:
        print('Você está reprovado')
    saida=input('Deseja sair do programa digite 0')
    if saida =='0':
        print('Saindo do programa!')
        break
    time.sleep(2)
    os.system('cls')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio23.py
# ==============================================================================

'''
Faça uma lista de compras com lista
O usuário dever ter a possibilidade de inserir, apagar e listar valores da sua lista
não permita que o programa que com erros de índices inexistente na lista.
'''
import time
import os
compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if opcao == 'i':
        os.system('cls')
        valor=input('Qual item deseja incluir: ')
        compras.append(valor)
    elif opcao == 'a':
        indice=input('Qual valor deseja apagar: ')
        try:
            indice_int = int(indice)
            del compras[indice_int]
            print('Item apagado!')
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        if len(compras) == 0:
            os.system('cls')
            print('Nada para listar!')
        for i, valor in enumerate(compras):
            print(i, valor)
    elif opcao == 's':
        print('Até mais')
        break
    else:
        print('Por favor, escolha i, l, ou s.')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio30.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio31.py
# ==============================================================================

def verificar_idade():
    try:
        idade=int(input('Informe sua idade: '))
        if idade >=18:
            return True
        else:
            return False
    except ValueError:
        return False
verifica_idade=verificar_idade()
if verifica_idade:
    print('Você é de maior!!')
else:
    print('Você não é de maior!!')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio32.py
# ==============================================================================

'''Enunciado

Crie uma lista com 4 frutas

Mostre numeradas (1 a 4)

Peça ao usuário para escolher

Se escolher certo índice:

mostre a fruta escolhida

Se errar:

mostre “opção inválida”'''
frutas = ['Morango', 'Laranja', 'Figo', 'Melância']
for i , fruta in enumerate(frutas,start=1):
    print(f'{i} {fruta}')
try:
    escolha=int(input('Escolha uma das frutas: '))
    if  1<= escolha <=len(frutas):
        print(f'A fruta escolhida foi {frutas[escolha-1]}')
    else:
        print('Opção inválida!!')
except ValueError:
    print('Somente números inteiro!!')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio33.py
# ==============================================================================

tarefas =['Estudar', 'Trabalhar', 'Treinar', 'Descansar']
def escolha_tarefa():
    for i, tarefa in enumerate(tarefas,start=1):
        print(f'{i} {tarefa}')
    try:
        opcao=int(input('Escolha uma tarefa: '))
        if 1<= opcao <=len(tarefas):
            return f'A tarefa escolhida é {tarefas[opcao-1]}'
        else:
            return 'Opção inválida!!!!'
    except ValueError:
        return 'Somente números inteiros permitido!!'
definir=escolha_tarefa()
print(definir)

# ==============================================================================
# ORIGINAL: Exercicios/exercicio35.py
# ==============================================================================

'''
1 - Estudar
2 - Trabalhar
3 - Descansar
0 - Sair

    Peça uma opção

    Enquanto a opção não for 0:

        mostre a escolha

        peça a opção novamente

    Quando for 0:

        mostre “Programa encerrado”'''
import os
import time
tarefas = ['Estudar', 'Trabalhar', 'Descansar']


while True:
    os.system('cls')
    for i, tarefa in enumerate(tarefas,start=1):
        print(f'{i} {tarefa}')
    try:
        opcao=int(input('Escolha uma tarefa caso deseje sair digitar [0]: '))
        if opcao ==0:
            print('Saindo do programa ate mais')
            break
        if 1<= opcao<=len(tarefas):
            print(f'Você vai {tarefas[opcao-1]}')
            time.sleep(2)
        else:
            print('Opção inválida')
            time.sleep(2)
    except ValueError:
        print('Somente números inteiros permitidos')
        time.sleep(2)

# ==============================================================================
# ORIGINAL: Exercicios/exercicio36.py
# ==============================================================================

'''chama mostrar_menu()

pede a entrada do usuário

valida

executa'''
import time
import os
tarefas = ['Estudar', 'Trabalhar', 'Descansar']
def mostra_menu(tarefas):
    for i, tarefa in enumerate(tarefas,start=1):
        print(f'[{i}] {tarefa}')
    print('[0] Para sair')
mostra_menu(tarefas)
while True:
    try:
        escolha=int(input('Escolha uma opção: '))
        if escolha == 0:
            print('Saindo do programa ate mais!!')
            break
        if 1<= escolha <= len(tarefas):
            print(f'Você escolheu {tarefas[escolha-1]}') 
        else:
            print('Opção invalida!!! Tente novamente!')
        time.sleep(2)
        os.system('cls')
    except ValueError:
        print('Somente números inteiros permitidos.')
        time.sleep(2)
        os.system('cls')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio37.py
# ==============================================================================

import time
import os

tarefas = ['Estudar', 'Trabalhar', 'Descansar']
def mostra_menu(tarefas):
    for i, tarefa in enumerate(tarefas,start=1):
        print(f'[{i}] {tarefa}')
    print('[0] Para sair')
opcao=['Mostra tarefas', 'Escolher tarefas']
def mostra_menu_princinpal():
    for i, op in enumerate(opcao, start=1):
        print(f'[{i}] {op}')
    print('[0] Para sair')
while True:
    try:
        
        mostra_menu_princinpal()
        escolha=int(input('Escolha uma opção: '))
        if escolha == 0:
            print('Saindo do programa!!')
            time.sleep(2)
            os.system('cls')
            break
        if escolha ==1:
            mostra_menu(tarefas)
        elif escolha ==2:
            decisao=int(input('Escolha a tarefa: '))
            if 1<= decisao <= len(tarefas):
                print(f'Você escolheu {tarefas[decisao-1]}') 
            else:
                print('Opção invalida!!! Tente novamente!')
        else:
            print('Opção invalida!!! Tente novamente!')
        time.sleep(2)
        os.system('cls')
    except ValueError:
        print('Apenas números inteiros permitido')
        time.sleep(2)
        os.system('cls')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio38.py
# ==============================================================================

import time
import os
tarefas = ['Estudar', 'Trabalhar', 'Descansar','Mostrar o total de tarefas']
def validar():
    for i, tarefa in enumerate(tarefas,start=1):
        print(f'[{i}] {tarefa}')
    print('[0] Para sair')
    try:
        escolha=int(input('Escolha uma opção: '))
        if escolha == 0:
            return 0
        elif 1<= escolha <=len(tarefas):
            return escolha
        return None
    except ValueError:
        return None
while True:
    escolha_1=validar()
    if escolha_1 is None:
        print('Erro!! Opção invalida!')
        time.sleep(2)
        os.system('cls')
        continue
    if escolha_1 == 0:
        print('Saindo do programa!!')
        break
    elif escolha_1 ==4:
        for i, tarefa in enumerate(tarefas,start=1):
            print(f'[{i}] {tarefa}')
            time.sleep(2)           
    else:
        print(f'Você escolheu {tarefas[escolha_1-1]}')
    time.sleep(2)
    os.system('cls')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio43.py
# ==============================================================================

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
contador=0

for i, pergunta in enumerate(perguntas,start=1):
    print(f"{i} {pergunta['Pergunta']}")
    for item, opcao in enumerate(pergunta['Opções'],start=1):
        print(f" [{item}] {opcao}")
    try:
        decisao=int(input('Qual opção é a correta: '))
        if decisao < 1 or decisao > len(pergunta['Opções']):
            print('Erro')
            continue
        opcao_escolhida = pergunta['Opções'][decisao - 1]
        if opcao_escolhida == pergunta['Resposta']:
            contador+=1
            print('Parabens Você acertou!!')
    except ValueError:
        print('Erro')  
print(f'Parabens você acertou {contador}')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio9.py
# ==============================================================================

'''🛒 Desafio: O Caixa de Supermercado (Acumulador)

A missão é somar o valor de uma compra, mas você não sabe quantos produtos o cliente tem.

As Regras:

    Crie uma variável para guardar o total (começa com 0).

    Peça o preço do produto.

    O laço (while) deve rodar enquanto o preço for diferente de 0.

        (Digitou 0 = acabou a compra).

    Dentro do laço: Sone o preço ao total (+=) e peça o próximo preço.

    No final, mostre: "Total a pagar: R$ X".

Dica de Ouro: Use a lógica da "Leitura Antecipada" (pergunta um fora, pergunta o outro dentro do loop) para evitar somar o zero ou dar erro.

total_compra = 0
try:
    # CORREÇÃO 1: Converta para float JÁ NA ENTRADA
    produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
    
    # Agora 'produto' é um número (0.0). O while consegue comparar.
    while produto != 0:
        # CORREÇÃO 2: Não precisa converter aqui dentro, já convertemos lá fora.
        total_compra += produto
        
        # CORREÇÃO 3: Converta de novo aqui dentro para o loop testar na volta
        produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
        
    print(f'O total a pagar: R$ {total_compra:.2f}')
except ValueError:
    print('Erro: Coloque apenas números.')'''
total_compra = 0
try:
    produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
    while produto != 0:
        total_compra += produto
        produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
    print(f'O total a pagar: R$ {total_compra:.2f}')
except:
    print('Erro, Coloue novamente o valor do produto')

# ==============================================================================
# ORIGINAL: Revisoes/revisao29.py
# ==============================================================================

'''
introução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input('Vou dobra o número que vc digitar: ')

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro do {numero_str} é {numero_float*2}')
except:
    print('Isso não é um número.')

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro do {numero_str} é {numero_float*2}')
#else:
#    print('Isso não é um número.')

# ==============================================================================
# ORIGINAL: Revisoes/revisao69.py
# ==============================================================================

lista = ['Estudar', 'Trabalhar', 'Treinar', 'Descansar']
def lista_usa(lista):
    for i,item in enumerate(lista, start=1):
        print(f'{i} {item}')
    try:
        escolha=int(input('Escolha uma tarefa: '))
        if 1<= escolha <= len(lista):
            return f'Você escolheu a tarefa {lista[escolha-1]}'
        return 'Opção inválida'
    except ValueError:
        return 'Apenas números inteiros permitidos!!'
afazeres = lista_usa(lista)
print(afazeres)

# ==============================================================================
# ORIGINAL: Revisoes/revisao82.py
# ==============================================================================

# Try, except, else e  finally


try:
    a=18
    b=0
    c = a / b
except ZeroDivisionError:
    print('Diviviu por zero')
print('CONTINUAR')

# ==============================================================================
# ORIGINAL: Revisoes/revisao83.py
# ==============================================================================

# Try, except, else e  finally
try:
    print('Abrindo arquivo')
finally:
    print('Fechando arquivo')

# ==============================================================================
# ORIGINAL: Revisoes/revisao84.py
# ==============================================================================

# raise - lançndo exceções(erros
# https://docs.python.org/3/library/exceptions.html)
def nao_aceito_zero(d):
    if d ==0:
        raise ZeroDivisionError('Divisão por zero não é permitida')
    return True

def numeros_inteiros_ou_floats(n,d):
    if not isinstance(n, (int,float)) or not isinstance(d, (int,float)):
        raise TypeError('Apenas números inteiros')
def divide(n, d):
    numeros_inteiros_ou_floats(n,d)
    nao_aceito_zero(d)
    return n/d

print(divide('8', 1))

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex5(32).py
# ==============================================================================

'''
Faça um programa que peça ao usuário oara digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro
, informe que não é um número inteiro
'''
try:
    numero = input ('Digite um número inteiro: ')
    numero_int = int(numero)
    par = numero_int % 2 == 0

    if par:
        print('O número informado é PAR!')
    else:
        print('O número informado é ÍMPAR')
except:
    print('O que foi digitado não é um número inteiro')

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex6(33).py
# ==============================================================================

'''
Faça um programa que pergunte a hora ao usuário e , baseando-se no horário
descrito, exiba saudação aproriada. Ex.
Bom dia 0-11, Boa tarde 12 - 17 e Boa noite 18-23
'''
try:
    hora = input('Informe com número inteiro a hora: ')
    hora_int = int(hora)
    manha = 0 <= hora_int <= 11
    tarde = 12<= hora_int <= 17
    noite = 18<= hora_int <= 23
    if manha:
        print('Bom dia!!')
    elif tarde:
        print('Boa tarde!!')
    elif noite:
        print('Boa noite!!')
    else:
        print('Horario invalido! Não existe essa hora')
except:
    print('Favor informe a hora em número inteiro')

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex8(40).py
# ==============================================================================

'''calculadora while
'''
while True:
    try:
        primeiro_fator = input('Digite o primeiro fator: ')
        primeiro_int = int(primeiro_fator)
        segundo_fator = input('Digite o segundo fator: ')
        segundo_int = int(segundo_fator)
        operador = input('Operadores: (+, -, /, *): ')
        if operador == '+':
            resultado = primeiro_int + segundo_int
            print(f'RESULTADO = {resultado}')
        elif operador == '-':
            resultado = primeiro_int - segundo_int
            print(f'RESULTADO =  {resultado}')
        elif operador == '/':
            if segundo_int == 0:
                print('Não existe divisão por ZERO!!')
                
            else:
                resultado = primeiro_int / segundo_int
                print(f'RESULTADO = {resultado}')
        elif operador == '*':
            resultado = primeiro_int * segundo_int
            print(f'RESULTADO = {resultado}')
        else:
            print('OPERADOR INVÁLIDO')
    except:
        print('Erro: Você precisa digitar números inteiros.')
        continue
    sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
    if sair.startswith('s'):
        break

