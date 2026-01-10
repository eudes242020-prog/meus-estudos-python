import os
import time
filmes = {
    "Matrix": [],
    "Titanic": [],
    "Vingadores": [],
    "Coringa": []
}
menu={1: "Votar em um filme", 2: "Ver média de nota por filme", 3: "Ver qual filme tem maior média", 0: "Sair"}
def menu_principal(menu):
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")
def obter_escolha():
    try:
        escolha=int(input("Escolha uma opçao: "))
        if escolha >= 0 and escolha <= len(menu):
            return escolha
        print('Escolha invalida!')
        return None
    except ValueError:
        print("Escolha um número inteiro")
def voto_filme(filmes):
    print('Lista de filmes:')
    for filme in filmes:
        print(f'{filme}')
    filme = input('Informe o filme: ').strip().lower()
    for nome_filme in filmes:
        if nome_filme.lower() == filme:
            try:
                voto=float(input('Informe a nota do filme: '))
                if voto < 0 or voto > 10:
                    print("Notas somente possíveis de 0 a 10")
                    return
                filmes[nome_filme].append(voto)
                print("Voto registrado com sucesso!")
                return
            except ValueError:
                print("Escolha um número inteiro")
                return
    else:
        print('Filme nao esta na lista')
def ver_media_filme(filmes):
    print('Lista de filmes:')
    for filme in filmes:
        print(f'{filme}')
    escolha = input('Informe o filme: ').strip().lower()
    for filme in filmes:
        if filme.lower() == escolha:
            if len(filmes[filme])==0:
                print('Filme nao tem notas')
                return
            media=sum(filmes[filme])/len(filmes[filme])
            print(f"A nota media do filme {filme} é {media:.2f}")
            return
    print("Filme não encontrado")
def ver_media(filmes):
    medias={}
    for filme in filmes:
        if filmes[filme]:
            media=sum(filmes[filme])/len(filmes[filme])
            medias[filme]= media
    for nome, media in medias.items():
        print(f"{nome}: média {media:.2f}")
def maior_media(filmes):
    medias={}
    for filme in filmes:
        if filmes[filme]:
            media=sum(filmes[filme])/len(filmes[filme])
            medias[filme]= media
    if medias:
        melhor=max(medias, key=medias.get)
        print(f"O filme com a maior média é '{melhor}' com nota {medias[melhor]:.2f}")
    else:
        print("Nenhum filme possui notas ainda.")
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')
def executar_sistema():
    while True:
        menu_principal(menu)
        escolha=obter_escolha()
        if escolha is None:
            print('Erro de entrada')
            pausar_e_limpar()
            continue
        elif escolha ==0:
            print('Saindo do programa')
            break
        elif escolha ==1:
            voto_filme(filmes)
        elif escolha ==2:
            ver_media_filme(filmes)
        elif escolha ==3:
            maior_media(filmes)
        pausar_e_limpar()
executar_sistema()