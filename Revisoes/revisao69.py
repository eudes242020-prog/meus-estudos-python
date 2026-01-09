def lista_usa(lista):
    for i,item in enumerate(lista, start=1):
        print(f'{i} {item}')
    try:
        escolha=int(input('Escolha uma tarefa: '))
        if 1<= escolha <= len(lista):
            return f'Você escolheu a tarefa {lista[escolha-1]}'
        return 'Opção inválida'
    except ValueError:
        return 'Apenas números inteiros permitidos!!'
afazeres = lista_usa(['Estudar', 'Trabalhar', 'Treinar', 'Descansar'])
print(afazeres)
