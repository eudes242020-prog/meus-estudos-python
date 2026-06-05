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