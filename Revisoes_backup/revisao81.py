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