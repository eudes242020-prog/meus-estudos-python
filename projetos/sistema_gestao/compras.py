import datetime
from produtos import ver_produtos, validar_numero
def selecionar_produto(lista_produtos):
    ver_produtos(lista_produtos)
    compra=input('Qual produto deseja comprar(nome/id): ').strip().lower()
    for produto in lista_produtos:
        if produto.nome.lower() ==compra or str(produto.id)== compra:
            return produto
    print('Produto nao encontrado')
    return None
def registrar_compra(login, lista_produtos, lista_vendas):
    # 1. Passamos a lista para buscar o cliente real na memória
    if not lista_produtos:
        return None
    cliente = login
    if cliente is None:
        return None# Sai da função se o usuário desistir
    itens_compra = []
    total_compra = 0
    while True:
        # 2. Passamos a lista de produtos para seleção
        produto = selecionar_produto(lista_produtos) 
        if produto is None:
            sair=input('Aperte [0] para sair da compra: ')
            if sair !='0':
                continue
            break
        quantidade = validar_numero()
        feita= -quantidade
        ajuste=produto.ajuste(feita)
        if ajuste is not None:
            print('Estoque não pode ficar negativo')
            continue
        item = {"id": produto.id, "produto": produto.nome, "preço unitario": produto.preco, "quantidade": quantidade} 
        itens_compra.append(item)
        total_compra += quantidade * produto.preco
        continuar = input("Deseja adicionar outro item? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
    # 4. Adicionamos na lista de vendas que o main gerencia
    if not itens_compra:
        return None
    venda=Venda(cliente= cliente, produtos= itens_compra,  valor_total= total_compra)
    lista_vendas.append(venda)
    print(f"Compra finalizada! Total: R${venda.valor_total:.2f}")
    return venda
class Venda:
    def __init__(self, cliente, produtos,valor_total):
        self.cliente=cliente
        self.produtos=produtos
        self.valor_total=valor_total
        self.data = datetime.datetime.now()
    