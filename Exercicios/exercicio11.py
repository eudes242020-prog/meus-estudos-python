'''🚀 Próximo Nível: Estatísticas (O if dentro do while)

Agora que você dominou Acumular (somar valor) e Contar (somar +1), vamos misturar as coisas.

O gerente gostou do sistema, mas agora ele quer uma estatística específica: "Quero saber quantos produtos custaram mais de R$ 1.000,00."

Desafio: Supermercado 3.0 (Estatísticas) Use o mesmo código que você acabou de fazer, mas adicione uma terceira variável (ex: qtd_mil).

    Toda vez que um produto passar, verifique:

        Se o preço for maior que 1000, aumente qtd_mil += 1.

    No final, mostre:

        Total da compra.

        Quantidade total de itens.

        Quantidade de itens que custam mais de R$ 1.000.

Dica: Você vai precisar colocar um if dentro do seu while.'''
acima_mil = 0
valor_total = 0
itens = 0
try:
    preco=float(input('Informe o valor do produto:R$ caso queira encerra digite "0": '))
    while preco != 0:
        valor_total += preco
        itens += 1
        if preco >= 1000:
            acima_mil += 1
        preco=float(input('Informe o valor do produto:R$ caso queira encerra digite "0": '))
        
    print(f'O valor total da compra é R$ {valor_total:.2f} e a quantidade de itens {itens} e valores acima de MIL {acima_mil}')
except:
    print('Erro, Coloue novamente o valor do produto')