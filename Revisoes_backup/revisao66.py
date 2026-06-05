#manipulando o dicionario
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
# for chave in pessoa:
    # print(chave, pessoa[chave])
chave = 'nome'

pessoas={}
pessoas[chave] = 'Eudes Goncalves'
del pessoa['sobrenome']
if pessoas.get('sobrenome') is None:
    print('Não existe')
    
print(pessoas)