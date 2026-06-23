from dados_tarefas import carregar_tarefas, salvar_tarefas
from mostrar_tarefas import ver_tarefas
from tarefas import adicionar_tarefa, remover_tarefa, entrada_usuario,concluir_tarefa, entrada_numero
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
        novo=adicionar_tarefa(valido)
        salvar_tarefas(novo)
    elif opcao== '2':
        ver_tarefas(carregar_tarefas())
        valido_num=entrada_numero()
        remover=remover_tarefa(valido_num)
        if remover is not None:
            print(remover)
    elif opcao == '3':
        ver_tarefas(carregar_tarefas())
        valido_num=entrada_numero()
        concluido=concluir_tarefa(valido_num)
        if concluido is not None:
            print(concluido)
    elif opcao == '4':
        checar=carregar_tarefas()
        if not checar:
            print('Não tem tarefa pra listar')
            continue
        ver_tarefas(checar)
    else:
        print('Opção invalida')