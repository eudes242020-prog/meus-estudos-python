from produtos import pegar_string
from utils import pausa_e_limpar
from cadastro_clientes import hash_senha
class Admin:
    def __init__(self, nome, senha , id=None):
        self.id=id
        self.nome=nome
        self._senha=senha
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,nova):
        if len(nova) <= 5:
            print('Senha invalida')
            return 
        self._senha=nova
        print('Senha valida')
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
        if not admins:
            nome=validar_admin()
            senha=hash_senha(validar_senha())
            adm=Admin(nome=nome,senha=senha)
            admins.append(adm)
            return adm
        else:
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
            senha=hash_senha(validar_senha())
            adm=Admin(nome=nome,senha=senha)
            admins.append(adm)
            print('Admin criado com sucesso')
            return adm
