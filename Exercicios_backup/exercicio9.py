'''🛒 Desafio: O Caixa de Supermercado (Acumulador)

A missão é somar o valor de uma compra, mas você não sabe quantos produtos o cliente tem.

As Regras:

    Crie uma variável para guardar o total (começa com 0).

    Peça o preço do produto.

    O laço (while) deve rodar enquanto o preço for diferente de 0.

        (Digitou 0 = acabou a compra).

    Dentro do laço: Sone o preço ao total (+=) e peça o próximo preço.

    No final, mostre: "Total a pagar: R$ X".

Dica de Ouro: Use a lógica da "Leitura Antecipada" (pergunta um fora, pergunta o outro dentro do loop) para evitar somar o zero ou dar erro.

total_compra = 0
try:
    # CORREÇÃO 1: Converta para float JÁ NA ENTRADA
    produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
    
    # Agora 'produto' é um número (0.0). O while consegue comparar.
    while produto != 0:
        # CORREÇÃO 2: Não precisa converter aqui dentro, já convertemos lá fora.
        total_compra += produto
        
        # CORREÇÃO 3: Converta de novo aqui dentro para o loop testar na volta
        produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
        
    print(f'O total a pagar: R$ {total_compra:.2f}')
except ValueError:
    print('Erro: Coloque apenas números.')'''
total_compra = 0
try:
    produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
    while produto != 0:
        total_compra += produto
        produto = float(input('Qual preço do produto: caso deseje finalizar digite "0": '))
    print(f'O total a pagar: R$ {total_compra:.2f}')
except:
    print('Erro, Coloue novamente o valor do produto')