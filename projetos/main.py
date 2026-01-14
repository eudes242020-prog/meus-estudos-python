from banco_dados import clientes, produtos
from cadastro_clientes import cadastro_completo
from produtos import cadastro_produto
from cadastro_clientes import ver_clientes
from produtos import ver_produtos
from compras import realizar_compra
adm_cliente ={
    1: "Administrador",
    2: "Cliente",
    0: "Sair"
    }
menu={
    1: "Cadastrar produto",
    2: "Ver clientes cadastrados",
    3: "Ver produtos cadastrados",
    0: "Sair"
    }
def primeiro_menu(adm_cliente):
    print('Você é:')
    for chave,opcao in adm_cliente:
        print(f'[{chave}] {opcao}')
def menu_principal(menu):
    print("\n---- MENU ----")
    for chave,valor in menu.items():
        print(f"[{chave}] {valor}")
def obter_escolha():
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        return None
def executar_sistema():
    while True:
        menu_principal(menu)
        escolha=obter_escolha()
        if escolha is None:
            continue
        if escolha==0:
            print('Saindo do programa!')
            break
        elif escolha==1:
            cadastro_completo()
        elif escolha==2:
            cadastro_produto()
        elif escolha==3:
            ver_clientes()
        elif escolha==4:
            ver_produtos()
        
executar_sistema()