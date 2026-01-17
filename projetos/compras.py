from banco_dados import produtos, clientes, vendas
from cadastro_clientes import cadastro_completo, cpf_cadastro
from utils import pausa_e_limpar
from produtos import ver_produtos
def receber_cpf():
    return cpf_cadastro()
def encontrar_cliente(cpf):
    for cliente in clientes:
        if cliente['cpf'] ==cpf:
            return cliente
    cadastro=input('Não existe cadastro deseja realizar um (sim/não): ').lower().strip
    if cadastro == 'sim':
        return cadastro_completo()
    else:
        print('Encerrando')
        return None
def selecionar_produto():
    ver_produtos()
    compra=input('Qual produto deseja comprar(nome/id): ').strip().lower()
    for produto in produtos:
        if produto['nome'].lower() ==compra or str(produto['id'])== compra:
            return produto
    print('Produto nao encontrado')
    return None
def escolher_quantidade(produto):
    while True: 
        produto=selecionar_produto()
        try:
            quantidade=int(input('Informe a quantidade do produto: '))
            if produto['estoque'] - quantidade <0:
                print('Compra não pode ser efetuada, não tem produto o suficiente!')
                pausa_e_limpar()
                continue
            else:
                print('Compra efetuada!')
                produto['estoque'] -= quantidade
                return quantidade
        except ValueError:
            print('Erro!!! informe número inteiro!!')
            pausa_e_limpar()
            continue
def registrar_compra():
    cpf = receber_cpf()
    cliente = encontrar_cliente(cpf)
    if cliente is None:
        return
    itens_compra=[]
    total_compra = 0  # Inicializa o total
    while True:
        produto = selecionar_produto()
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
        continuar = input("Deseja realizar outra compra? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
    vendas.append({
        'cliente': cliente['nome'],
        'cpf': cliente['cpf'],
        'itens': itens_compra,
        'total': round(total_compra, 2)    
        })
    print("Compra registrada com sucesso.")
    print(f"Total da compra: R${total_compra:.2f}")