import time
import os

menu=['Ver todas as tarefas','Adicionar nova tarefa', 'Remover tarefa']
    
tarefas=[]
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')
def menu_princinpal():
    print('=== MENU DO SISTEMA ===')
    for item, opcao in enumerate(menu,start=1):
        print(f'[{item}] {opcao}')
    print('[0] Sair')
def mostrar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada')
        return False
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'[{i}] {tarefa}')
        return True
def adicionar_tarefa():
    tarefa=input('Qual tarefa deseja adicionar: ').strip()
    tarefas.append(tarefa)
    return True 
def remover_tarefa():
    if not tarefas:
            return False
    mostrar_tarefas()
    try:
        escolha=int(input('Escolha uma tarefa: '))
        if 1<= escolha <=len(tarefas):
            tarefas.pop(escolha-1)
            return True
        else:
            return False
    except ValueError:
        return False
while True:
    menu_princinpal()
    try:
        decisao=int(input('Oque deseja fazer: '))
        if decisao==0:
            print('Saindo do programa!!')
            break
        elif decisao==1:
            if not tarefas:
                print('Não existe tarefa para listar!!')
                pausar_e_limpar()
                continue
            else:
                mostrar_tarefas()
        elif decisao==2:
            ok = adicionar_tarefa()
            if ok:
                print('Tarefa adicionada com sucesso!')
            else:
                print('Nenhuma tarefa foi adicionada.')
        elif decisao==3:
            remover=remover_tarefa()
            if remover:
                print('Tarefa foi removida com sucesso!')
            else:
                print('Nenhuma tarefa foi removida.')
        else:
            print('Opção inválida!!')
            pausar_e_limpar()
        pausar_e_limpar()
    except ValueError:
        print('Somente números inteiros permitidos!!!')
        pausar_e_limpar()