'''Sua Missão Agora:

    Copie, rode e entenda esse código.

    Desafio: Crie um dicionário chamado eu com seus dados: 'nome', 'idade', 'cargo' (pode por "Dev Python") e 'tecnologias' (aqui dentro coloque uma lista ['Python', 'Git']).

    Mande um print chamando seu nome e uma tecnologia.'''
# eu = {'Nome' : 'Eudes',
#       'Nome': 'Maria', 'idade': 50,
#       'Idade':  30,
#       'Cargo': 'Dev Python',
#       'Tecnologias': ['Python', 'Git']
# }

pessoas =[
     {'nome': 'Eudes', 'idade': 30},
     {'nome': 'Maria', 'idade': 55},
]
# pessoas.append({'nome': 'João', 'idade': 20})
# for pessoa in pessoas:
#     print(f"Seu nome é {pessoa['nome']} e idade {pessoa['idade']}")
import os
import time
while True:
    os.system('cls')
    print('\n--- Cadastro de Nova Pessoa ---')
    nome=input("Informe seu nome: ")
    try:
        idade=int(input("Informe sua idade: "))
    except ValueError:
        print('Erro: Somente números inteiros permitidos!')
        time.sleep(2)
        continue
    except Exception:
        print('Erro desconhecido reiniciando o programa')
        time.spleep(2)
        continue
    novo = {'nome': nome,'idade': idade}
    pessoas.append(novo)
    for pessoa in pessoas:
        print(f'Seu nome é {pessoa['nome']} e sua idade {pessoa['idade']}')
    sair = input("Deseja sair do programa: [s]im ou [n]ão")
    if sair.lower() == 's':
        break
    else:
        print('Continuando o programa!')
        time.sleep(2)