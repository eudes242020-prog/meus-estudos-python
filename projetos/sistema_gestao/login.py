from admin import validar_admin, validar_senha,criar_admin,validar_admin,codigo_admin
from produtos import pegar_string
from utils import pausa_e_limpar
from banco_dados import admins
def login_admin(lista):
    while True:
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
                    print("Senha Incorreta! Digite Novamente")
                    trava_senha=True
                    break
        if trava_senha:
            print('Senha Incorreta')
            pausa_e_limpar()
            continue
        print('Login não existe')
        pausa_e_limpar()