# TÓPICO: 01 Variaveis E Tipos De Dados

# ==============================================================================
# ORIGINAL: Exercicios/exercicio34.py
# ==============================================================================



# ==============================================================================
# ORIGINAL: Exercicios/imc.py
# ==============================================================================



# ==============================================================================
# ORIGINAL: Revisoes/revisao14.py
# ==============================================================================

a = 'A'
b = 'B'
c = 1.1
string= 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)

# ==============================================================================
# ORIGINAL: Revisoes/revisao33.py
# ==============================================================================

'''
Imutáveis que vimas: str, int, float, bool
'''
string = 'luiz Otávio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.zfill(30))

# ==============================================================================
# ORIGINAL: Revisoes/revisao98.py
# ==============================================================================

# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv . env

