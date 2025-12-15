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
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b #faz a concatenação das lista
lista_a.extend(lista_b) # junta as lista dentro da primeira colocando o valor da variavel na lista
