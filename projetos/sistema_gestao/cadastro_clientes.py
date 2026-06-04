import json
from utils import pausa_e_limpar
def nome_cadastro():
    while True:
        pausa_e_limpar()
        nome = input('Informe o nome: ').strip()
        if nome and len(nome) >= 2:
            return nome.capitalize()
        print("Nome inválido. Informe pelo menos 2 caracteres.")
def cpf_cadastro():
    while True:
        pausa_e_limpar()
        cpf_limpo = ''
        cpf_sujo = input('Informe seu CPF: ')
        for numero in cpf_sujo:
            if numero.isdigit():
                cpf_limpo += numero
        cpf_limpo = cpf_limpo[:11] 
        if len(cpf_limpo) < 11:
            print('CPF incompleto.')
            continue
        sucesso = validar_cpf(cpf_limpo)
        if sucesso:
            return cpf_limpo
        print('CPF inválido. Tente novamente.')
def validar_cpf(cpf):
    primeiro_caractere = cpf[0]
    sequencia_repetida = primeiro_caractere * len(cpf)
    if cpf == sequencia_repetida:
        print('Você digitou dados iguais, CPF invalido!')
        return False
    nove_digitos=cpf[:9] 
    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1-=1
    digit_1 = (resultado_digito_1*10) % 11
    if digit_1 >9:
        digit_1 = 0
    dez_digitos = nove_digitos + str(digit_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2+=int(digito) * contador_regressivo_2
        contador_regressivo_2-=1
    digit_2 = (resultado_digito_2 *10) % 11
    if digit_2 >9:
        digit_2 = 0
    cpf_calculado = f'{nove_digitos}{digit_1}{digit_2}'
    if cpf == cpf_calculado:
        return True
    return False
def email_cadastro():
    while True:
        pausa_e_limpar()
        email=input('Informe o email: ').strip().lower()
        if email.count('@') != 1:
            print('Email inválido.')
            continue
        partes = email.split('@')
        if "." in partes[1] and partes[0]:
            return email
        print('Email inválido.')
def cadastro_completo(lista_atual):
    nome=nome_cadastro()
    cpf = cpf_cadastro()
    for cliente in lista_atual:
        if cliente['cpf'] == cpf:
            print("Erro: CPF já cadastrado!")
            return
    email=email_cadastro()
    if None in (nome,cpf,email):
        print("Todos os dados devem ser preenchidos corretamente.")
        return
    novo_cadastro={'nome':nome, 'cpf': cpf, 'email': email}
    print("Cadastro realizado com sucesso!")
    return novo_cadastro
def ver_clientes(lista_para_exibir):
    if not lista_para_exibir:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n--- Clientes Cadastrados ---")
        for cliente in lista_para_exibir:
            print(f"Nome: {cliente['nome']} - CPF: {cliente['cpf']} - Email: {cliente['email']}")
def salvar_dados(lista_clientes):
    try:
        with open("config.json", "w", encoding='utf-8') as arquivo:
            json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
    return lista_clientes
def carregar_dados():
    try:
        with open ("config.json", 'r',) as arquivo:
            return json.load(arquivo)
    except:
        return []