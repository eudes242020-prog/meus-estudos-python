from dados_tarefas import carregar_tarefas, salvar_tarefas
from mostrar_tarefas import ver_tarefas
from tarefas import adicionar_tarefa, remover_tarefa, marcar_concluida,pegar_nome_tarefa,validar_nome_tarefa
atividade = carregar_tarefas()
menu={1: "Cadastra Tarefa", 2: "Remover Tarefa", 3: "Marcar tarefa como concluida", 4: "Listar Tarefas", 0: "Sair"}
def opcoes_menu(menu):
    for chave,opcao in menu.items():
        print(f'[{chave}] {opcao}')
def obter_nome_valido():
    tarefa =pegar_nome_tarefa()
    validar=validar_nome_tarefa(tarefa)
    if validar is None:
            print('Erro de entrada!')
    return validar
while True:
    opcoes_menu(menu)
    opcao = input('Escolha uma opção: ')
    if opcao =='0':
        print('Saindo do programa')
        break
    elif opcao == '1':
        valido=obter_nome_valido()
        if valido is None:
            continue
        adicionar_tarefa(atividade, valido)
        salvar_tarefas(atividade)
    elif opcao== '2':
        valido=obter_nome_valido()
        if valido is None:
            continue
        remover_tarefa(atividade, valido)
        salvar_tarefas(atividade)
    elif opcao == '3':
        valido=obter_nome_valido()
        if valido is None:
            continue
        marcar_concluida(atividade, valido)
        salvar_tarefas(atividade)
    elif opcao == '4':
        ver_tarefas(atividade)
    else:
        print('Opção invalida')