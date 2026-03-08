# Generator expression, Iterables e Iterators em Python
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
generator= (n for n in range(10000000))
print(sys.getsizeof(generator))
for n in generator:
    print(n)
