frase = 'O Python é uma linguagem de programação '\
    'multiparadiga. '\
    'Python foi criado por Guido van Rossum.'

recorde = 0
vencedora = ''

for letra in frase:
    if letra == ' ':
        continue
    qtd_atual = frase.count(letra)
    if qtd_atual > recorde:
        recorde = qtd_atual      
        vencedora = letra  
print(f'A letra "{vencedora}" venceu com {recorde} aparições.')