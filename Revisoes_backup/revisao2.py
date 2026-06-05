import re
clientes = []
produtos = [{"id": 1, "nome": "Mouse", "preço": 49.90, "estoque": 10}]
# ---------- Funções de entrada ----------
def input_texto(msg):
    texto = input(msg).strip()
    return texto if texto else None
def input_numero(msg, positivo=False):
    try:
        num = float(input(msg))
        if positivo and num < 0:
            print("Digite apenas números positivos.")
            return None
        return num
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return None
# ---------- Cadastro de Cliente ---------- 
def nome_cadastro():
    return input_texto("Informe o nome: ")
def cpf_cadastro():
    cpf_sujo = input_texto("Informe seu CPF: ")
    if not cpf_sujo:
        return None
    cpf_limpo = ''.join(filter(str.isdigit, cpf_sujo))
    return cpf_limpo if len(cpf_limpo) == 11 else None
def validar_cpf(cpf):
    if cpf == cpf[0] * len(cpf):
        print("CPF inválido (sequência repetida).")
        return None
    def calcular_digito(digs, peso):
        total = sum(int(d) * p for d, p in zip(digs, range(peso, 1, -1)))
        digito = (total * 10) % 11
        return 0 if digito > 9 else digito
    n1 = calcular_digito(cpf[:9], 10)
    n2 = calcular_digito(cpf[:9] + str(n1), 11)
    return cpf if cpf.endswith(f"{n1}{n2}") else None
def email_cadastro():
    email = input_texto("Informe o e-mail: ")
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao, email):
        return email
    print("E-mail inválido.")
    return None
def cadastro_completo():
    nome = nome_cadastro()
    cpf = validar_cpf(cpf_cadastro())
    email = email_cadastro()
    if None in (nome, cpf, email):
        print("Todos os dados devem ser preenchidos corretamente.")
        return
    clientes.append({'nome': nome, 'cpf': cpf, 'email': email})
    print("Cliente cadastrado com sucesso!")
# ---------- Cadastro de Produto ----------
def nome_produto():
    return input_texto("Informe o nome do produto: ")
def codigo_produto():
    return 1 if not produtos else max(p['id'] for p in produtos) + 1
def preco_produto():
    return input_numero("Informe o valor do produto: ", positivo=True)
def quantidade_estoque():
    return int(input_numero("Informe a quantidade em estoque: ", positivo=True) or 0)
def ajuste_estoque(estoque_atual):
    try:
        escolha = int(input("Deseja: [1] Adicionar ou [0] Remover do estoque? "))
        qtd = int(input("Informe a quantidade: "))
        if qtd < 0:
            print("A quantidade não pode ser negativa.")
            return None
        if escolha == 1:
            return qtd
        elif escolha == 0:
            if estoque_atual - qtd < 0:
                print("Estoque não pode ficar negativo.")
                return None
            return -qtd
        else:
            print("Opção inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None
def cadastro_produto():
    nome = nome_produto()
    preco = preco_produto()
    id = codigo_produto()
    quantidade = quantidade_estoque()
    if None in (nome, preco, id, quantidade):
        print("Erro no preenchimento dos dados.")
        return
    for produto in produtos:
        if produto["nome"] == nome and produto["preço"] == preco:
            ajuste = ajuste_estoque(produto["estoque"])
            if ajuste is not None:
                produto["estoque"] += ajuste
            return
    produtos.append({"id": id, "nome": nome, "preço": preco, "estoque": quantidade})
    print("Produto cadastrado com sucesso!")