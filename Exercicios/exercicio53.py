import time
import os
menu={1: "Cadastrar funcionário", 2: "Listar funcionários", 3: "Buscar funcionário por cargo", 4: "Ver salário médio por cargo", 0: "Sair"}
funcionarios=[]
def opcoes_menu(menu):
    for chave,opcao in menu.items():
        print(f'[{chave}] {opcao}')
def escolha_usuario():
    try:
        escolha=int(input('Escolha uma opção: '))
        if 0<=escolha<=len(menu):
            return escolha
        return None
    except ValueError:
        return None
def nome_funcionario():
    nome=input('Informe o nome do funcionario: ').strip().lower()
    if nome:
        return nome
    return None
def cargo_funcionario():
    cargo=input('Informe o cargo do funcionario: ').strip().lower()
    if cargo:
        return cargo
    return None
def salario_funcionario():
    try:
        salario=float(input('Informe o salario do salário do funcionario: '))
        if salario <0:
            return None
        return salario
    except ValueError:
        return None
def cadastro_funcionario(nome, cargo, salario):
    novo_funcionario={"nome": nome, "cargo": cargo, 'salario': salario}
    funcionarios.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso!")
def listar_funcionario(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    for funcionario in funcionarios:
        print(f"Nome do funcionario {funcionario['nome']} função {funcionario['cargo']}")
def buscar_cargo(funcionarios):
    lista_nova=[]
    cargo=input('Informe o cargo que gostaria de pesquisa: ').strip().lower()
    if not cargo:
        print('Precisa preencher a informação necessaria')
    for funcionario in funcionarios:
        if funcionario['cargo'] == cargo:
            lista_nova.append(funcionario)
    if not lista_nova:
        print('Nenhum funcionário encontrado com esse cargo.')
    else:
        for pessoa in lista_nova:
            print(f'{pessoa['nome']} | {pessoa['cargo']}')
def media_salario_cargo(funcionarios):
    salarios=[]
    cargo=input('Informe o cargo que gostaria de pesquisa: ').strip().lower()
    for pessoa in funcionarios:
        if pessoa['cargo']== cargo:
            salarios.append(pessoa['salario'])
    if salarios:
        media=sum(salarios)/len(salarios)
        print(f'A media salarial do cargo {cargo} é de {media:.2f}')
    else:
        print('Nenhum funcionário encontrado com esse cargo.')
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')        
def executar_sistema():
    while True:
        opcoes_menu(menu)
        decisao=escolha_usuario()
        if decisao is None:
            print('Erro de entrada!')
            pausar_e_limpar()
            continue
        if decisao==0:
            print('Saindo do programa!')
            break
        if decisao==1:
            nome=nome_funcionario()
            salario=salario_funcionario()
            cargo=cargo_funcionario()
            if nome is None or salario is None or cargo is None:
                print('Erro de entrada: todos os campos devem ser preenchidos corretamente.')
                pausar_e_limpar()
                continue
            cadastro_funcionario(nome, cargo, salario)    
        elif decisao==2:
            listar_funcionario(funcionarios)
        elif decisao==3:
            buscar_cargo(funcionarios)
        elif decisao==4:
            media_salario_cargo(funcionarios)
        pausar_e_limpar()
executar_sistema()