from dados_tarefas import carregar_tarefas, salvar_tarefas
from mostrar_tarefas import ver_tarefas
from tarefas import adicionar_tarefa, remover_tarefa, entrada_usuario,concluir_tarefa, entrada_numero
atividade = carregar_tarefas()
menu={1: "Cadastra Tarefa", 2: "Remover Tarefa", 3: "Marcar tarefa como concluida", 4: "Listar Tarefas", 0: "Sair"}
def opcoes_menu(menu):
    for chave,opcao in menu.items():
        print(f'[{chave}] {opcao}')
while True:
    opcoes_menu(menu)
    opcao = input('Escolha uma opção: ')
    if opcao =='0':
        print('Saindo do programa')
        break
    elif opcao == '1':
        valido=entrada_usuario()
        adicionar_tarefa(atividade, valido)
        salvar_tarefas(atividade)
    elif opcao== '2':
        ver_tarefas(atividade)
        valido_num=entrada_numero()
        remover=remover_tarefa(atividade,valido_num)
        if remover is not None:
            print(remover)
        salvar_tarefas(atividade)
    elif opcao == '3':
        ver_tarefas(atividade)
        valido_num=entrada_numero()
        concluido=concluir_tarefa(atividade, valido_num)
        if concluido is not None:
            print(concluido)
        salvar_tarefas(atividade)
    elif opcao == '4':
        ver_tarefas(atividade)
    else:
        print('Opção invalida')