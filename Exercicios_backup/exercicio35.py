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