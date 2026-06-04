# TÓPICO: 05 Condicionais If Elif Else

# ==============================================================================
# ORIGINAL: Exercicios/correcao.py
# ==============================================================================

print('Calculo de formação de triângulos!!')
reta1 = input('Informe o comprimento da primeira reta: ')
reta2 = input('Informe o comprimento da segunda reta: ')
reta3 = input('Informe o comprimento da terceira reta: ')
reta1_float=float(reta1)
reta2_float=float(reta2)
reta3_float=float(reta3)
pode_formar = (reta1_float + reta2_float > reta3_float) and (reta2_float + reta3_float > reta1_float) and (reta3_float + reta1_float > reta2_float)
equi= reta1_float == reta2_float == reta3_float
if pode_formar:
    if equi:
        print('Equilátero: Todos os lados são iguais')
    elif reta1_float == reta2_float or reta1_float == reta3_float or reta2_float == reta3_float:
        print('Isósceles: Apenas dois lados são iguais.')
    else:
        print('Escaleno: Todos os lados são diferentes.')
else:
    print('Os fatores não formam um triângulo.')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio24.py
# ==============================================================================

'''
 Desafio: O Banco dos Centavos

Imagine que você tem uma conta e depositou R$ 0.10 três vezes seguidas. A lógica diz: 0.10 + 0.10 + 0.10 = 0.30.

Sua missão: Crie um código que faça essa soma de duas formas e compare:

    Modo "Ingênuo" (Float): Some 0.1 três vezes e peça para o Python verificar se o resultado é igual (==) a 0.3.

    Modo "Profissional" (Decimal): Importe o módulo decimal, use a classe Decimal para somar os três valores e verifique se bate com o Decimal('0.3').'''
import decimal
soma_i = 0.1
soma1 = '0.1'
decimal1 = decimal.Decimal(soma1)
soma_p = decimal1 + decimal1 + decimal1
print(soma_i + soma_i + soma_i)
print(soma_p)
if soma_p == decimal.Decimal('0.3'):
    print('Sim')
else:
    print('Não')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio4.py
# ==============================================================================

'''Exercício 3: Cálculo de Média Final com Bônus

Crie um programa que calcule a média ponderada de um aluno e decida sua aprovação, incorporando um fator bônus.

    Colete via input() as notas de três provas (P1, P2, P3).

    Colete um valor de "Bônus" que será somado à nota final (pode ser 0).

    Garanta que todas as entradas sejam tratadas como números de ponto flutuante (float).

    Calcule a Média Ponderada das três provas com os seguintes pesos:
    Média=10(P1x2)+(P2 x 3)+(P3 x 5)

    Calcule a Nota Final somando a Média ao Bônus.

    Use a lógica condicional para determinar o status do aluno (use if/elif/else):

        Se a Nota Final for maior ou igual a 7.0: APROVADO com nota {Nota Final}.

        Se a Nota Final for maior ou igual a 5.0 e menor que 7.0: RECUPERAÇÃO com nota {Nota Final}.

        Se a Nota Final for menor que 5.0: REPROVADO com nota {Nota Final}.

    Use f-strings para exibir a Nota Final com duas casas decimais.'''
nota1 = input('Informe sua primeira nota: ')
nota2 = input('Informe sua segunda nota: ')
nota3 = input('Informe sua Terceira nota: ')
nota1_float=float(nota1)
nota2_float=float(nota2)
nota3_float=float(nota3)
media = ((nota1_float*2)+ (nota2_float * 3)+ (nota3_float * 5)) / 10
b = input('Tem ponto por trabalho? "sim" ou "não" ')
if b == 'sim':
    valor = input('Informe sua pontuação bonus: ')
    valor_float = float(valor)
    media_final= valor_float + media
    if media_final >=7:
        print(f'APROVADO com nota {media_final}')
    elif media_final >=5 and media_final <7:
        print(f'RECUPERAÇÃO com nota {media_final}')
    elif media_final <5:
        print(f'REPROVADO com nota final {media_final}')
if b == 'não':
    if media >=7:
        print(f'APROVADO com nota {media}')
    elif media >=5 and media <7:
        print(f'RECUPERAÇÃO com nota {media}')
    elif media <5:
        print(f'REPROVADO com nota {media}')
else:
        print('Necessario responder "sim" ou "não"')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio5.py
# ==============================================================================

'''
 Qualidade (Q): Peça ao usuário para digitar um número (que deve ser convertido para int) de 1 a 10.

    Tamanho (T): Peça ao usuário para digitar um número (que deve ser convertido para int) de 1 a 5.

    Especial (E): Peça ao usuário para digitar 'sim' ou 'não' (string).
2. Regras de Classificação (Lógica Condicional)
Use uma estrutura if/elif/else para classificar o produto em uma das quatro categorias, seguindo esta ordem de prioridade estrita:
A. Categoria PREMIUM (Prioridade Máxima)

    Condição: A Qualidade (Q) é maior ou igual a 9 E o produto é Especial (E) ('sim').

    Saída: Produto classificado como PREMIUM.

B. Categoria AVANÇADA

    Condição: A Qualidade (Q) é maior ou igual a 7 E o Tamanho (T) é maior ou igual a 4.

    Saída: Produto classificado como AVANÇADO.

C. Categoria PADRÃO

    Condição: A Qualidade (Q) está entre 5 e 6 (inclusive, ou seja, 5≤Q≤6) E o produto não é Especial (E) ('não').

    Saída: Produto classificado como PADRÃO.

D. Categoria BÁSICA (O que sobrar)

    Condição: Qualquer outro caso que não se encaixe nas categorias acima.

    Saída: Produto classificado como BÁSICO.'''
print('CLASSIFICAÇÃO DOS PRODUTOS!!')
qualidade = input('Informe a qualidade do produto de 1 a 10: ')
tamanho = input ('Informe o tamanho do produto de 1 a 5: ')
especial = input ('Informe se o produto é especial com "sim" ou "não": ')
qualidade_int = int(qualidade)
tamanho_int= int(tamanho)
if qualidade_int >= 9 and especial == 'sim':
    print('Produto classificado como PREMIUM.')
elif qualidade_int>=7 and tamanho_int >=4:
    print('Produto classificado como AVANÇADO.')
elif qualidade_int >=4 and qualidade_int <=6 and especial == 'não':
    print('Produto classificado como PADRÃO.')
else:
    print('Produto classificado como BÁSICO.')

# ==============================================================================
# ORIGINAL: Revisoes/revisao17.py
# ==============================================================================

'''
if / elif       /else
se / se não se  / se não
'''
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')
print('Fora do if')

# ==============================================================================
# ORIGINAL: Revisoes/revisao18.py
# ==============================================================================

'''
if / elif       /else
se / se não se  / se não
'''
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')
print('Fora do if')

# ==============================================================================
# ORIGINAL: Revisoes/revisao21.py
# ==============================================================================

'''
Operadores lógicos
and (e) or (ou) not(não)
and - Todas as condições precisam ser
verdadeiras.
se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
São considerados falsy (que vc já viu)
0 0.0 '' False
Tambem existe o tipo None que é
usado para representar um não valor
'''
#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')
#senha_permitida = '123456'

#if entrada=='E' and senha_digitada == senha_permitida:
#    print('Entrar')

#elif entrada=='S':
#    print('Sair')
print(True and False and True)
print(bool(''))

# ==============================================================================
# ORIGINAL: Revisoes/revisao22.py
# ==============================================================================

'''
Operadores lógicos
and (e) or (ou) not(não)
or - Qualquer condição verdadeira avalia
toda a expressão como verdadeira.
Se qiaçqier vaçpr fpr cpmsoderadp verdadeiro,
a expressão inteira será avaliada naquele valor.
São considerados falsy (que vc já viu)
0 0.0 "" False
Também existe o tipo None que é
usado para representar um não valor
'''
#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')
#senha_permitida = '123456'

#if (entrada=='E' or entrada == 'e') and senha_digitada == senha_permitida:
#    print('Entrar')

#elif entrada=='S':
#    print('Sair')
senha = input('Senha: ') or 'Sem senha'
print(senha)

# ==============================================================================
# ORIGINAL: Revisoes/revisao23.py
# ==============================================================================

'''
Operador lógico "not"
Usado para inverter expressões
not True = False
not False = True
'''
senha = input('Senha: ')
if not senha:
    print('Senha incorreta.')

# ==============================================================================
# ORIGINAL: Revisoes/revisao24.py
# ==============================================================================

'''
Operadores in e not in
Strings são iteráveis
 0 1 2 3 4 5
 O t á v i o
-6-5-4-3-2-1
'''
nome = 'Otávio'
#print(nome[2])
#print(nome[-4])
#print('vio' in nome)
#print('zero' in nome)
#print('-'*10)
#print('vio' not in nome)
#print('zero' not in nome)
nome = input ('Digite seu nome: ')
encontra = input ('Digite o qque deseja encontrar: ')
if encontra in nome:
    print(f'{encontra} está em {nome}')
else:
    print(f'{encontra} não está em {nome}')

# ==============================================================================
# ORIGINAL: Revisoes/revisao30.py
# ==============================================================================

'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade(ruim)
'''
velocidade = 61
local_carro = 100

RADAR_1 = 60 #velocidade máxima o radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega
velocidade_passou_radar_1 = velocidade > RADAR_1
carro_multao =local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <=(LOCAL_1 + RADAR_RANGE)

if velocidade_passou_radar_1:
    print('Velocidade carro passou o radar 1')
if  carro_multao and velocidade_passou_radar_1:
    print('Carro multado em radar 1')

# ==============================================================================
# ORIGINAL: Revisoes/revisao31.py
# ==============================================================================

'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identiade
'''
#v1 = 'a'
#v2 = 'b'
#print(id(v1))
#print(id(v2))



condicao = True
passou_no_if = None

if condicao:
   passou_no_if = True
   print('Faça algo')
else:
   print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if , passou_no_if is not None)

# ==============================================================================
# ORIGINAL: Revisoes/revisao78.py
# ==============================================================================

# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe')
    print(getattr(string, metodo)())
else:
    print('Não existe método', metodo)

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex3(20).py
# ==============================================================================

primeiro_valor = input('Digite um valor: ')
segundo_valor = input ('Digite outro valor: ')
if primeiro_valor>segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif segundo_valor>primeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
else:
    print(f'Os valores do primeiro valor {primeiro_valor} e segundo valor {segundo_valor} são iguais!')

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex4(28).py
# ==============================================================================

'''
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
se nome e idade forem digitados
exiba
seu nome ...
seu nome invertido é ...
seu nome contém (ou não) espaços
Seu nome conte {n} letras
A primeira letra do seu nome é ...
A última letra do seu nome é ...
se nada for digitado em nome ou idade 
exiba
"Desculpe, você deixou campos vazios."
'''
nome = input ('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_limpo = nome.strip()
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome) - nome.count(" ")}')
    print(f'A primeira letra do seu nome é {nome_limpo[0]}')
    print(f'A última letra do seu nome é {nome_limpo[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex7(34).py
# ==============================================================================

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letra, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande"
'''

nome = input ('Escreva seu primeiro nome: ')
quantidade_letras = len(nome)
nome_curto = quantidade_letras <= 4
nome_normal = 5 <= quantidade_letras <= 6

if nome_curto:
    print('Seu nome é curto!')
elif nome_normal:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')

