# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.
# Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
lista = [x+y for x, y in zip(lista_a,lista_b)]
print(lista)