import os
import time
#outro problema que eu vejo é o codigo todo em si, que eu entendo como ta funcionando as coisas, mas se colocasse pra eu fazer do zero, não sei colocar em codigo
def limpar_tela():
    os.system('cls')
def mostrar_lista(lista_de_pessoas):
    print('--- LISTA ATUAL DE PESSOAS ---')
    if not lista_de_pessoas:
        print(" (Nenhuma pessoa cadastrada ainda)")
    print(f"{'NOME':<20} | {'CARGO':<20} | IDADE")
    print('-' * 60)
    for pessoa in lista_de_pessoas:
        print(f"{pessoa['nome']:<20} | {pessoa['cargo']:<20} | {pessoa['idade']} anos")
def cadastrar_pessoas():
    print('\n--- NOVO CADASTRO ---')
    nome=input('Informe seu nome: ')
    cargo = input('Informe seu cargo: ')
    while True:
        try:
            idade = int(input('Informe a idade: '))
            return {'nome': nome, 'idade': idade, 'cargo': cargo}
        except ValueError:
            print('❌ Erro: Digite apenas números!')
def apagar_pessoas():
    # PASSO 1: MOSTRAR A LISTA COM OS IDS
    # Note que aqui eu NÃO pergunto nada, só mostro.
    print('--- ESCOLHA QUEM APAGAR ---')
    for id_da_lista, pessoa in enumerate(pessoas):
        # Corrigi as aspas: Usei aspas simples fora e DUPLAS dentro do dicionário
        print(f'ID: {id_da_lista} | Nome: {pessoa["nome"]} | Cargo: {pessoa["cargo"]}')
    print('-' * 60)

    # PASSO 2: PERGUNTAR (FORA DO LOOP)
    # Agora que a lista inteira já apareceu, a gente pergunta UMA vez só.
    try:
        apagar = int(input('Digite o número do ID para apagar: '))
        
        # O .pop() remove pelo índice e devolve quem foi apagado
        nome_removido = pessoas.pop(apagar) 
        
        print(f"✅ {nome_removido['nome']} foi removido com sucesso!")
        time.sleep(1)
        
    except IndexError:
        print('Erro: Esse ID não existe!')
        time.sleep(1)
    except ValueError:
        print('Erro: Digite apenas o número!')
        time.sleep(1)
pessoas = [
     {'nome': 'Eudes', 'idade': 30, 'cargo': 'Dev. Python'},
]
while True:
    limpar_tela()
    mostrar_lista(pessoas)
    print('\n[1] Cadastrar nova pessoa')
    print('[2] Apagar Cadastro')
    print('[3] Sair do sistema')
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        nova = cadastrar_pessoas()
        pessoas.append(nova)
        print('Salvo!')
        time.sleep(1)

    elif opcao == '2':
        apagar_pessoas()
    elif opcao =='3':
        print('Saindo')
        break
    else:
        print('Opção inválida!')
        time.sleep(1) 