from banco_dados import produtos, vendas,admins
from produtos import cadastro_produto, ver_produtos 
from cadastro_clientes import ver_clientes, cadastro_completo, salvar_dados, carregar_dados
from compras import registrar_compra
from utils import pausa_e_limpar
from relatorios import listar_vendas, vendas_por_cliente, total_gasto_por_cliente
from admin import validar_admin, validar_senha,criar_admin,validar_admin,codigo_admin
from login import login_admin,login_cliente
menu_administrador = {
    1: "Criar ADMINISTRADOR",
    2: "Cadastrar produto",
    3: "Ver produtos cadastrados",
    4: "Ver clientes cadastrados",
    5: "Relatório de Vendas",
    6: "Vendas por Cliente",
    7: 'Total Gasto por Cliente',
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
    if not admins:
        criar_admin(admins)
    while True:
        primeiro_menu(adm_cliente)
        decisao = obter_escolha()
        if decisao == 0:
            print("Saindo do programa!")
            break
        elif decisao == 1:  # ADMINISTRADOR
            adm=login_admin(admins)
            if adm:
                while True:
                    menu_adm(menu_administrador)
                    escolha_admin = obter_escolha()
                    if escolha_admin == 0:
                        break
                    elif escolha_admin == 1:
                        criar_admin(admins)
                    elif escolha_admin == 2:
                        produto=cadastro_produto(produtos)
                        if produto is not None:
                            produtos.append(produto)
                        else:
                            print("Produto ajustado")
                    elif escolha_admin == 3:
                        ver_produtos()
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 4:
                        ver_clientes(clientes)
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 5:
                        listar_vendas()
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 6:
                        vendas_por_cliente()
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 7:
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
                    login=login_cliente()
                    if login is not None:
                        registrar_compra(login, produtos, vendas)
                pausa_e_limpar()                  
        else:
            print('Opção invalida')
            pausa_e_limpar()
executar_sistema()