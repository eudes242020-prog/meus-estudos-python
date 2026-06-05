import os
import time
tarefas = [
    {"nome": "Estudar", "feito": False},
    {"nome": "Trabalhar", "feito": False},
]
menu=["Ver tarefas", 'Marcar tarefa como concluída', 'Desmarcar tarefa como concluída', ]
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')
def menu_principal():
    print('------------')
    for item, tarefa in enumerate(menu, start=1):
        print(f'[{item}] {tarefa}')
    print('[0] Para sair')

def executar_menu():
    menu_principal()
    try:
        numero=int(input('Qual opção deseja: '))
        if numero==0:
            return 'sair'
        if 1<= numero <=len(menu):
            if numero==1:
                mostrar_tarefa()
            elif numero==2:
                status = marcar_tarefa()
                mensagem=mensagem_status(status)
                return mensagem
            elif numero==3:
                status = desmarcar_tarefa()
                mensagem = mensagem_status(status)
                return mensagem
            else:
                return 'erro'
    except ValueError:
        return 'erro'       
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
def mostrar_tarefa():
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["feito"] else "❌"
        print(f'{i} {tarefa['nome']} {status}')

def marcar_tarefa():
    if not tarefas: #primeiro verificar se a lista está vazia, se estiver dar o returno e polpa codigo
            return 'vazio'
    mostrar_tarefa() #mostra lista de tarefas numerada
    try:  #tratativa de errro
        escolha=int(input('Qual tarefa deseja marcar como concluida: '))#pede ao usuario para coloca a tarefa concluida
        if 1<=escolha<=len(tarefas):#verificador da escolha do usuario pra ver se esta no "range"
            tarefas[escolha-1]['feito'] = True #transforma a escolha do cliente en verdadeira, com isso mostrando que concluio
            return 'ok'#mostra que foi feito tudo ok com todo programa
        return 'erro'#como nao passo pelo if está fora do range e n é possivel fazer a escolha da tarefa
    except ValueError:
        return 'erro'#erro tratado
def mensagem_status(status):
    if status=='ok': return 'Sucesso!'
    if status=='vazio': return 'Lista vazia'
    if status=='erro': return 'Opção inválida / digite um número'
while True:
    verificar=executar_menu()
    if  verificar=='sair':
        print('Saindo')
        break
    if verificar:
        print(verificar)
    pausar_e_limpar()
