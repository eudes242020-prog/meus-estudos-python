'''🏦 Próximo Desafio: O Menu Bancário (Backend Puro)

Já que seu foco é ser Backend Developer, nada melhor que simular a lógica de um caixa eletrônico. Aqui, o while não vai depender de um preço, mas sim da vontade do usuário de continuar no sistema.

Cenário: Você tem um saldo inicial de R$ 0.00. O programa deve mostrar um menu com opções e realizar operações até a pessoa decidir sair.

As Regras:

    Crie uma variável saldo começando com 0.

    Crie uma variável opcao (pode começar com algo diferente da opção de saída).

    O menu deve ter:

        1: Consultar Saldo (Mostra o saldo atual).

        2: Depositar (Pede um valor e soma ao saldo).

        3: Sacar (Pede um valor e subtrai do saldo).

        4: Sair (Encerra o loop).

    O while deve rodar enquanto a opção for diferente de 4.

Dica de Lógica: Dessa vez, você vai pedir a opcao dentro do loop (ou usar a leitura antecipada se preferir, mas em menus geralmente mostramos as opções repetidamente dentro do loop).
'''
saldo = 0
try:
    opcao = float(input('[1] Consultar Saldo: \n[2] Depositar: \n[3] Sacar: \n[4] Sair: \nQual opção: '))
    while opcao!= 4:
        if opcao == 1:
            print(f'Seu saldo atual é R$ {saldo:.2f}')
        elif opcao ==2:
            valor = float(input('Informe o valor: '))
            saldo += valor
        elif opcao ==3:
            valor = float(input('Informe o valor: '))
            if valor > saldo:
                print('Saldo Insuficiente!')
            else:
                print('Saque realizado')
                saldo -= valor
        else:
            print('Erro, Pricisa digitar a opção correta')
        opcao = float(input('[1] Consultar Saldo: \n[2] Depositar: \n[3] Sacar: \n[4] Sair: \nQual opção: '))
    print('Finalizando o sistema!')
except:
    print('ERRO: Digite as opções corretamente')