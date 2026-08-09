from produtos import ver_produtos, validar_numero
def selecionar_produto(lista_produtos):
    ver_produtos()
    compra=input('Qual produto deseja comprar(nome/id): ').strip().lower()
    for produto in lista_produtos:
        if produto.nome.lower() ==compra or str(produto.id)== compra:
            return produto
    print('Produto nao encontrado')
    return None
def registrar_compra(login, lista_produtos, lista_vendas):
    # 1. Passamos a lista para buscar o cliente real na memória
    cliente = login
    if cliente is None:
        return None# Sai da função se o usuário desistir
    itens_compra = []
    total_compra = 0
    while True:
        # 2. Passamos a lista de produtos para seleção
        produto = selecionar_produto(lista_produtos) 
        if not produto:
            continue
        quantidade = validar_numero()
        feita= -quantidade
        produto.ajuste(feita)
        item = {"id": produto.id, "produto": produto.nome, "preço unitario": produto.preco, "quantidade": quantidade} 
        itens_compra.append(item)
        total_compra += quantidade * produto.preco
        continuar = input("Deseja adicionar outro item? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
    # 4. Adicionamos na lista de vendas que o main gerencia
    lista_compra={"cliente": cliente.nome, "cpf": cliente.cpf, "itens": itens_compra, "total": total_compra}
    lista_vendas.append(lista_compra)
    print(f"Compra finalizada! Total: R${total_compra:.2f}")