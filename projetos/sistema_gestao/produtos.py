from banco_dados import produtos
from utils import pausa_e_limpar
class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.id=id
        self.nome=nome
        self.preco=preco
        self.estoque=estoque
    def ajuste(self,ajustar):
        if self.estoque + ajustar < 0:
            return 'Estoque não pode ficar negativo'
        self.estoque+=ajustar
        return
    def __str__(self):
        return f'ID: {self.id} | Nome: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}'
def pegar_string(mensagem):
    produto = input(mensagem).strip()
    return produto
def validar_nome():
    while True:
        nome=pegar_string('Informe o nome: ')
        if nome and len(nome) >= 2:
            return nome
        print('Nome não é valido')
def codigo_produto():
    id=0
    if not produtos:
        id+=1
        return id
    else:
        ids = [item['id'] for item in produtos]
        return max(ids)+1
def pegar_int(mensagem):
    numero=input(mensagem)
    return numero
def validar_numero():
    while True:
        try:
            pausa_e_limpar()
            qtd = int(pegar_int('Quantos itens deseja: '))
            if qtd < 0:
                print('A quantidade não pode ser negativa.')
                continue
            return qtd
        except ValueError:
            print('Digite apenas números inteiros.')
            continue
def validar_preco():
    while True:
        try:
            pausa_e_limpar()
            preco=float(pegar_int('Informe o valor do produto: '))
            if preco<=0:
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
            qtd = int(pegar_int('Informe a quantidade em estoque: '))
            if qtd < 0:
                print('A quantidade não pode ser negativa.')
                continue
            return qtd
        except ValueError:
            print('Digite apenas números inteiros.')
            continue
def ajuste_estoque():
    while True:
        try:
            pausa_e_limpar()
            print('[1] Para adicionar no estoque\n[0] Para tirar do estoque')
            escolha=int(pegar_int('Escolha a opção desejada: '))
            if escolha==1:
                qtd = int(pegar_int('Informe a quantidade que deseja adicionar: '))
                return qtd
            elif escolha==0:
                qtd = int(pegar_int('Informe a quantidade que deseja tira do estoque: '))
                return -qtd
            else:
                print('Opção inválida')
                continue   
        except ValueError:
            print('Digite apenas números inteiros.')
            continue
def cadastro_produto(lista_produtos):
    nome = validar_nome()
    preco = validar_preco()
    # Item de segurança: verifica se o item já está nas "prateleiras"
    for produto in lista_produtos:
        if produto.nome == nome and produto.preco == preco:
            produto.ajuste(ajuste_estoque())
            return None
    id = codigo_produto()
    quantidade = quantidade_estoque()
    cadastro_novo = Produto(id=id, nome= nome,  preco= preco, estoque = quantidade)
    print(f"Produto {nome} cadastrado com sucesso!")
    return cadastro_novo # Devolve a "peça" pronta para o main
def ver_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\n--- Produtos Cadastrados ---")
        for produto in produtos:
            print(produto)
