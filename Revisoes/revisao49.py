'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido (primeiro argumente é onde vc quer inserir e o segundo é qual valor vc quer inserir)
    pop - Adiciona um item no índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i](CRUD)
'''
lista=[10, 20, 30, 40, 50, 60]
lista.append(90)
lista.insert(0, 100)
del lista[-1] #nesse caso funciona igual ao comando pop()

print(lista)