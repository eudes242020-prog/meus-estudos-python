import re
clientes = []
produtos = []
def nome_cadastro():
    nome=input('Informe o nome: ').strip().capitalize()
    if nome:
        return nome
    return None
def cpf_cadastro():
    cpf_limpo=''
    cpf_sujo=input('Informe seu cpf: ')
    for numero in cpf_sujo:
        if numero.isdigit():
            cpf_limpo+=numero
    if len(cpf_limpo)==11:
        return cpf_limpo
    return None
def validar_cpf(cpf):
    primeiro_caractere = cpf[0]
    sequencia_repetida = primeiro_caractere * len(cpf)
    if cpf == sequencia_repetida:
        print('Você digitou dados iguais, CPF invalido!')
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
        return cpf
    return None
def email_cadastro():
    email=input('Informe o email: ').strip().lower()
    padrao = r'^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return email
    print('Email inválido.')
    return None
def cadastro_completo(nome, cpf, email):
    nome=nome_cadastro()
    cpf = cpf_cadastro()
    cpf = validar_cpf(cpf)
    email=email_cadastro()
    if None in (nome,cpf,email):
        print("Todos os dados devem ser preenchidos corretamente.")
        return
    novo_cadastro={'nome':nome, 'cpf': cpf, 'email': email}
    clientes.append(novo_cadastro)
    print("Cadastro realizado com sucesso!")