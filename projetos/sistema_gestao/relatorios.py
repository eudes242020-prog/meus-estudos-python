from banco_dados import vendas
from utils import pausa_e_limpar
from banco_dados import lista_para_exibir
from cadastro_clientes import cpf_cadastro
def listar_vendas(vendas):
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    for venda in vendas:
        print(f"\nCliente: {venda.cliente.nome}")
        print(f"CPF: {venda.cliente.cpf}")
        if not venda.produtos:
            print("Cliente não tem compras!")
        else:
            print("Itens comprados:")
            for item in venda.produtos:
                print(f" - {item['produto']} | Quantidade: {item['quantidade']} | Preço unitário: R${item['preço unitario']:.2f}")
        print(f"Total da compra: R${venda.valor_total}")
        print("-" * 40)
def vendas_por_cliente(itens,clientes):
    cpf = cpf_cadastro()
    cadastro=False
    encontrou = False
    if clientes:
        for pessoa in clientes:
            if pessoa.cpf==cpf:
                cadastro=True
                break
    for venda in itens:
        if venda.cliente.cpf == cpf:
            encontrou = True
            print(f"\nCliente: {venda.cliente.nome}")
            print(f"CPF: {venda.cliente.cpf}")
            if not venda.produtos:
                print("Cliente não tem compras!")
            else:
                print("Itens comprados:")
                for item in venda.produtos:
                    print(f"Produto:  {item['produto']} | Quantidade: {item['quantidade']}| Preço unitario: R${item['preço unitario']:.2f}")
            print("-" * 40)
    if not cadastro:
        print("Cliente não cadastrado.")
    else:
        if encontrou:
            pass
        else:
            print("Cliente não tem compras!")
def total_gasto_por_cliente(vendas):
    if not vendas:
        print('Não existe vendas a serem exibidas!')
        return
    totais_por_cliente = {}
    for venda in vendas:
        cpf = venda.cliente.cpf  
        for item in venda.produtos:
            total_item = item['quantidade'] * item['preço unitario']
            if cpf in totais_por_cliente:
                totais_por_cliente[cpf] += total_item
            else:
                totais_por_cliente[cpf] = total_item
    # Mostrar os resultados
    for cpf, total in totais_por_cliente.items():
        print(f"CPF: {cpf} | Total gasto: R${total:.2f}")
def clientes_sem_compra(compras,clientes):
    nova_lista=[]
    for cliente in clientes:
        possui_compra = False
        for compra in compras:
            if cliente.cpf==compra.cliente.cpf:
                possui_compra=True
                break
        if not possui_compra:
            nova_lista.append(cliente)
    if not nova_lista:
        print('Não existe cliente sem compras')
        return
    for novo in nova_lista:
        print(novo)
