# TÓPICO: 20 Programacao Funcional Map Filter Reduce

# ==============================================================================
# ORIGINAL: Revisoes/revisao91.py
# ==============================================================================

# count é um iterador sem fim
from itertools import count
c1 = count()

# ==============================================================================
# ORIGINAL: Revisoes/revisao92.py
# ==============================================================================

# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product
def print_iter(iterator):
    print(*list(iterator), sep= '\n')
    print()
pessoas=[
    'João', 'Joana', 'Luiz', 'Letícia'
]
camisetas=[
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

# ==============================================================================
# ORIGINAL: Revisoes/revisao93.py
# ==============================================================================

# groupby - agrupando valores (itertools)
from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
def ordena(aluno):
    return aluno['nota']
alunos_agrupados= sorted(alunos, key=ordena)

grupos=groupby(alunos_agrupados, key=ordena)
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# ==============================================================================
# ORIGINAL: Revisoes/revisao94.py
# ==============================================================================

# map - para mapear dados
from functools import partial
def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
def aumentar_valor(valor, porcentagem):
    return round(valor*porcentagem, 2)
aumentar_dez_porcento= partial(
    aumentar_valor,
    porcentagem = 1.1
)
def muda_preco_de_produtos(produto):
    return {
        **produto, 'preco': aumentar_dez_porcento(produto['preco'])
    }
novos_produtos= map(muda_preco_de_produtos, produtos)
print_iter(produtos)
print_iter(novos_produtos)

# ==============================================================================
# ORIGINAL: Revisoes/revisao95.py
# ==============================================================================

# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# novos_produtos=[
#     p for p in produtos
#     if p['preco']> 10
# ]
novo_produtos=filter(
    lambda p: p['preco']>100,
    produtos
)
print_iter(produtos)
print_iter(novo_produtos)

# ==============================================================================
# ORIGINAL: Revisoes/revisao96.py
# ==============================================================================

# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
def funcao_do_reduce(acumulador, produto):
    
    return acumulador + produto['preco']
total= reduce(
    funcao_do_reduce,
    produtos,
    0
)
print(total)

