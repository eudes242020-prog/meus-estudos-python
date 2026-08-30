from banco_dados import vendas,admins,criar_tabela_produto,salvar_produtos,carregar_produtos,compras_produtos,ajuste_de_estoque,apagar_produto,criar_tabela_venda,criar_tabela_itens,salvar_itens_venda,salvar_venda
from produtos import cadastro_produto, ver_produtos, ajuste_produto, remover_produto
from cadastro_clientes import ver_clientes, cadastro_completo, salvar_dados, carregar_dados
from compras import registrar_compra,Venda
from utils import pausa_e_limpar
from relatorios import listar_vendas, vendas_por_cliente, total_gasto_por_cliente,clientes_sem_compra
from admin import validar_admin, validar_senha,criar_admin,validar_admin,codigo_admin
from login import login_admin,login_cliente
menu_administrador = {
    1: "Criar ADMINISTRADOR",
    2: "Cadastrar produto",
    3: "Ver produtos cadastrados",
    4: 'Gerenciar produto',
    5: "Ver clientes cadastrados",
    6: "Relatório de Vendas",
    7: "Vendas por Cliente",
    8: 'Total Gasto por Cliente',
    9: 'Cliente que nunca compraram',
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
    criar_tabela_produto()
    criar_tabela_itens()
    criar_tabela_venda()
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
                        produto=cadastro_produto(carregar_produtos())
                        salvar_produtos(produto)
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 3:
                        ver_produtos(carregar_produtos())
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 4:
                        print('[1] para ajustar estoque')
                        print('[2] para apagar do estoque')
                        p=obter_escolha()
                        if p == 1:
                            ajuste=ajuste_produto(carregar_produtos())
                            if ajuste is not None:
                                ajuste_de_estoque(ajuste)
                                print('Produto ajustado')
                        elif p == 2:
                            remover=remover_produto(carregar_produtos())
                            if remover is not None:
                                apagar_produto(remover)
                                print('PRODUTO REMOVIDO')
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 5:
                        ver_clientes(clientes)
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 6:
                        listar_vendas(vendas)
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 7:
                        vendas_por_cliente(vendas,clientes)
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 8:
                        total_gasto_por_cliente(vendas)
                        input('\nPressione ENTER para voltar...')
                    elif escolha_admin == 9:
                        clientes_sem_compra(vendas,clientes)
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
                        venda=registrar_compra(login, carregar_produtos(), vendas)
                        if venda is None:
                            break
                        for v in venda.produtos:
                            compras_produtos(v['id'],v['quantidade'])
                        efetuada=salvar_venda(venda)
                        salvar_itens_venda(venda,efetuada)
                pausa_e_limpar()                  
        else:
            print('Opção invalida')
            pausa_e_limpar()
executar_sistema()