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