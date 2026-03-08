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