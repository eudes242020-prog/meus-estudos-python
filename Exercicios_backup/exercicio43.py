perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
contador=0

for i, pergunta in enumerate(perguntas,start=1):
    print(f"{i} {pergunta['Pergunta']}")
    for item, opcao in enumerate(pergunta['Opções'],start=1):
        print(f" [{item}] {opcao}")
    try:
        decisao=int(input('Qual opção é a correta: '))
        if decisao < 1 or decisao > len(pergunta['Opções']):
            print('Erro')
            continue
        opcao_escolhida = pergunta['Opções'][decisao - 1]
        if opcao_escolhida == pergunta['Resposta']:
            contador+=1
            print('Parabens Você acertou!!')
    except ValueError:
        print('Erro')  
print(f'Parabens você acertou {contador}')