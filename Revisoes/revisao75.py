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