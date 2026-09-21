from admin import validar_senha,criar_admin,validar_admin
from produtos import pegar_string
from utils import pausa_e_limpar
from banco_dados import carregar_clientes
from cadastro_clientes import Cliente,nome_cadastro,cpf_cadastro,senha_cliente,validar_cpf,email_cadastro,cpf_cadastro,conferir_senha
def login_admin(lista):
    while True:
        logar=input("[1] Logar / [0] Voltar: ")
        if logar=="0":
            return False
        trava_senha=False
        login=validar_admin()
        for adm in lista:
            if adm.nome==login:
                senha=validar_senha()
                if conferir_senha(senha,adm.senha):
                    print('Acesso concedido!')
                    return True
                else:
                    trava_senha=True
                    break
        if trava_senha:
            print("Senha Incorreta! Digite Novamente")
            pausa_e_limpar()
            continue
        print('Login não existe')
        pausa_e_limpar()
def login_cliente():
    while True:
        logar=input("[1] Logar / [0] Voltar: ")
        if logar=="0":
            return None
        trava_senha=False
        clientes=carregar_clientes()
        cpf=cpf_cadastro()
        for cliente in clientes:
            if cliente.cpf==cpf:
                senha=senha_cliente()
                if conferir_senha(senha,cliente.senha):
                    print('Acesso concedido')
                    return cliente
                else:
                    trava_senha=True
                    break
        if trava_senha:
            print("Senha Incorreta! Digite Novamente")
            pausa_e_limpar()
            continue
        print('Login não existe')
        pausa_e_limpar()