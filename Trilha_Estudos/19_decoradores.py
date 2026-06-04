# TÓPICO: 19 Decoradores

# ==============================================================================
# ORIGINAL: Revisoes/revisao88.py
# ==============================================================================

# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradora são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
def inverte_string(string):
    return string[::-1]
def criar_funcao(funcao):
    def interna(*args, **kwargs): 
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        return resultado
    return interna
invertida = criar_funcao(inverte_string)
    
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro(23)
print(invertida)

# ==============================================================================
# ORIGINAL: Revisoes/revisao89.py
# ==============================================================================

# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradora são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são 'Syntax Sugar' (Açúcar sintatico)

def criar_funcao(funcao):
    def interna(*args, **kwargs): 
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        return resultado
    return interna
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
@criar_funcao
def inverte_string(string):
    return string[::-1]
invertida = inverte_string('123')
print(invertida)

# ==============================================================================
# ORIGINAL: Revisoes/revisao90.py
# ==============================================================================

# Decoradores com parâmetros
def decoradora(func):
    print('Decoradora 1')
    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora
def soma(x, y):
    print('Soma')
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

