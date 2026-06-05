votos={'Python': 3, 'JavaScript': 2, 'C#': 1, 'Java': 0}
def menu_linguagem():
    for i, linguagem in enumerate(votos,1):
        print(f"{i} {linguagem}")
def votar_linguagem():
    try:
        voto=int(input('Qual sua linguagem favorita: '))
        if 1 <= voto <= len(votos):
            return voto
        else:
            print("Opção fora do intervalo.")
    except ValueError:
        print("Digite um número válido!")
def validar_voto():
    opcoes = ['Python', 'JavaScript', 'C#', 'Java']
    indice = votar_linguagem()
    if indice is None:
        print('Voto não é valido')
        return
    validar= opcoes[indice-1]
    if validar:
        votos[validar]+=1
def contagem_votos():
    for linguagem, quantidade in votos.items():
        print(f"{linguagem}: {quantidade} votos")
def executa_sistema():
    while True:
        menu_linguagem()
        validar_voto()
        sair=input('Quer sair do sistema: ').lower()
        if sair=='s':
            print('saindo do programa')
            break
executa_sistema()
contagem_votos()