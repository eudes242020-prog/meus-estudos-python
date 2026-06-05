filmes = {
    "Ação": [],
    "Drama": [],
    "Comédia": []
}

menu = {
    1: "Cadastrar filme",
    2: "Listar filmes por gênero",
    0: "Sair"
}

def menu_principal():
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")

def decisao_usuario():
    try:
        return int(input("Escolha uma opção: "))
    except:
        return None

def cadastrar_filme():
    genero = input("Informe o gênero (Ação, Drama, Comédia): ").capitalize()
    if genero not in filmes:
        print("Gênero inválido.")
        return
    titulo = input("Informe o título do filme: ").capitalize()
    filmes[genero] = titulo
    print("Filme cadastrado com sucesso!")

def listar_filmes_por_genero():
    genero = input("Qual gênero deseja listar? ").capitalize()
    if genero in filmes:
        if not filmes[genero]:
            print("Nenhum filme cadastrado nesse gênero.")
        else:
            for titulo in filmes[genero]:
                print(f"- {titulo}")
    else:
        print("Gênero inválido.")

def executar_sistema():
    while True:
        menu_principal()
        escolha = decisao_usuario()
        if escolha == 0:
            print("Saindo...")
            break
        elif escolha == 1:
            cadastrar_filme()
        elif escolha == 2:
            listar_filmes_por_genero()
        else:
            print("Opção inválida!")

executar_sistema()