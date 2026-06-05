# 1. As ferramentas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y


def calcular(funcao, a, b):
    return funcao(a, b) 


print(calcular(somar, 10, 5))    # O python executa somar(10, 5) -> 15
print(calcular(subtrair, 10, 5)) # O python executa subtrair(10, 5) -> 5