from produtos import pegar_string
from banco_dados import admins
from utils import pausa_e_limpar
class Admin:
    def __init__(self, id, nome, senha):
        self.id=id
        self.nome=nome
        self.senha=senha
    def __str__(self):
        return f'ID ADMIN: {self.id} ADMIN: {self.nome}'
def validar_admin():
    while True:
        admin=pegar_string("Qual nome do ADMIN: ").strip()
        if len(admin)<=3:
            print("Precisa ter mais de 3 caracteres")
            pausa_e_limpar()
            continue
        return admin
def codigo_admin():
    if not admins:
        id=1
        return id
    else:
        ids = [item.id for item in admins]
        return max(ids)+1
def validar_senha():
    while True:
        admin=pegar_string("Qual senha: ").strip()
        if len(admin) <=5:
            print("Precisa ter mais de 5 caracteres")
            pausa_e_limpar()
            continue
        return admin
def criar_admin(admins):
    while True:
        trava=False
        nome=validar_admin()
        for valor in admins:
            if valor.nome == nome:
                print("Já existe um ADMIN com esse nome escolha outro!!")
                pausa_e_limpar()
                trava=True
                break
        if trava:
            continue
        id=codigo_admin()
        senha=validar_senha()
        adm=Admin(id=id,nome=nome,senha=senha)
        admins.append(adm)
        print('Admin criado com sucesso')
        return adm
    