import time
import os
while True:
    os.system('cls')
    cpf_limpo = ''
    cpf_sujo =input('Informe seu cpf: ')
    for valor in cpf_sujo:
        if valor.isnumeric():
            cpf_limpo += valor
    if len(cpf_limpo) == 0:
        print('Você não digitou números.')
        time.sleep(2)
        continue
    primeiro_caractere = cpf_limpo[0]
    sequencia_repetida = primeiro_caractere * len(cpf_limpo)
    if cpf_limpo == sequencia_repetida:
        print('Você digitou dados sequenciais!')
        continue
    nove_digitos = cpf_limpo[:9] 
    contador_regressivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1-=1
    verificador_1 = (resultado_digito_1*10) % 11
    if verificador_1 >9:
        verificador_1 = 0
    dez_digitos = nove_digitos + str(verificador_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2+=int(digito) * contador_regressivo_2
        contador_regressivo_2-=1
    verificador_2 = (resultado_digito_2 *10) % 11
    if verificador_2 >9:
        verificador_2 = 0
    cpf_calculado = f'{nove_digitos}{verificador_1}{verificador_2}'
    if cpf_limpo == cpf_calculado:
        print(f'O CPF {cpf_sujo} é VÁLIDO ')
    else:
        print(f'O CPF {cpf_sujo} é INVÁLIDO ')
    sair=input('Deseja sair do programa: [s]im ou [n]ão: ').lower()
    if sair =='sim':
        print('Saindo do programa!')
        break
    