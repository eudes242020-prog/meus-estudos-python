produtos = [
    {"nome": "arroz", "preço": 3.50, "categoria": "mercado"},
    {"nome": "feijão", "preço": 5.20, "categoria": "mercado"},
    {"nome": "sabão", "preço": 2.00, "categoria": "limpeza"},
    {"nome": "detergente", "preço": 1.50, "categoria": "limpeza"},
    {"nome": "leite", "preço": 4.00, "categoria": "mercado"},
]
menu={1: "Cadastrar", 2: "Listar", 3: "Filtrar", 4: 'Qtd por Categoria', 0: "Sair"}
def menu_principal():
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")
def decisao_usuario():
    try:
        escolha=int(input('Qual opção deseja: '))
        if 0<= escolha<= len(menu):
            return escolha
        return None
    except ValueError:
        return None
def cadastrar_produto(listar_produtos):
    produto=input('Informe o nome do produto: ')
    try:
        preco=float(input('Informe o valor do produto: '))
        categoria=input('Informe a categoria: ')
        novo_produto={"nome": produto, "preço": preco, "categoria": categoria}
        listar_produtos.append(novo_produto)

    except ValueError:
        print('Erro de entrada!!')
def listar_produtos(lista_produtos):
    for produto in lista_produtos:
        print(f"O produto {produto['nome']} preço R${produto['preço']:.2f} categoria {produto['categoria']}")
def filtro_preço():
    try:
        if not produtos:
            return None
        valor=float(input('Gostaria de ver os itens com valor superior a R$: '))
        nova_lista=[]
        for produto in produtos:
            if produto['preço']>valor:
                nova_lista+=[produto]
        for produto in nova_lista:
            print(f"O produto {produto['nome']} preço R${produto['preço']:.2f} categoria {produto['categoria']}")
    except ValueError:
        print('Favor que o número inteiro')
def produto_categoria(produtos):
    categoria={}
    for produto in produtos:
        if produto['categoria'] in categoria:
            categoria[produto['categoria']]+=1
        else:
            categoria[produto['categoria']] = 1  
    for nome_categoria, quantidade in categoria.items():
        print(f"{nome_categoria}: {quantidade}")   
        
def executa_sistema():
    while True:
        menu_principal()
        decisao=decisao_usuario()
        if decisao is None:
            print('Erro de entrada!!')
            continue
        if decisao== 0:
            print('Saindo do programa!')
            break
        elif decisao==1:
            cadastrar_produto(produtos)
        elif decisao ==2:
            listar_produtos(produtos)
        elif decisao== 3:
            filtro_preço()
        elif decisao ==4:
            produto_categoria(produtos)
executa_sistema()
'''
Implemente a função para adicionar produtos.    

Implemente a função para listar todos.

Implemente a função para filtrar produtos com preço acima de X valor.
'''
