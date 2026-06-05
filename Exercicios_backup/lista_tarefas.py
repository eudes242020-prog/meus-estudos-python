# PROJETO: Lista de Tarefas Simples
# Autor: [Eudes]
# Data: 16/12/2025
import os
import time
tarefas = []

while True:
    os.system('cls')
    print('\n--- MENU ---')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Apagar uma tarefa')
    print('4. Sair')
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Você escolheu adicionar...')
        # Aqui vamos escrever a lógica de adicionar
        tarefa=input('Qual tarefa deseja adicionar: ')
        print("Tarefa adicionada!")
        time.sleep(2)
        tarefas.append(tarefa)
    elif opcao == '2':
        # Aqui vamos escrever a lógica de listar
            if len(tarefas) == 0:
                os.system('cls')
                print('Você não possui tarefas')   
            else:
                print('Suas tarefas são...')
                for item, topico in enumerate(tarefas):
                   print(f'[{item}] - {topico}')
    elif opcao == '3':
        if len(tarefas) == 0:
            print('Você não possui tarefas para apagar')
        else:
            print('\n--- LISTA PARA APAGAR ---')
            for indice, topico in enumerate(tarefas):
                print(f'[{indice}] - {topico}')
            try:
                apagar=int(input('Qual tarefa deseja apagar: '))
                del tarefas[apagar]
                print('Tarefa removida com sucesso!')
            except ValueError:
                print('Por favor, digite um número inteiro.')
            except IndexError:
                print('Índice não existe na lista.')
            except Exception:
                print('Erro desconhecido')

    elif opcao == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida!')
    input("\nPressione ENTER para continuar...")