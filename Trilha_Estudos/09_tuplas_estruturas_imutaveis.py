# TÓPICO: 09 Tuplas Estruturas Imutaveis

# ==============================================================================
# ORIGINAL: Revisoes/revisao52.py
# ==============================================================================

'''
introdução ao desempacotamento + tuples(tuplas)
'''

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)

# ==============================================================================
# ORIGINAL: Revisoes/revisao53.py
# ==============================================================================

'''
tipo tupla - uma lista imutavel
'''
nomes = 'Maria', 'Helena', 'Luiz'
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes)

