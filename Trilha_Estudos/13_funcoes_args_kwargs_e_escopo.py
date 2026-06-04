# TÓPICO: 13 Funcoes Args Kwargs E Escopo

# ==============================================================================
# ORIGINAL: Exercicios/exercicio27.py
# ==============================================================================

# def multiplica(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total
# multiplicacao = multiplica(1,2 ,3 ,4 ,5 )
# print(multiplicacao)

def verificar(*args):
    lista = []
    for numero in args:
        if numero % 2 !=1:
            lista.append('Par')
        else:
            lista.append('Impar')
    return lista
par_impar = verificar(10, 11, 35, 102)
print(par_impar)

# ==============================================================================
# ORIGINAL: Revisoes/revisao61.py
# ==============================================================================

'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é nosso escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
'''
def escopo():
    x = 1
    print(x)
    #codigo dentro da função não pode ser usado fora do escopo
    #tem maneiras de dribla isso porem não é uma boa pratica
escopo()

# ==============================================================================
# ORIGINAL: Revisoes/revisao63.py
# ==============================================================================

'''
args - Argumentos não nomeaados
* - *args (empcotamento e desempacotamento)
'''
#Lembre-te de desempacotamento
def soma(*args):
    total = 0
    for numero in args:
        total+=numero
    return total
soma_total=soma(1,3,4,6,8)
print(soma_total)

# ==============================================================================
# ORIGINAL: Revisoes/revisao72.py
# ==============================================================================

# Empacotamento e desempacotamento de dicionários
a,b= 1,2
a,b = b,a
#print(a,b)
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2, b1, b2)
# args e kwargs
# args(ja vi)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
#mostro_argumentos_nomeados(nome='Eudes', sobrenome='Goncalves')
mostro_argumentos_nomeados(**pessoa_completa)

# ==============================================================================
# ORIGINAL: Revisoes/revisao87.py
# ==============================================================================

# Variáveis livre + nonlocal
# def fora(x):
#     a = x
#     def dentro():
#         return a
#     return dentro
# dentro = fora(10)
# dentro2 = fora(20)

# print(dentro())
# print(dentro2())
def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(string_a_concatenar):
        nonlocal valor_final
        valor_final += string_a_concatenar
        return valor_final
    return interna
c= concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

