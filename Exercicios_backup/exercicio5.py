'''
 Qualidade (Q): Peça ao usuário para digitar um número (que deve ser convertido para int) de 1 a 10.

    Tamanho (T): Peça ao usuário para digitar um número (que deve ser convertido para int) de 1 a 5.

    Especial (E): Peça ao usuário para digitar 'sim' ou 'não' (string).
2. Regras de Classificação (Lógica Condicional)
Use uma estrutura if/elif/else para classificar o produto em uma das quatro categorias, seguindo esta ordem de prioridade estrita:
A. Categoria PREMIUM (Prioridade Máxima)

    Condição: A Qualidade (Q) é maior ou igual a 9 E o produto é Especial (E) ('sim').

    Saída: Produto classificado como PREMIUM.

B. Categoria AVANÇADA

    Condição: A Qualidade (Q) é maior ou igual a 7 E o Tamanho (T) é maior ou igual a 4.

    Saída: Produto classificado como AVANÇADO.

C. Categoria PADRÃO

    Condição: A Qualidade (Q) está entre 5 e 6 (inclusive, ou seja, 5≤Q≤6) E o produto não é Especial (E) ('não').

    Saída: Produto classificado como PADRÃO.

D. Categoria BÁSICA (O que sobrar)

    Condição: Qualquer outro caso que não se encaixe nas categorias acima.

    Saída: Produto classificado como BÁSICO.'''
print('CLASSIFICAÇÃO DOS PRODUTOS!!')
qualidade = input('Informe a qualidade do produto de 1 a 10: ')
tamanho = input ('Informe o tamanho do produto de 1 a 5: ')
especial = input ('Informe se o produto é especial com "sim" ou "não": ')
qualidade_int = int(qualidade)
tamanho_int= int(tamanho)
if qualidade_int >= 9 and especial == 'sim':
    print('Produto classificado como PREMIUM.')
elif qualidade_int>=7 and tamanho_int >=4:
    print('Produto classificado como AVANÇADO.')
elif qualidade_int >=4 and qualidade_int <=6 and especial == 'não':
    print('Produto classificado como PADRÃO.')
else:
    print('Produto classificado como BÁSICO.')
