import json
from utils import pausa_e_limpar
from produtos import pegar_string, pegar_int, validar_nome
def validar_cpf(cpf):
    if not cpf:
        return None
    primeiro_caractere = cpf[0]
    sequencia_repetida = primeiro_caractere * len(cpf)
    if cpf == sequencia_repetida:
        return None
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
    return None
def verificar_nome(nome):
    trava=any( letra.isdigit() for letra in nome)
    if len(nome)> 2 and trava is False:
        return True
    return None
def nome_cadastro():
    while True:
        pausa_e_limpar()
        nome = pegar_string('Informe o nome: ').strip()
        if verificar_nome(nome):
            return nome.capitalize()
        print('Nome Invalido precisa ter mais que duas letras')
        pausa_e_limpar()
def verificar_email(email):
    if email.count('@') != 1:
        return None
    partes = email.split('@')
    if "." in partes[1] and partes[0]:
        return True
    return None
class Cliente:
    def __init__(self, nome, cpf, senha, email):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.email = email
    @property
    def nome(self):
        return self._nome      
    @property
    def senha(self):
        return self._senha
    @property
    def email(self):
        return self._email
    @property
    def cpf(self):
        return self._cpf
    @nome.setter
    def nome(self, checar):
        nome=verificar_nome(checar)
        if nome:
            self._nome=checar
            return
        self._nome=None
    @cpf.setter
    def cpf(self,checar):
        cpf_verificar=validar_cpf(checar)
        if cpf_verificar is not None:
            self._cpf=checar
            return
        self._cpf=None
    @email.setter
    def email(self,checar):
        email=verificar_email(checar)
        if email is not None:
            self._email=checar
            return
        self._email=None
    @senha.setter
    def senha(self,nova):
        senha=verificar_senha(nova)
        if senha:
            self._senha=nova
            return 
        self._senha=None
    def __str__(self):
        return f'LOGIN : {self.nome} CPF : {self.cpf} EMAIL : {self.email}'
def senha_cliente():
    while True:
        senha=pegar_string("Informe a senha: ").strip()
        verificar=verificar_senha(senha)
        if verificar:
            return senha
        print('Senha Invalida, precisa ter minimo de 6 caracteres')
        pausa_e_limpar()
def verificar_senha(senha):
        if len(senha) > 5:
            return True
        return None
def cpf_cadastro():
    while True:
        cpf_limpo = ''
        cpf_sujo = pegar_string('Informe seu CPF: ').strip()
        for numero in cpf_sujo:
            if numero.isdigit():
                cpf_limpo += numero
        cpf_limpo = cpf_limpo[:11] 
        validar=validar_cpf(cpf_limpo)
        if validar:
            return cpf_limpo
        print('CPF INVALIDO')
        pausa_e_limpar()
def email_cadastro():
    email=pegar_string('Informe o email: ').strip().lower()
    if verificar_email(email):
        return email
    print('Email Invalido')
    pausa_e_limpar()
def cadastro_completo(lista_atual):
    while True:
        invalido=False
        nome=nome_cadastro()
        cpf=cpf_cadastro()
        for cliente in lista_atual:
            if cliente.cpf == cpf:
                print("Erro: CPF já cadastrado!")
                return
        senha=senha_cliente()
        email=email_cadastro()
        novo_cadastro=Cliente(nome=nome, cpf=cpf, senha=senha, email=email)
        if novo_cadastro.nome is None or novo_cadastro.cpf is None or novo_cadastro.senha is None or novo_cadastro.email is None:
            invalido=True
        if novo_cadastro.nome is None:
            print("Nome invalido")
        if novo_cadastro.cpf is None:
            print("CPF invalido")
        if novo_cadastro.senha is None:
            print('Senha invalida')
        if novo_cadastro.email is None:
            print('Email invalido')
        if invalido:
            escolha=input('Deseja para de fazer o cadastro: [sim]/[não]')
            if escolha !='não':
                break
            continue
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