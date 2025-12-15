'''Desafio: O Espelho (Inverter a Palavra)
Esse é um clássico de entrevistas de emprego para iniciantes. Quero ver se você consegue usar a lógica do for, mas mudando a ordem das coisas.
O Objetivo: O usuário digita uma palavra e o programa mostra ela ao contrário.
Exemplo:
    Entrada: AMOR
    Saída: ROMA
A Dica de Ouro (Lógica): No exercício anterior, você fez nova_frase += letra (que é igual a nova_frase = nova_frase + letra). Ou seja: o novo entra no final da fila.
Para inverter, você precisa colocar a letra nova no começo da fila.

    A equação muda: nova_frase = letra + nova_frase

Tente implementar isso! Sem usar +=, usando a soma manual para controlar a ordem.'''
frase = input('Digite uma palavra: ')
nova_frase  =''
for letra in frase:
    nova_frase = letra + nova_frase
print(nova_frase)