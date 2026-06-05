'''O Desafio: Contador de Vogais

Seu objetivo é criar um código que:

    Peça para o usuário digitar uma frase qualquer.

    Use um for para passar letra por letra.

    Conte quantas vogais (a, e, i, o, u) existem nessa frase.

    Mostre o total no final.

Dica de lógica: Você vai precisar de uma variável contador = 0. Dentro do for, você pergunta: if letra in 'aeiou': -> Se for verdade, contador += 1.'''
frase = input('Digite uma frase: ').lower()
contador = 0
for letra in frase:
    if letra in 'aeiou':
        contador += 1
print(f'A frase escrita tem {contador} vogais')