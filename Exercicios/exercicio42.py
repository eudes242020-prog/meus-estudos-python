import time
import os
import json
menu={
    1 :'Adicionar pessoa',
    2 :'Listar pessoas',
    0 :'Sair' 
}
def salvar_pessoas(lista_de_pessoas):
    with open("pessoas.json", "w") as arquivo:
        json.dump(lista_de_pessoas, arquivo, indent=4)
def ler_pessoas():
    try:
        with open("pessoas.json", "r") as arquivo:
            pessoas_lidas = json.load(arquivo)
            return pessoas_lidas
    except FileNotFoundError:
        return []
pessoas=ler_pessoas()
def mostrar_menu():
    for item in menu:
        print(f"[{item}] {menu[item]}")
def adicionar_pessoa(pessoas):
    nome=input('Nome da pessoa: ').capitalize()
    try:
        idade=int(input('Qual idade da pessoa: '))
        prof=input('Qual a profissão da pessoa: ').capitalize()
        nova_pessoa={'nome': nome, 'idade': idade, 'profissão': prof}
        print('Pessoa adicionada com sucesso!')
        pessoas.append(nova_pessoa)
        return True 
    except ValueError:
        print('Erro na idade')
def listar_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome:{pessoa['nome']} Idade:{pessoa['idade']} Profissão:{pessoa['profissão']}")
        print('-' * 30)
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')

def executar_sistema():
    while True:
        mostrar_menu()
        decisao=input('Oque deseja fazer: ')
        if decisao =='0':
            print('Saindo do programa')
            break
        elif decisao=='1':
            adicionar_pessoa(pessoas)
            salvar_pessoas(pessoas)
            pausar_e_limpar()
        elif decisao=='2':
            listar_pessoas(pessoas)
            pausar_e_limpar()
        else:
            print('Erro, escolha uma das opções do MENU!!')
            pausar_e_limpar()
executar_sistema()