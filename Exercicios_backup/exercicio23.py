'''
Faça uma lista de compras com lista
O usuário dever ter a possibilidade de inserir, apagar e listar valores da sua lista
não permita que o programa que com erros de índices inexistente na lista.
'''
import time
import os
compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if opcao == 'i':
        os.system('cls')
        valor=input('Qual item deseja incluir: ')
        compras.append(valor)
    elif opcao == 'a':
        indice=input('Qual valor deseja apagar: ')
        try:
            indice_int = int(indice)
            del compras[indice_int]
            print('Item apagado!')
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        if len(compras) == 0:
            os.system('cls')
            print('Nada para listar!')
        for i, valor in enumerate(compras):
            print(i, valor)
    elif opcao == 's':
        print('Até mais')
        break
    else:
        print('Por favor, escolha i, l, ou s.')


