'''
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados
exiba
seu nome ...
seu nome invertido é ...
seu nome contém (ou não) espaços
Seu nome conte {n} letras
A primeira letra do seu nome é ...
A última letra do seu nome é ...
se nada for digitado em nome ou idade 
exiba
"Desculpe, você deixou campos vazios."
'''
nome = input ('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_limpo = nome.strip()
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome) - nome.count(" ")}')
    print(f'A primeira letra do seu nome é {nome_limpo[0]}')
    print(f'A última letra do seu nome é {nome_limpo[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')