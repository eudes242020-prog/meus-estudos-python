'''calculadora while
'''
while True:
    try:
        primeiro_fator = input('Digite o primeiro fator: ')
        primeiro_int = int(primeiro_fator)
        segundo_fator = input('Digite o segundo fator: ')
        segundo_int = int(segundo_fator)
        operador = input('Operadores: (+, -, /, *): ')
        if operador == '+':
            resultado = primeiro_int + segundo_int
            print(f'RESULTADO = {resultado}')
        elif operador == '-':
            resultado = primeiro_int - segundo_int
            print(f'RESULTADO =  {resultado}')
        elif operador == '/':
            if segundo_int == 0:
                print('Não existe divisão por ZERO!!')
                
            else:
                resultado = primeiro_int / segundo_int
                print(f'RESULTADO = {resultado}')
        elif operador == '*':
            resultado = primeiro_int * segundo_int
            print(f'RESULTADO = {resultado}')
        else:
            print('OPERADOR INVÁLIDO')
    except:
        print('Erro: Você precisa digitar números inteiros.')
        continue
    sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
    if sair.startswith('s'):
        break