'''
 Desafio: O Banco dos Centavos

Imagine que você tem uma conta e depositou R$ 0.10 três vezes seguidas. A lógica diz: 0.10 + 0.10 + 0.10 = 0.30.

Sua missão: Crie um código que faça essa soma de duas formas e compare:

    Modo "Ingênuo" (Float): Some 0.1 três vezes e peça para o Python verificar se o resultado é igual (==) a 0.3.

    Modo "Profissional" (Decimal): Importe o módulo decimal, use a classe Decimal para somar os três valores e verifique se bate com o Decimal('0.3').'''
import decimal
soma_i = 0.1
soma1 = '0.1'
decimal1 = decimal.Decimal(soma1)
soma_p = decimal1 + decimal1 + decimal1
print(soma_i + soma_i + soma_i)
print(soma_p)
if soma_p == decimal.Decimal('0.3'):
    print('Sim')
else:
    print('Não')