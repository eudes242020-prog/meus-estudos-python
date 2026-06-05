# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em phon são mutáveis, porem aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set() #vazio
# s1 = {1, 2, 3, 3, 3, 3, 1} #com dados
# Sets são eficientes para remover valores duplicados
# de iteráveis.
#  - eles não tem índexes;
#  - eles não são ordenados;
#  - eles não são acessados via índice, mas via (for, i, in, in)
s1 = {1, 2, 3, 3, 3, 3, 1} #com dados

s1.add('Luiz')
s1.add(1)
s1.update('Olá mundo')

#  
# 
#  Métodos úteis:
#  add, update, clear, discard
# 
#  operadores úteis:
#  união | união (union) - Une
#  intersecção & (intersection) - Itens presentes em ambos
#  difença - Itens presentes apenas no set da esquerda
#  diferença simétrica ^ - Itens que não estão em ambos
#