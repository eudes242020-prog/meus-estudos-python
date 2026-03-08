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