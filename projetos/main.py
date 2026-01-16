from banco_dados import clientes, produtos
from cadastro_clientes import cadastro_completo
from produtos import cadastro_produto
from cadastro_clientes import ver_clientes
from produtos import ver_produtos
from compras import registrar_compra
from utils import pausa_e_limpar
menu_administrador = {
    1: "Cadastrar produto",
    2: "Ver produtos cadastrados",
    3: "Ver clientes cadastrados",
    0: "Voltar"
}
adm_cliente ={
    1: "Administrador",
    2: "Cliente",
    0: "Sair"
    }
menu_cliente={
    1: "Fazer cadastro",
    2: "Realizar compra",
    0: "Voltar"
}
def menu_adm(menu_administrador):
    print('Escolha uma opção')
    for chave, valor in menu_administrador.items():
        print(f"[{chave}] {valor}")
def primeiro_menu(adm_cliente):
    print('Você é:')
    for chave,opcao in adm_cliente.items():
        print(f'[{chave}] {opcao}')
def menu_clientes(menu_cliente):
    print("\n---- MENU ----")
    for chave,valor in menu_cliente.items():
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
        primeiro_menu(adm_cliente)
        decisao = obter_escolha()

        if decisao == 0:
            print("Saindo do programa!")
            break

        elif decisao == 1:  # ADMINISTRADOR
            while True:
                menu_adm(menu_administrador)
                escolha_admin = obter_escolha()
                if escolha_admin == 0:
                    break
                elif escolha_admin == 1:
                    cadastro_produto()
                elif escolha_admin == 2:
                    ver_produtos()
                elif escolha_admin == 3:
                    ver_clientes()
                pausa_e_limpar()
        elif decisao == 2:  # CLIENTE
            while True:
                menu_clientes(menu_cliente)
                escolha_cliente = obter_escolha()
                if escolha_cliente == 0:
                    break
                elif escolha_cliente == 1:
                    cadastro_completo()
                elif escolha_cliente == 2:
                    registrar_compra()
                pausa_e_limpar()
        else:
            print('Opção invalida')
            pausa_e_limpar()
executar_sistema()