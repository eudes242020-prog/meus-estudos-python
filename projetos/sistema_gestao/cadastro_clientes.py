import json
from utils import pausa_e_limpar
from produtos import pegar_string, pegar_int, validar_nome
class Cliente:
    def __init__(self, nome, cpf, senha, email):
        self.nome = nome
        self.cpf = cpf
        self.senha=senha
        self.email=email

def nome_cadastro():
    while True:
        pausa_e_limpar()
        nome = pegar_string('Informe o nome: ').strip()
        if nome and len(nome) >= 2:
            return nome.capitalize()
        print("Nome inválido. Informe pelo menos 2 caracteres.")
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
def criar_senha():
    while True:
        senha=pegar_string("Informe a senha: ").strip()
        if len(senha) <=5:
            print("Senha tem que ter mais de 5 caracteres ")
            pausa_e_limpar()
            continue
        return senha
def cpf_cadastro():
    while True:
        pausa_e_limpar()
        cpf_limpo = ''
        cpf_sujo = pegar_string('Informe seu CPF: ')
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
        return None
def email_cadastro():
    while True:
        pausa_e_limpar()
        email=pegar_string('Informe o email: ').strip().lower()
        if email.count('@') != 1:
            print('Email inválido.')
            continue
        partes = email.split('@')
        if "." in partes[1] and partes[0]:
            return email
        print('Email inválido.')
def cadastro_completo(lista_atual):
    nome=nome_cadastro()
    cpf=cpf_cadastro()
    for cliente in lista_atual:
        if cliente.cpf == cpf:
            print("Erro: CPF já cadastrado!")
            return
    senha=criar_senha()
    email=email_cadastro()
    novo_cadastro=Cliente(nome=nome, cpf=cpf, senha=senha, email=email)
    print("Cadastro realizado com sucesso!")
    return novo_cadastro
def ver_clientes(lista_para_exibir):
    if not lista_para_exibir:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n--- Clientes Cadastrados ---")
        for cliente in lista_para_exibir:
            print(f"Nome: {cliente.nome} - CPF: {cliente.cpf} - Email: {cliente.email}")
def salvar_dados(lista_clientes):
    try:
        nova_lista=[]
        with open("config.json", "w", encoding='utf-8') as arquivo:
            for cliente in lista_clientes:
                clientes={"nome": cliente.nome, "cpf": cliente.cpf, "senha": cliente.senha, "email": cliente.email }
                nova_lista.append(clientes)
            json.dump(nova_lista, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
    return lista_clientes
def carregar_dados():
    try:
        nova_lista=[]
        with open ("config.json", 'r',) as arquivo:
            dados=json.load(arquivo)
        for cliente in dados:
            novo=Cliente(nome=cliente["nome"], cpf=cliente['cpf'], senha=cliente["senha"], email=cliente["email"])
            nova_lista.append(novo)
        return nova_lista
    except:
        return []