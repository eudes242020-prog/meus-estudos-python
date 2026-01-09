pessoas =[{'nome': 'Carlos', 'idade': 35, 'profissao': 'Médico'},]
def cadastra_pessoa():
    print('Para seguir com cadastro Porfavor forneça as informções!')
    nome=input('Informe o nome: ')
    try:
        idade=int(input('Informe a idade: '))
        profi=input('Informe a profissão: ')
        nova_pessoa={'nome': nome, 'idade': idade, 'profissao': profi}
        pessoas.append(nova_pessoa)
    except ValueError:
        print('A idade precisa ser um número inteiro!!')

def filtro_pessoas():
    profi=input('Qual profissão deseja filtrar: ').strip().lower()
    encontrado = False
    for pessoa in pessoas:
        if pessoa['profissao'].lower() == profi:
            print(f"{pessoa['nome']} {pessoa['idade']}")
            encontrado = True
    if not encontrado:
        print('Nenhuma pessoa com essa profissão foi encontrada.')
