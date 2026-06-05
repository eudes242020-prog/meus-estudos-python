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


