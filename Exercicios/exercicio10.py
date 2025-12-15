'''Você já fez o código que soma os preços. Agora, o gerente do mercado pediu uma atualização no sistema: além do valor total, ele quer saber quantos itens o cliente comprou no total.

Suas Missões:

    Pegue a lógica do exercício anterior (acumulador de preço).

    Adicione um Contador: uma nova variável que conte +1 cada vez que um produto passa.

    Saída Final: O programa deve mostrar o Total (R$) e a Quantidade de Itens.

Dica de Lógica:

    Você vai precisar de duas variáveis nascendo fora do while: uma para o dinheiro (total_compra) e uma para a quantidade (qtd_itens).'''
valor_total = 0
qtd_itens = 0
try:
    preco = float(input('Qual valor do item R$: caso queira encerra compra digite "0": '))
    while preco != 0:
        valor_total += preco
        qtd_itens += 1
        preco = float(input('Qual valor do item R$: caso queira encerra compra digite "0": '))
    print(f'O valor total da compra é R$ {valor_total:.2f} e a quantidade de itens {qtd_itens}')
except:
    print('Erro, Coloue novamente o valor do produto')
