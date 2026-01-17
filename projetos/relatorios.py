from banco_dados import vendas
from utils import pausa_e_limpar
from banco_dados import clientes
from cadastro_clientes import cpf_cadastro
def listar_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    for venda in vendas:
        print(f"\nCliente: {venda['cliente']}")
        print(f"CPF: {venda['cpf']}")
        for item in venda['itens']:
            if not venda['itens']:
                print("Cliente não tem compras!")
            else:
                print("Itens comprados:")
                for item in venda['itens']:
                    print(f" - {item['produto']} | Quantidade: {item['quantidade']} | Preço unitário: R${item['preço unitario']:.2f}")
        print(f"Total da compra: R${venda['total']:.2f}")
        print("-" * 40)
def vendas_por_cliente():
    cpf = cpf_cadastro()
    encontrou = False

    for venda in vendas:
        if venda['cpf'] == cpf:
            encontrou = True
            print(f"\nCliente: {venda['cliente']}")
            print(f"CPF: {venda['cpf']}")

            itens = venda.get('itens', [])
            if not itens:
                print("Cliente não tem compras!")
            else:
                print("Itens comprados:")
                for item in itens:
                    if isinstance(item, dict):  # Confirma que item é dicionário
                        print(f" - {item['produto']} | Quantidade: {item['quantidade']} | Preço unitário: R${item['preço unitario']:.2f}")
            print(f"Total da compra: R${venda.get('total', 0):.2f}")
            print("-" * 40)

    if not encontrou:
        print("Nenhuma compra encontrada para este CPF.")

vendas_por_cliente()
