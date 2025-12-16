# PROJETO: Lista de Tarefas Simples
# Autor: [Seu Nome]
# Data: 16/12/2025
import os
tarefas = []

while True:
    
    print("\n--- MENU ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Você escolheu adicionar...")
        # Aqui vamos escrever a lógica de adicionar
        tarefa=input('Qual tarefa deseja adicionar: ')
        tarefas.append(tarefa)
    elif opcao == '2':
        # Aqui vamos escrever a lógica de listar
            if len(tarefas) == 0:
                os.system('cls')
                print('Você não possui tarefas')
            else:
                print("Suas tarefas são...")
                print(item)
            for item in tarefas:
                print(item)
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")