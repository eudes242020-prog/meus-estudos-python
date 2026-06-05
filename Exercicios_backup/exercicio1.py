'''
Exercício 1: Calculadora Simples de IMC (Reforço e Conversão)

O objetivo é recriar o cálculo do IMC, mas garantindo que todos os conceitos de tipos de dados e operadores estejam claros.

    Coleta de Dados: Use a função input() para pedir ao usuário:

        O peso (em kg).

        A altura (em metros).

    Tratamento/Conversão: Como input() retorna strings, converta o peso e a altura para o tipo de dado float (número decimal).

    Saída de Dados: Imprima o resultado usando uma f-string para exibir o peso e altura que o usuário digitou, e o resultado do IMC com apenas duas casas decimais de precisão.

Exemplo de Saída Esperada:

    Se o usuário digitar 80 e 1.75, a saída deve ser: Para o peso 80.0kg e altura 1.75m, o IMC calculado é 26.12.'''
# print('Calculadora IMC!')
# peso = input('Informe seu peso: ')
# altura = input('Informe sua altura: ')
# peso_float = float(peso)
# altura_float=float(altura)
# imc=peso_float / altura_float**2
# print(f'Para o peso {peso_float:.1f}kg e altura {altura_float:.2f}m, o IMC calculado é {imc:.2f}')
'''Solicite a idade do usuário.
Exiba uma mensagem informando se ele é maior ou menor de idade (18 anos como referência).'''
import time
import os
def solicitacao():
    try:
        print('Caso queira sair do programa digita 0')
        idade=int(input('Informe sua idade: '))
        return idade
    except ValueError:
        return None
def verificar_idade(idade):
    if idade is None:
        return'Erro de entrada'
    if idade==0:
        return 'Saindo do programa'
    if idade>=18:
        return "Você é maior de idade"
    else:
        return "Você é menor de idade"
    
def sistema():
    while True:
        idade=solicitacao()
        mensagem = verificar_idade(idade)
        print(mensagem)
        if mensagem=='Saindo do programa':
            break
        time.sleep(2)
        os.system('cls')
sistema()