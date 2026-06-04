# TÓPICO: 03 Operadores Logicos E Relacionais

# ==============================================================================
# ORIGINAL: Revisoes/revisao19.py
# ==============================================================================

'''
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               "a" == "a"
!=      diferente           "a" != "b"
'''
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

# ==============================================================================
# ORIGINAL: Revisoes/revisao5.py
# ==============================================================================

'''
Tipo de dado bool (boolean)
Ao questionar algo em ym programa,
só existem duas resposta possíveis:
sim (True) ou não (False).
Existem vários operadores para "questionar".
Dentre eles o ==, que é um operador lógico que
uestiona se um valor é igual a outro
'''
print(10 == 10)
print(10 == 11)
print(type(10 == 10))
print(type(10 == 11))

# ==============================================================================
# ORIGINAL: Revisoes/revisao7.py
# ==============================================================================

'''
Variáveis são usadas para salvar algo na memória do compitador.
PEP8: inici3e variáveis com letras minúsculas, pode usar
números e underline _.
O sinal de = é o operador ede atribuição. Ele é usado para
atribuir um valor a um nome (variável).
Uso: nome_variavel = expressão
'''
#nome_completo = 'Luiz Otávio Miranda'
#soma_dois_mais_dois = 2 + 2
#int_um= int('1')
#print(int_um, type(int('1')))
#print(nome_completo, soma_dois_mais_dois)
nome= 'Luiz'
idade = 18
maior_de_idade = idade >= 18
print(f'Nome:{nome} idade:{idade} é maior? {maior_de_idade}')

# ==============================================================================
# ORIGINAL: Revisoes/revisaoex1(8).py
# ==============================================================================

nome= 'Victoria'
sobrenome = 'Lucas'
idade = 18
ano_nascimento = 2025-idade
maior_de_idade = idade>=18
altura_metros = 1.59
print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Idade: {idade}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'É maior de idade? {maior_de_idade}')
print(f'Altura em metros: {altura_metros}')

