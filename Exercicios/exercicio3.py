'''Exercício 2: Validador de Senha Simples

Crie um sistema de login simples que use a lógica booleana e operadores relacionais para validar credenciais.

    Defina duas variáveis fixas (no código, não use input()):

        USUARIO_CORRETO = 'admin'

        SENHA_CORRETA = '123456'

    Use a função input() para pedir ao usuário que digite o nome de usuário e a senha.

    Use um único if para verificar se ambas as credenciais digitadas pelo usuário correspondem às credenciais corretas.
   
     A saída deve ser:

        Se correto: Login bem-sucedido. Bem-vindo!

         Se incorreto: Acesso negado. Usuário ou senha incorretos.'''
usuario_correto = 'admin'
senha_correta = '123456'
usuario = input('Digite o nome do usúario: ')
senha = input('Digite a senha: ')
if usuario == usuario_correto and senha == senha_correta:
    print('Login bem-sucedido. Bem-vindo!')
else:
    print('Acesso negado. Usúario ou senha incorretos.')