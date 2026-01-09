livros = [{
    "título": "",
    "autor": "",
    "gênero": ""}]
menu={1: "Cadastrar livros", 2: "Listar livros", 3: "Filtrar por gênero", 4: 'Qtd por autor', 0: "Sair"}
def menu_principal(menu):
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")
def decisao_usuario(menu):
    try:
        decisao=int(input("Informe oque deseja: "))
        if 0<= decisao<=len(menu):
            return decisao
        return None
    except ValueError:
        return None
def cadastra_livro(livros):
    titulo=input('Informe o título do livro: ')
    autor=input('Informe o autor do livro: ')
    genero=input('Informe o gênero do livro: ')
    novo_livro={"título": titulo, "autor": autor, "gênero": genero}
    if livros[0]['título'] =='' and livros[0]['autor']=='' and livros[0]['gênero']=='':
        livros[0] = novo_livro
    else:
        livros.append(novo_livro)
def listar_livros(livros):
    for livro in livros:
        print(f"Título:{livro['título']} Autor:{livro['autor']} Gênero{livro['gênero']}")
def buscar_genero(livros):
    busca=input('Qual gênero deseja buscar: ')
    nova_lista=[]
    for livro in livros:
        if livro['gênero'].lower() == busca.lower():
            nova_lista.append(livro)
    if not nova_lista:
        print("Nenhum livro encontrado para esse gênero.")
    for livro in nova_lista:
        print(f"Título: {livro['título']} | Autor: {livro['autor']} | Gênero: {livro['gênero']}")
def quantidade_autor(livros):
    lista_autor={}
    for livro in livros:
        if livro['autor'] in lista_autor:
            lista_autor[livro['autor']]+=1
        else:
            lista_autor[livro['autor']] = 1 
    for autor, quantidade in lista_autor.items():
        print(f'{autor}: {quantidade}')
def executar_sistema():
    while True:
        menu_principal(menu)
        decisao=decisao_usuario(menu)
        if decisao is None:
            print('Erro de entrada')
            continue
        elif decisao ==0:
            print("Saindo do programa!!")
            break
        elif decisao==1:
            cadastra_livro(livros)
        elif decisao ==2:
            listar_livros(livros)
        elif decisao==3:
            buscar_genero(livros)
        elif decisao==4:
            quantidade_autor(livros)
executar_sistema()