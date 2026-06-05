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
