print('Calculo de formação de triângulos!!')
reta1 = input('Informe o comprimento da primeira reta: ')
reta2 = input('Informe o comprimento da segunda reta: ')
reta3 = input('Informe o comprimento da terceira reta: ')
reta1_float=float(reta1)
reta2_float=float(reta2)
reta3_float=float(reta3)
pode_formar = (reta1_float + reta2_float > reta3_float) and (reta2_float + reta3_float > reta1_float) and (reta3_float + reta1_float > reta2_float)
equi= reta1_float == reta2_float == reta3_float
if pode_formar:
    if equi:
        print('Equilátero: Todos os lados são iguais')
    elif reta1_float == reta2_float or reta1_float == reta3_float or reta2_float == reta3_float:
        print('Isósceles: Apenas dois lados são iguais.')
    else:
        print('Escaleno: Todos os lados são diferentes.')
else:
    print('Os fatores não formam um triângulo.')

