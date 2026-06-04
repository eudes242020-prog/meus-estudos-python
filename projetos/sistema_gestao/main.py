from banco_dados import lista_para_exibir, produtos, vendas
from produtos import cadastro_produto, ver_produtos 
from cadastro_clientes import ver_clientes, cadastro_completo, salvar_dados, carregar_dados
from compras import registrar_compra
from utils import pausa_e_limpar
from relatorios import listar_vendas, vendas_por_cliente, total_gasto_por_cliente

menu_administrador = {
    1: "Cadastrar produto",
    2: "Ver produtos cadastrados",
    3: "Ver clientes cadastrados",
    4: "Relatório de Vendas",
    5: "Vendas por Cliente",
    6: "Total Gasto por Cliente",
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
    clientes = carregar_dados()
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
                    input('\nPressione ENTER para voltar...')
                elif escolha_admin == 3:
                    ver_clientes(clientes)
                    input('\nPressione ENTER para voltar...')
                elif escolha_admin == 4:
                    listar_vendas()
                    input('\nPressione ENTER para voltar...')
                elif escolha_admin == 5:
                    vendas_por_cliente()
                    input('\nPressione ENTER para voltar...')
                elif escolha_admin == 6:
                    total_gasto_por_cliente()
                    input('\nPressione ENTER para voltar...')
                pausa_e_limpar()
        elif decisao == 2:  # CLIENTE
            while True:
                menu_clientes(menu_cliente)
                escolha_cliente = obter_escolha()
                if escolha_cliente == 0:
                    break
                elif escolha_cliente == 1:
                    novo = cadastro_completo(clientes)
                    if novo is not None: 
                        clientes.append(novo)
                        salvar_dados(clientes)
                elif escolha_cliente == 2:
                    registrar_compra(clientes, produtos, vendas)
                pausa_e_limpar()
        else:
            print('Opção invalida')
            pausa_e_limpar()
executar_sistema()