# TÓPICO: 16 List E Dict Comprehensions

# ==============================================================================
# ORIGINAL: Exercicios/exercicio25.py
# ==============================================================================

# TESTE DE MEMÓRIA: LISTA vs GERADOR
# Aprendizado do dia: Listas carregam tudo na RAM de uma vez.
# Geradores (usando parênteses) criam sob demanda (Lazy Evaluation).
#
# Ruim para memória pois útiliza uma quantidade muito alta (List Comprehension [])
# ainda não me aprofudei nesse assunto mais em breve voltaria para dizer que entendi tudo em 100%
# lista_pesada = [x for x in range(10000000)]

# 2. GERADOR (Usa parênteses ())
# O Python NÃO cria os números. Ele só guarda a "receita".
import sys
gerador = (n for n in range(1000000))
print(f"Tamanho do Gerador na RAM: {sys.getsizeof(gerador)} bytes")

# ==============================================================================
# ORIGINAL: Exercicios/exercicio56.py
# ==============================================================================

# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
l1=['Salvador', 'Ubatuba', 'Belo Horizonte']
l2=['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# def zipper(l1, l2):
#     intervalo_maximo = min
#     if len(l1) < len(l2):
#         intervalo_maximo = len(l1)
#     return [(l1[i], l2[i]) for i in range(intervalo_maximo)]
# print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ']))
# def zipper(l1,l2):
#     intervalo_maximo = min(len(l1), len(l2))
#     return[
#         (l1[i], l2[i]) for i in range(intervalo_maximo)
#     ]
print(list(zip(l1,l2)))

# ==============================================================================
# ORIGINAL: Exercicios/exercicio57.py
# ==============================================================================

# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.
# Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
lista = [x+y for x, y in zip(lista_a,lista_b)]
print(lista)

# ==============================================================================
# ORIGINAL: Revisoes/revisao73.py
# ==============================================================================

# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis
print(list(range(10)))

# ==============================================================================
# ORIGINAL: Revisoes/revisao75.py
# ==============================================================================

# Dictionary comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper
    if isinstance(valor,str) else valor
    for chave, valor 
    in produto.items()
    if chave == 'categoria'
}
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

print(dc)

