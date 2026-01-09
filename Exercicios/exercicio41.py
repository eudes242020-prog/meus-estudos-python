def mostrar_menu(menu):
    print('------------')
    for i, item in enumerate(menu, 1):
        print(f'[{i}] {item}')
    print('[0] Para sair')

def mostrar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, 1):
        status = "✔" if tarefa["feito"] else "❌"
        print(f'{i}. {tarefa["nome"]} {status}')

def alterar_status_tarefa(tarefas, status_desejado):
    if not tarefas:
        raise ValueError("Lista de tarefas vazia")
    mostrar_tarefas(tarefas)
    try:
        escolha = int(input("Escolha uma tarefa: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["feito"] = status_desejado
        else:
            raise IndexError("Índice fora do intervalo")
    except ValueError:
        raise ValueError("Entrada inválida, digite um número")

def executar_programa():
    tarefas = [
        {"nome": "Estudar", "feito": False},
        {"nome": "Trabalhar", "feito": False},
    ]
    menu = ["Ver tarefas", "Marcar como concluída", "Desmarcar como concluída"]
    while True:
        mostrar_menu(menu)
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 0:
                print("Saindo...")
                break
            elif opcao == 1:
                mostrar_tarefas(tarefas)
            elif opcao == 2:
                alterar_status_tarefa(tarefas, True)
            elif opcao == 3:
                alterar_status_tarefa(tarefas, False)
            else:
                print("Opção inválida")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    executar_programa()