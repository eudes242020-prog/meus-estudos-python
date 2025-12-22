
 
def verificar_idade():
    try:
        idade=int(input('Informe sua idade: '))
        if idade >=18:
            return True
        else:
            return False
    except ValueError:
        return False
verifica_idade=verificar_idade()
if verifica_idade:
    print('Você é de maior!!')
else:
    print('Você não é de maior!!')
