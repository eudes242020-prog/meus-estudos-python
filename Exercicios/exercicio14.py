total_caixa = 0

print('--- CINE PYTHON ---')

try:
    filme = int(input('Escolha: [1] Avatar [2] Titanic [0] Sair: '))


    while filme != 0: 
        if filme == 1:
            preco = 30.00
        elif filme == 2:
            preco = 25.00

        else:
            print('Opção Inválida! Escolha 1 ou 2.')          
            filme = int(input('Escolha: [1] Avatar [2] Titanic [0] Sair: '))
            continue
        qtd = int(input('Quantos ingressos? '))
        subtotal = preco * qtd
        total_caixa += subtotal
        print(f'Venda registrada: R$ {subtotal}')
        filme = int(input('Escolha: [1] Avatar [2] Titanic [0] Sair: '))
    print(f'Total do dia: R$ {total_caixa}')
except:
    print('Erro!!')