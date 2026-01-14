from banco_dados import produtos
from utils import pausa_e_limpar
def nome_produto():
    while True:
        pausa_e_limpar()
        produto = input('Informe o nome: ').strip()
        if produto and len(produto) >= 2:
            return produto.capitalize()
        print("Nome inválido. Informe pelo menos 2 caracteres.")
def codigo_produto():
    id=0
    if not produtos:
        id+=1
        return id
    else:
        ids = [item['id'] for item in produtos]
        return max(ids)+1
def preco_produto():
    while True:
        try:
            pausa_e_limpar()
            preco=float(input('Informe o valor do produto: '))
            if preco<0:
                print('Apenas números positivo para adicionar um preço')
                continue
            return preco
        except ValueError:
            print('Apenas números são permitidos')
            continue
def quantidade_estoque():
    while True:
        try:
            pausa_e_limpar()
            qtd = int(input('Informe a quantidade em estoque: '))
            if qtd < 0:
                print('A quantidade não pode ser negativa.')
                continue
            return qtd
        except ValueError:
            print('Digite apenas números inteiros.')
            continue
def ajuste_estoque(quantidade_estoque):
    while True:
        estoque=quantidade_estoque
        try:
            pausa_e_limpar()
            print('[1] Para adicionar no estoque\n[0] Para tira do estoque')
            escolha=int(input('Escolha a opção desejada: '))
            if escolha==1:
                qtd = int(input('Informe a quantidade que deseja adicionar: '))
                if qtd < 0:
                    print('A quantidade não pode ser negativa.')
                    continue
                return qtd
            elif escolha==0:
                qtd = int(input('Informe a quantidade que deseja tira do estoque: '))
                if estoque - qtd < 0:
                    print('Estoque não pode ficar negativo.')
                    continue
                return -qtd
            else:
                print('Opção inválida')
                continue   
        except ValueError:
            print('Digite apenas números inteiros.')
            continue
def cadastro_produto():
    nome=nome_produto()
    preco=preco_produto()
    id=codigo_produto()
    quantidade=quantidade_estoque()
    produto_encontrado = False
    if None in (nome,preco,id,quantidade):
        print('Erro de entrada!')
        return None
    for produto in produtos:
        if produto['nome'] == nome and produto['preço'] == preco:
            ajuste=ajuste_estoque(produto['estoque'])
            if ajuste is not None:
                produto['estoque'] += ajuste
            produto_encontrado = True
            break
    if not produto_encontrado:    
        cadastro_novo={'id': id,'nome': nome, 'preço': preco, 'estoque':quantidade}
        produtos.append(cadastro_novo)
def ver_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\n--- Produtos Cadastrados ---")
        for produto in produtos:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R${produto['preço']:.2f} | Estoque: {produto['estoque']}")
