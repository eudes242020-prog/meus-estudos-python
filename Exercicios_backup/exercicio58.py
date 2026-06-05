"""Sem olhar nada, escreve uma função que recebe uma lista de palavras e retorna apenas as palavras que têm mais de 5 letras"""
nomes = ["Ana", "Roberto", "Bia", "Guilherme", "Max", "Fernanda", "João", "Valentina", "Caio", "Alexandre", "Lucas", "Lara"]

def maior_que_cinco(lista):
    nova = []
    for nome in lista:
            if len(nome.replace(' ','')) >=5:
                nova.append(nome)
    return nova
nova=maior_que_cinco(nomes)
print(nova)