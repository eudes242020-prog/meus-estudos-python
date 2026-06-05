# Módulos padrao do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# import sys

# partes - from nome_modulo import objeto1, objeto2 
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

# from sys import exit, platform

# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# from sys import exit as ex, platform as pf
# print(pf)
# ex()

# má prática - from nome_modulo import *
# Vantagens: import tudo de um módulo
# Desvantagens: Importa tudo de um módulo

# from sys import *
# print(platform)
