# Exemplo mental:
# Entrada: "T3nho 2 Gatos"
# Saída esperada: "32"
frase = input('Digite algo: ')
nova_frase = ''
for letra in frase:
    if letra.isdigit():
        nova_frase += letra
print(nova_frase)