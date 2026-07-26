from admin import validar_admin, validar_senha,criar_admin,validar_admin,codigo_admin
from produtos import pegar_string
from utils import pausa_e_limpar
from banco_dados import admins
from cadastro_clientes import Cliente,carregar_dados,nome_cadastro,cpf_cadastro,senha_cliente,validar_cpf,email_cadastro,cpf_cadastro
def login_admin(lista):
    while True:
        logar=input("[1] Logar / [0] Voltar: ")
        if logar=="0":
            return False
        trava_senha=False
        if not lista:
            criar_admin(lista)
        login=validar_admin()
        for adm in lista:
            if adm.nome==login:
                senha=validar_senha()
                if adm.senha==senha:
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
            return False
        trava_senha=False
        clientes=carregar_dados()
        cpf=cpf_cadastro()
        for cliente in clientes:
            if cliente.cpf==cpf:
                senha=senha_cliente()
                if cliente.senha==senha:
                    print('Acesso concedido')
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
                   