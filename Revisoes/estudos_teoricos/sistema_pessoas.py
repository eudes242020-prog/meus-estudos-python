import os
import time
def limpar_tela():
    os.system('cls')
def mostrar_lista(lista_de_pessoas):
    print('--- LISTA ATUAL DE PESSOAS ---')
    if not lista_de_pessoas:
        print(" (Nenhuma pessoa cadastrada ainda)")
    print(f"{'NOME':<20} | {'CARGO':<20} | IDADE")
    print("-" * 60)
    for pessoa in lista_de_pessoas:
        print(f"{pessoa['nome']:<20} | {pessoa['cargo']:<20} | {pessoa['idade']} anos")
def cadastrar_pessoas():
    print('\n--- NOVO CADASTRO ---')
    nome=input('Informe seu nome: ')
    cargo = input('Informe seu cargo: ')
    while True:
        try:
            idade = int(input("Informe a idade: "))
            return {'nome': nome, 'idade': idade, 'cargo': cargo}
        except ValueError:
            print('❌ Erro: Digite apenas números!')
pessoas = [
     {'nome': 'Eudes', 'idade': 30, 'cargo': 'Dev. Python'},
]
while True:
    limpar_tela()
    mostrar_lista(pessoas)
    
    print("\n[1] Cadastrar nova pessoa")
    print("[2] Sair do sistema")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        # Só chama o cadastro se a pessoa escolher 1
        nova = cadastrar_pessoas()
        pessoas.append(nova)
        print("✅ Salvo!")
        time.sleep(1)
        
    elif opcao == '2':
        print("Saindo...")
        break
        
    else:
        print("Opção inválida!")
        time.sleep(1)