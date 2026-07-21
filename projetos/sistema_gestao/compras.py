from banco_dados import produtos, lista_para_exibir, vendas
from cadastro_clientes import cadastro_completo, cpf_cadastro
from utils import pausa_e_limpar
from produtos import ver_produtos, validar_numero, pegar_int
def receber_cpf():
    return cpf_cadastro()
def encontrar_cliente(cpf, lista_clientes):
    while True:
        # 1. Tenta achar o cliente na lista
        for cliente in lista_clientes:
            if cliente['cpf'] == cpf:
                return cliente 
        print(f"CPF {cpf} não encontrado no sistema.")
        escolha = input("Deseja realizar o cadastro agora para continuar a compra? (sim/não): ").lower().strip()
        if escolha == 'sim':
            novo = cadastro_completo(lista_clientes)
            if novo:
                lista_clientes.append(novo)
                return novo # SUCESSO 2: Cadastrou e já retorna o novo cliente
        else:
            print("Para comprar, é necessário um CPF cadastrado.")
            cpf = input("Por favor, informe um CPF válido ou cadastrado: ").strip()
def selecionar_produto(lista_produtos):
    ver_produtos()
    compra=input('Qual produto deseja comprar(nome/id): ').strip().lower()
    for produto in lista_produtos:
        if produto.nome.lower() ==compra or str(produto.id)== compra:
            return produto
    print('Produto nao encontrado')
    return None
def registrar_compra(lista_clientes, lista_produtos, lista_vendas):
    cpf = receber_cpf()
    # 1. Passamos a lista para buscar o cliente real na memória
    cliente = encontrar_cliente(cpf, lista_clientes)
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
        item = {"id": produto.id, "nome": produto.nome, "preço": produto.preco, "quantidade": quantidade} 
        itens_compra.append(item)
        total_compra += quantidade * produto.preco
        continuar = input("Deseja adicionar outro item? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
    # 4. Adicionamos na lista de vendas que o main gerencia
    lista_compra={"cliente": cliente['nome'], "cpf": cpf, "itens": itens_compra, "total": total_compra}
    lista_vendas.append(lista_compra)
    print(f"Compra finalizada! Total: R${total_compra:.2f}")