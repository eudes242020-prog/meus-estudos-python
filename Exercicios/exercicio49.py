livros = []

menu = {1:'Cadastrar livros', 2: 'Listar livros', 0: 'Sair'}

def menu_principal():
    for chave,valor in menu.items():
        print(f"[{chave}] {valor}")

def decisao_usuario():
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha >= 0 and escolha <= len(menu):
            return escolha
        print('Opção inválida!!')
    except ValueError:
        return None
def cadastrar_livro():
    titulo = input("Informe o nome do livro: ")
    autor = input("Informe o nome do autor: ")
    genero = input("Informe o gênero do livro: ")
    if not titulo or not autor or not genero:
        print("Todos os campos devem ser preenchidos.")
        return
    novo_livro = {'título':titulo, 'autor':autor, 'gênero': genero}
    livros.append(novo_livro)

def listar_livros():
    if livros == []:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"Título: {livro['título']} | Autor: {livro['autor']} | Gênero: {livro['gênero']}")

def executar_sistema():
    while True:
        menu_principal()
        decisao = decisao_usuario()
        if decisao == 0:
            print("Saindo...")
            break
        elif decisao == 1:
            cadastrar_livro()
        elif decisao == 2:
            listar_livros()
        else:
            print("Opção inválida.")

executar_sistema()