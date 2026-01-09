tarefas =['Estudar', 'Trabalhar', 'Treinar', 'Descansar']
def escolha_tarefa():
    for i, tarefa in enumerate(tarefas,start=1):
        print(f'{i} {tarefa}')
    try:
        opcao=int(input('Escolha uma tarefa: '))
        if 1<= opcao <=len(tarefas):
            return f'A tarefa escolhida é {tarefas[opcao-1]}'
        else:
            return 'Opção inválida!!!!'
    except ValueError:
        return 'Somente números inteiros permitido!!'
definir=escolha_tarefa()
print(definir)