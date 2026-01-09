'''Exercício 2: Validador de Senha Simples

Crie um sistema de login simples que use a lógica booleana e operadores relacionais para validar credenciais.

    Defina duas variáveis fixas (no código, não use input()):

        USUARIO_CORRETO = 'admin'

        SENHA_CORRETA = '123456'

    Use a função input() para pedir ao usuário que digite o nome de usuário e a senha.

    Use um único if para verificar se ambas as credenciais digitadas pelo usuário correspondem às credenciais corretas.
   
     A saída deve ser:

        Se correto: Login bem-sucedido. Bem-vindo!

         Se incorreto: Acesso negado. Usuário ou senha incorretos.'''
# usuario_correto = 'admin'
# senha_correta = '123456'
# usuario = input('Digite o nome do usúario: ')
# senha = input('Digite a senha: ')
# if usuario == usuario_correto and senha == senha_correta:
#     print('Login bem-sucedido. Bem-vindo!')
# else:
#     print('Acesso negado. Usúario ou senha incorretos.')
'''Crie um programa que imprima os números pares de 1 a 20'''
# for numero in range(1,21):
#     if numero %2==0:
#         print(numero)
# try:
#     n1=int(input('Digite um número: '))
#     for item in range(1,11):
#         print(n1*item)
# except ValueError:
#     print('digite um número inteiro')

# for nome in range(6):
#     print('Treinando')
'''Crie uma lista vazia chamada frutas

Peça ao usuário para digitar 3 frutas (com input())

Adicione cada fruta à lista usando append()

Ao final, mostre a lista completa com print()'''
frutas=[]
def adicionar_3_fruta():
    for fruta in range(3):
        fruta=input('Informe uma fruta: ')
        frutas.append(fruta)
    print(frutas)
adicionar_3_fruta()
def remover_fruta():
    try:
        fruta=input('Informe uma fruta pra retira: ').lower()
        frutas.remove(fruta)
        print(frutas)
    except ValueError:
        print('Essa fruta não existe na lista')
remover_fruta()
def remover_todas_frutas():
    fruta=input('Deseja remover todas as frutas: [s]im ou [n]ão')
    if fruta in 's':
        frutas.clear()
        print(frutas)
'''Peça ao usuário para digitar o nome de uma fruta a ser removida da lista

Use remove() para tentar excluir

Se a fruta não estiver na lista, mostre uma mensagem de erro

Ao final, exiba a lista atualizada'''
