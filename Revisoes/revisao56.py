'''
split e join com list e str
split - divide uma string
join - une uma string
'''
frase =' olha so que, coisa interessante'
lista_frase = frase.split()

for i, frase in enumerate(lista_frase):
    lista_frase[i] = lista_frase[i].strip()
print(lista_frase)
p = 'Python'
frase_juntas = '*'.join(p)
print(frase_juntas)