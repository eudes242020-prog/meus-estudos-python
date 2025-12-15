'''
Regras de Negócio (Requisitos):

    Peça ao usuário um Login e uma Senha.

    Validação do Login:

        Não pode conter espaços.

        Obrigatório começar com a letra 'a' (maiúscula ou minúscula).

        Se falhar, printe: "Erro: Login inválido (espaços ou inicial incorreta)".

    Validação da Senha:

        Use try/except para garantir que é um número inteiro.

        Precisa ter pelo menos 4 dígitos.

        Precisa ser ÍMPAR.

        Se falhar na conversão, printe: "Erro: A senha deve ser numérica".

        Se falhar nas regras (tamanho ou par/ímpar), printe: "Erro: Senha fraca (tamanho ou paridade)".

    Sucesso:

        Só exiba "Cadastro realizado com sucesso" se AMBOS (Login e Senha) passarem em todas as regras.'''

print('Realizando Cadastro!')
login = input('Informe um login: ')
senha = input('Informe uma senha: ')
tamanho = len(senha)
if login:
    validacao_login = ' ' not in login and (login[0] == 'a' or login[0] == 'A')
else:
    validacao_login = False
try:
    senha_int = int(senha)
    validacao_senha = tamanho >= 4 and senha_int % 2 != 0
    if validacao_login:
        if validacao_senha:
            print('Cadastro realizado com sucesso')
        else:
            print('Erro: Senha fraca (tamanho ou paridade)')
    else:
        print('Erro: Login inválido (espaços ou inicial incorreta)')
except:
        print('Erro: A senha deve ser númerica.')
