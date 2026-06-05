frase =  'o rato roeu a roupa do rei de roma'
nova_frase=''
for letra in frase:
    if letra in 'aeiou':
        nova_frase += '*'
    else:
        nova_frase+=letra
print(nova_frase)