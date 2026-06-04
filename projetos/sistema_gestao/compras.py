from banco_dados import produtos, lista_para_exibir, vendas
from cadastro_clientes import cadastro_completo, cpf_cadastro
from utils import pausa_e_limpar
from produtos import ver_produtos
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
        if produto['nome'].lower() ==compra or str(produto['id'])== compra:
            return produto
    print('Produto nao encontrado')
    return None
def escolher_quantidade(produto):
    while True: 
        try:
            quantidade=int(input('Informe a quantidade do produto: '))
            if quantidade <= 0:
                print('A quantidade deve ser maior que zero.')
                pausa_e_limpar()
                continue
            if produto['estoque'] - quantidade <0:
                print('Compra não pode ser efetuada, não tem produto o suficiente!')
                pausa_e_limpar()
                continue
            else:
                return quantidade
        except ValueError:
            print('Erro!!! informe número inteiro!!')
            pausa_e_limpar()
            continue
def registrar_compra(lista_clientes, lista_produtos, lista_vendas):
    cpf = receber_cpf()
    # 1. Passamos a lista para buscar o cliente real na memória
    cliente = encontrar_cliente(cpf, lista_clientes)
    if cliente is None:
        return # Sai da função se o usuário desistir
    itens_compra = []
    total_compra = 0
    while True:
        # 2. Passamos a lista de produtos para seleção
        produto = selecionar_produto(lista_produtos) 
        if not produto:
            continue
        quantidade = escolher_quantidade(produto)
        if quantidade is None:
            continue 
        produto['estoque'] -= quantidade
        item = {
            'produto': produto['nome'],
            'quantidade': quantidade,
            'preço unitario': produto['preço']
        }
        itens_compra.append(item)
        total_compra += quantidade * produto['preço']
        continuar = input("Deseja adicionar outro item? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
    # 4. Adicionamos na lista de vendas que o main gerencia
    lista_vendas.append({
        'cliente': cliente['nome'],
        'cpf': cliente['cpf'],
        'itens': itens_compra,
        'total': round(total_compra, 2)
    })
    print(f"Compra finalizada! Total: R${total_compra:.2f}")