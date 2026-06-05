'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor da memória (mutável)
'''
lista_a = ['Eudes', 'Victoria']
lista_b = lista_a
lista_a[0] = 'Outra coisa'
print(lista_b)