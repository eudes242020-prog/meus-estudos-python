
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