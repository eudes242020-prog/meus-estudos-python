menu=['Adicionar aluno em uma turma','Listar todos os alunos de uma turma','Listar todas as turmas existentes']
turmas = {
    "A": [{"nome": "Carlos", "idade": 15}, {"nome": "Ana", "idade": 14}],
    "B": [{"nome": "João", "idade": 13}]
}
def obter_opcao_menu():
    print('----MENU----')
    for i, opcao in enumerate(menu,1):
        print(f"[{i}] {opcao}")
    print('[0] Para sair do programa aperto')
    try:
        numero=int(input('Oque deseja: '))
        if 0<= numero<=len(menu):
            return numero
        return None
    except ValueError:
        return None
def adicionar_aluno():
    turma=input('Deseja adicionar o aluno em que turma: [A] ou [B]: ').upper()
    if turma not in turmas:
        return None
    nome=input('Informe o nome do aluno: ').capitalize()
    try:
        idade=int(input('Informe a idade do aluno: '))
        novo_aluno={"nome": nome, "idade": idade}
        turmas[turma].append(novo_aluno)
    except:
        return None
def listar_turma_especifica():
    turma=input('Deseja listar os alunos em que turma: [A] ou [B]: ').upper()
    if turma not in turmas:
        return None
    for aluno in turmas[turma]:
        print(f'Nome do aluno {aluno["nome"]} idade {aluno["idade"]}')
def listar_todas():
    for turma in turmas:
        for aluno in turmas[turma]:
            print(f'Nome do aluno {aluno["nome"]} tem {aluno["idade"]} anos')
def executar_sistema():
    while True:
        decisao=obter_opcao_menu()
        if decisao is None:
            print('Erro de entrada')
        if decisao ==0:
            print('Saindo do programa!')
            break
        elif decisao == 1:
            adicionar_aluno()
        elif decisao==2:
            listar_turma_especifica()
        else:
            listar_todas()
executar_sistema()