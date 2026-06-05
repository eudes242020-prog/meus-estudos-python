'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
qtd_linhas = 5
qtd_colunas = 5
linha = 1

while linha <= qtd_linhas:
    colunas= 1 
    while colunas <= qtd_colunas:
        print(f'{linha=} {colunas=}')
        colunas += 1
    linha += 1
    
print('Acabou')