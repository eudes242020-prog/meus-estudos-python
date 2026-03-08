# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
l1=['Salvador', 'Ubatuba', 'Belo Horizonte']
l2=['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# def zipper(l1, l2):
#     intervalo_maximo = min
#     if len(l1) < len(l2):
#         intervalo_maximo = len(l1)
#     return [(l1[i], l2[i]) for i in range(intervalo_maximo)]
# print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ']))
# def zipper(l1,l2):
#     intervalo_maximo = min(len(l1), len(l2))
#     return[
#         (l1[i], l2[i]) for i in range(intervalo_maximo)
#     ]
print(list(zip(l1,l2)))
