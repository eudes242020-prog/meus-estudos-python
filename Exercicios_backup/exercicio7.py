'''Desafio: O Contador de Letras "A" Quero que você escreva um código que:

    Tenha uma frase: frase = "O rato roeu a roupa do rei de Roma".

    Use um while para percorrer letra por letra (igual você fez agora).

    Dentro do while, use um if para ver se a letra atual é "r" (minúsculo) ou "R" (maiúsculo).

    Se for, aumente um contador (contador_r += 1).

    No final, mostre: "Achei X letras R".

Dica:

    Você vai precisar de um índice i = 0.

    Você vai precisar de um contador qtd_r = 0.

    Lembre-se: while i < len(frase):.'''

frase = "O rato roeu a roupa do rei de Roma"
frase_tamanho = len(frase)
i = 0
qtd_r = 0
while i < frase_tamanho:
    letra = frase[i]
    i += 1
    if letra in'rR':
        qtd_r += 1
print(f'Achei {qtd_r}')
        