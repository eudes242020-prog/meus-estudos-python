# TÓPICO: 17 Geradores E Iteradores

# ==============================================================================
# ORIGINAL: Revisoes/revisao45.py
# ==============================================================================

'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
nex -> me entregye o próximo valor
iter -> me entregue seu iteraor
'''
texto = iter('Luiz')

# ==============================================================================
# ORIGINAL: Revisoes/revisao79.py
# ==============================================================================

# Generator expression, Iterables e Iterators em Python
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
generator= (n for n in range(10000000))
print(sys.getsizeof(generator))
for n in generator:
    print(n)

# ==============================================================================
# ORIGINAL: Revisoes/revisao80.py
# ==============================================================================

#Introdução às Generator functions em Python
#generator = (n for n in range(100000))
def generator(n=0, maximum=10):
    while True:
        yield n
        n+=1
        if n == maximum:
            return
        
gen = generator()
for n in gen:
    print(n)

# ==============================================================================
# ORIGINAL: Revisoes/revisao81.py
# ==============================================================================

# Yield from
def g1():
    yield 1
    yield 2
    yield 3
def g2():
    yield 4
    yield from g1()
    yield 5
    yield 6
    yield 7

g = g2()
for n in g:
    print(n)

