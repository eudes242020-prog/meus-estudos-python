from banco_dados import vendas
from utils import pausa_e_limpar
from banco_dados import lista_para_exibir
from cadastro_clientes import cpf_cadastro
def listar_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    for venda in vendas:
        print(f"\nCliente: {venda['cliente']}")
        print(f"CPF: {venda['cpf']}")
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
def total_gasto_por_cliente():
    if not vendas:
        print('Não existe vendas a serem exibidas!')
        return
    totais_por_cliente = {}
    for venda in vendas:
        cpf = venda['cpf']
        totais_por_cliente.setdefault(cpf, 0)  # garante que o cpf existe no dicionário
        for item in venda['itens']:
            total_item = item['quantidade'] * item['preço unitario']
            totais_por_cliente[cpf] += total_item
    # Mostrar os resultados
    for cpf, total in totais_por_cliente.items():
        print(f"CPF: {cpf} | Total gasto: R${total:.2f}")
