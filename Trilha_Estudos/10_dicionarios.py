# TÓPICO: 10 Dicionarios

# ==============================================================================
# ORIGINAL: Revisoes/revisao65.py
# ==============================================================================

# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
for chave in pessoa:
    print(chave, pessoa[chave])

# ==============================================================================
# ORIGINAL: Revisoes/revisao68.py
# ==============================================================================

'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}
# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.value())
# print(list(pessoa.items()))
# pessoa.setdefault('idade', 900)
#pessoa.copy() faz uma copia, porem se tiver listar dentro do dicionario ele vai copiar 100% nesse caso os valores vao ser iguais
# print(pessoa.get('nome'))
# nome=pessoa.pop('nome')
pessoa.update({
    'idade': 30,
    'local': 'Aracaju'
})
print(pessoa)

