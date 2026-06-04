# TÓPICO: 12 Funcoes Basicas E Retornos

# ==============================================================================
# ORIGINAL: Exercicios/exercicio26.py
# ==============================================================================

def verificar_par(a):
    if a % 2 != 1:
        return 'Par'
    return 'impar'
print(verificar_par(303))

# ==============================================================================
# ORIGINAL: Exercicios/exercicio28.py
# ==============================================================================

# 1. As ferramentas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y


def calcular(funcao, a, b):
    return funcao(a, b) 


print(calcular(somar, 10, 5))    # O python executa somar(10, 5) -> 15
print(calcular(subtrair, 10, 5)) # O python executa subtrair(10, 5) -> 5

# ==============================================================================
# ORIGINAL: Exercicios/exercicio29.py
# ==============================================================================

def equipar_arma(dano_base):
    def calcular(forca):
        return dano_base + forca
    return calcular
machado = equipar_arma(50)
espada = equipar_arma(10)
print(f'o dano do machado é {machado(60)}, e o dano da espada é {espada(70)}')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio55.py
# ==============================================================================

def soma(x,y):
    return x+y
def multiplica(x,y):
    return x*y
def cria_funcao(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna
soma_com_cinco = cria_funcao(soma, 5)
multiplica_por_dez = cria_funcao(multiplica, 10) 
print(soma_com_cinco(10))
print(multiplica_por_dez(10))

# ==============================================================================
# ORIGINAL: Revisoes/revisao58.py
# ==============================================================================

'''
introdução às funções (def) em Python
Funções são trechos de código usads para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
por padrão, funções Python retornam None(nada)
'''
# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')
    
# def imprimir(a, b, c):
#     print(a, b, c)
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')
saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

# ==============================================================================
# ORIGINAL: Revisoes/revisao59.py
# ==============================================================================

'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''
def soma(x, y):
    print(f'{x=} + {y=}', '|', 'x + y =', x+y)
soma(2,5)
soma(y=2, x=5)

# ==============================================================================
# ORIGINAL: Revisoes/revisao60.py
# ==============================================================================

'''
Valores padrão para parâmetros
Ao definir uma função. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
'''
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
    
soma(10, 2)
soma(9, 0 , 3)

# ==============================================================================
# ORIGINAL: Revisoes/revisao62.py
# ==============================================================================

'''
Retorno de valores das funções
'''
def soma(x, y):
    return x + y
soma1= soma(2,2)
soma2= soma(3,3)
print(soma1 + soma2)

# ==============================================================================
# ORIGINAL: Revisoes/revisao77.py
# ==============================================================================

# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0,10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0 
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))

# ==============================================================================
# ORIGINAL: Revisoes/revisao97.py
# ==============================================================================

# Funções recursivas e recursividade
# - funções que poedm se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base base que para a recursão
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim
    inicio+=1
    return recursiva(inicio,fim)
print(recursiva(0,1000))

