# Funções recursivas e recursividade
# - funções que poedm se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base base que para a recursão
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim
    inicio+=1
    return recursiva(inicio,fim)
print(recursiva(0,1000))