perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta':'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta':'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    
    escolha = input('Escolha uma opção: ')
    
    
    if escolha.isdigit():
        indice = int(escolha)
        
       
        resposta_do_usuario = opcoes[indice]

        if resposta_do_usuario == pergunta['Resposta']:
            print('✅ Acertou!')
        else:
            print('❌ Errou!')
    else:
        print('⚠️ Por favor, digite um número.')
        
    print() #