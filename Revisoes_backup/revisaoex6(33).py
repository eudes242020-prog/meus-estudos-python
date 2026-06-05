'''
Faça um programa que pergunte a hora ao usuário e , baseando-se no horário
descrito, exiba saudação aproriada. Ex.
Bom dia 0-11, Boa tarde 12 - 17 e Boa noite 18-23
'''
try:
    hora = input('Informe com número inteiro a hora: ')
    hora_int = int(hora)
    manha = 0 <= hora_int <= 11
    tarde = 12<= hora_int <= 17
    noite = 18<= hora_int <= 23
    if manha:
        print('Bom dia!!')
    elif tarde:
        print('Boa tarde!!')
    elif noite:
        print('Boa noite!!')
    else:
        print('Horario invalido! Não existe essa hora')
except:
    print('Favor informe a hora em número inteiro')