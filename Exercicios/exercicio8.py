''' Vamos manter o while, mas agora aumentar a pressão.

Regras:

    A senha é '1234'.

    O usuário tem apenas 3 tentativas.

    Use um contador (variável, ex: tentativas = 0) para controlar isso.

    O while deve continuar rodando enquanto a senha estiver errada E (and) o número de tentativas for menor que 3.

    Se acertar, imprima "Acesso permitido".

    Se gastar as 3 tentativas e errar, imprima "Conta bloqueada".

Dica: Você vai precisar incrementar o contador (tentativas = tentativas + 1 ou += 1) dentro do loop.'''
senha_secreta = '1234'
senha = input('Digite sua senha: ')
tentativa = 0
while senha_secreta != senha and tentativa < 2:
    tentativa+=1
    print('Senha incorreta! Tente novamente!')
    senha = input('Digite sua senha: ')
if senha == senha_secreta:
    print('Acesso permitido!')
elif tentativa <= 3:
    print('Conta Bloqueada')
