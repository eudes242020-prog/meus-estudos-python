
perguntas = [
    {
        'Pergunta': 'Qual é o resultado de 3 * "A"?',
        'Opções': ['AAA', '3A', 'A3', 'Erro'],
        'Resposta': 'AAA',
    },
    {
        'Pergunta': 'Qual comando usamos para mostrar algo na tela?',
        'Opções': ['input()', 'screen()', 'print()', 'echo()'],
        'Resposta': 'print()',
    },
    {
        'Pergunta': 'O que o comando int("5") faz?',
        'Opções': ['Transforma em texto', 'Transforma em inteiro', 'Nada', 'Dá erro'],
        'Resposta': 'Transforma em inteiro',
    },
    {
        'Pergunta': 'Como se inicia uma lista vazia?',
        'Opções': ['{}', '()', '[]', '<>'],
        'Resposta': '[]',
    },
    {
        'Pergunta': 'Qual símbolo usamos para comentários?',
        'Opções': ['//', '#', '--', '/*'],
        'Resposta': '#',
    }
]
contador=0
for pergunta in perguntas:
    print(f'{pergunta["Pergunta"]}')
    opcoes=pergunta['Opções']
    for i, disponiveis in enumerate(opcoes):
        print(f'{i} {disponiveis}')
    try:
        escolha=int(input('Qual opção é a correta: '))
        if escolha >= 0 and escolha <len(opcoes):

            if opcoes[escolha]==pergunta['Resposta']:
                print('Você acertou!!')
                contador+=1
            else:
                print('Errou!')
        else:
            print('Opção inválida (número fora da lista)')

    except ValueError:
        print('precisa ser um numero inteiro')
print(f'Você acertou {contador}')