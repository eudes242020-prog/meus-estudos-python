# TÓPICO: 21 Miniprojetos E Sistemas

# ==============================================================================
# ORIGINAL: Exercicios/exercicio.py
# ==============================================================================

import time
import os
def pedido_usuario():
    try:
        print('Caso queira sair do programa digita 0')
        numero=int(input('Vamos ver se o número é IMPAR ou PAR: '))
        return numero
    except ValueError:
        return None
def executar_sistema():
    while True:
        numero=pedido_usuario()
        if numero is None:
            print('Erro de entrada!')
            time.sleep(2)
            os.system('cls')
        elif numero == 0:
            print('Saindo do programa!')
            break
        else:
            if numero %2==0:
                print(f'O número {numero} é PAR!')
            else:
                print(f'O número é {numero} IMPAR')
        time.sleep(2)
        os.system('cls')
executar_sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio1.py
# ==============================================================================

'''
Exercício 1: Calculadora Simples de IMC (Reforço e Conversão)

O objetivo é recriar o cálculo do IMC, mas garantindo que todos os conceitos de tipos de dados e operadores estejam claros.

    Coleta de Dados: Use a função input() para pedir ao usuário:

        O peso (em kg).

        A altura (em metros).

    Tratamento/Conversão: Como input() retorna strings, converta o peso e a altura para o tipo de dado float (número decimal).

    Saída de Dados: Imprima o resultado usando uma f-string para exibir o peso e altura que o usuário digitou, e o resultado do IMC com apenas duas casas decimais de precisão.

Exemplo de Saída Esperada:

    Se o usuário digitar 80 e 1.75, a saída deve ser: Para o peso 80.0kg e altura 1.75m, o IMC calculado é 26.12.'''
# print('Calculadora IMC!')
# peso = input('Informe seu peso: ')
# altura = input('Informe sua altura: ')
# peso_float = float(peso)
# altura_float=float(altura)
# imc=peso_float / altura_float**2
# print(f'Para o peso {peso_float:.1f}kg e altura {altura_float:.2f}m, o IMC calculado é {imc:.2f}')
'''Solicite a idade do usuário.
Exiba uma mensagem informando se ele é maior ou menor de idade (18 anos como referência).'''
import time
import os
def solicitacao():
    try:
        print('Caso queira sair do programa digita 0')
        idade=int(input('Informe sua idade: '))
        return idade
    except ValueError:
        return None
def verificar_idade(idade):
    if idade is None:
        return'Erro de entrada'
    if idade==0:
        return 'Saindo do programa'
    if idade>=18:
        return "Você é maior de idade"
    else:
        return "Você é menor de idade"
    
def sistema():
    while True:
        idade=solicitacao()
        mensagem = verificar_idade(idade)
        print(mensagem)
        if mensagem=='Saindo do programa':
            break
        time.sleep(2)
        os.system('cls')
sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio10.py
# ==============================================================================

'''Você já fez o código que soma os preços. Agora, o gerente do mercado pediu uma atualização no sistema: além do valor total, ele quer saber quantos itens o cliente comprou no total.

Suas Missões:

    Pegue a lógica do exercício anterior (acumulador de preço).

    Adicione um Contador: uma nova variável que conte +1 cada vez que um produto passa.

    Saída Final: O programa deve mostrar o Total (R$) e a Quantidade de Itens.

Dica de Lógica:

    Você vai precisar de duas variáveis nascendo fora do while: uma para o dinheiro (total_compra) e uma para a quantidade (qtd_itens).'''
valor_total = 0
qtd_itens = 0
try:
    preco = float(input('Qual valor do item R$: caso queira encerra compra digite "0": '))
    while preco != 0:
        valor_total += preco
        qtd_itens += 1
        preco = float(input('Qual valor do item R$: caso queira encerra compra digite "0": '))
    print(f'O valor total da compra é R$ {valor_total:.2f} e a quantidade de itens {qtd_itens}')
except:
    print('Erro, Coloue novamente o valor do produto')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio11.py
# ==============================================================================

'''🚀 Próximo Nível: Estatísticas (O if dentro do while)

Agora que você dominou Acumular (somar valor) e Contar (somar +1), vamos misturar as coisas.

O gerente gostou do sistema, mas agora ele quer uma estatística específica: "Quero saber quantos produtos custaram mais de R$ 1.000,00."

Desafio: Supermercado 3.0 (Estatísticas) Use o mesmo código que você acabou de fazer, mas adicione uma terceira variável (ex: qtd_mil).

    Toda vez que um produto passar, verifique:

        Se o preço for maior que 1000, aumente qtd_mil += 1.

    No final, mostre:

        Total da compra.

        Quantidade total de itens.

        Quantidade de itens que custam mais de R$ 1.000.

Dica: Você vai precisar colocar um if dentro do seu while.'''
acima_mil = 0
valor_total = 0
itens = 0
try:
    preco=float(input('Informe o valor do produto:R$ caso queira encerra digite "0": '))
    while preco != 0:
        valor_total += preco
        itens += 1
        if preco >= 1000:
            acima_mil += 1
        preco=float(input('Informe o valor do produto:R$ caso queira encerra digite "0": '))
        
    print(f'O valor total da compra é R$ {valor_total:.2f} e a quantidade de itens {itens} e valores acima de MIL {acima_mil}')
except:
    print('Erro, Coloue novamente o valor do produto')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio12.py
# ==============================================================================

'''🏦 Próximo Desafio: O Menu Bancário (Backend Puro)

Já que seu foco é ser Backend Developer, nada melhor que simular a lógica de um caixa eletrônico. Aqui, o while não vai depender de um preço, mas sim da vontade do usuário de continuar no sistema.

Cenário: Você tem um saldo inicial de R$ 0.00. O programa deve mostrar um menu com opções e realizar operações até a pessoa decidir sair.

As Regras:

    Crie uma variável saldo começando com 0.

    Crie uma variável opcao (pode começar com algo diferente da opção de saída).

    O menu deve ter:

        1: Consultar Saldo (Mostra o saldo atual).

        2: Depositar (Pede um valor e soma ao saldo).

        3: Sacar (Pede um valor e subtrai do saldo).

        4: Sair (Encerra o loop).

    O while deve rodar enquanto a opção for diferente de 4.

Dica de Lógica: Dessa vez, você vai pedir a opcao dentro do loop (ou usar a leitura antecipada se preferir, mas em menus geralmente mostramos as opções repetidamente dentro do loop).
'''
saldo = 0
try:
    opcao = float(input('[1] Consultar Saldo: \n[2] Depositar: \n[3] Sacar: \n[4] Sair: \nQual opção: '))
    while opcao!= 4:
        if opcao == 1:
            print(f'Seu saldo atual é R$ {saldo:.2f}')
        elif opcao ==2:
            valor = float(input('Informe o valor: '))
            saldo += valor
        elif opcao ==3:
            valor = float(input('Informe o valor: '))
            if valor > saldo:
                print('Saldo Insuficiente!')
            else:
                print('Saque realizado')
                saldo -= valor
        else:
            print('Erro, Pricisa digitar a opção correta')
        opcao = float(input('[1] Consultar Saldo: \n[2] Depositar: \n[3] Sacar: \n[4] Sair: \nQual opção: '))
    print('Finalizando o sistema!')
except:
    print('ERRO: Digite as opções corretamente')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio14.py
# ==============================================================================

total_caixa = 0

print('--- CINE PYTHON ---')

try:
    filme = int(input('Escolha: [1] Avatar [2] Titanic [0] Sair: '))


    while filme != 0: 
        if filme == 1:
            preco = 30.00
        elif filme == 2:
            preco = 25.00

        else:
            print('Opção Inválida! Escolha 1 ou 2.')          
            filme = int(input('Escolha: [1] Avatar [2] Titanic [0] Sair: '))
            continue
        qtd = int(input('Quantos ingressos? '))
        subtotal = preco * qtd
        total_caixa += subtotal
        print(f'Venda registrada: R$ {subtotal}')
        filme = int(input('Escolha: [1] Avatar [2] Titanic [0] Sair: '))
    print(f'Total do dia: R$ {total_caixa}')
except:
    print('Erro!!')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio3.py
# ==============================================================================

'''Exercício 2: Validador de Senha Simples

Crie um sistema de login simples que use a lógica booleana e operadores relacionais para validar credenciais.

    Defina duas variáveis fixas (no código, não use input()):

        USUARIO_CORRETO = 'admin'

        SENHA_CORRETA = '123456'

    Use a função input() para pedir ao usuário que digite o nome de usuário e a senha.

    Use um único if para verificar se ambas as credenciais digitadas pelo usuário correspondem às credenciais corretas.
   
     A saída deve ser:

        Se correto: Login bem-sucedido. Bem-vindo!

         Se incorreto: Acesso negado. Usuário ou senha incorretos.'''
# usuario_correto = 'admin'
# senha_correta = '123456'
# usuario = input('Digite o nome do usúario: ')
# senha = input('Digite a senha: ')
# if usuario == usuario_correto and senha == senha_correta:
#     print('Login bem-sucedido. Bem-vindo!')
# else:
#     print('Acesso negado. Usúario ou senha incorretos.')
'''Crie um programa que imprima os números pares de 1 a 20'''
# for numero in range(1,21):
#     if numero %2==0:
#         print(numero)
# try:
#     n1=int(input('Digite um número: '))
#     for item in range(1,11):
#         print(n1*item)
# except ValueError:
#     print('digite um número inteiro')

# for nome in range(6):
#     print('Treinando')
'''Crie uma lista vazia chamada frutas

Peça ao usuário para digitar 3 frutas (com input())

Adicione cada fruta à lista usando append()

Ao final, mostre a lista completa com print()'''
frutas=[]
def adicionar_3_fruta():
    for fruta in range(3):
        fruta=input('Informe uma fruta: ')
        frutas.append(fruta)
    print(frutas)
adicionar_3_fruta()
def remover_fruta():
    try:
        fruta=input('Informe uma fruta pra retira: ').lower()
        frutas.remove(fruta)
        print(frutas)
    except ValueError:
        print('Essa fruta não existe na lista')
remover_fruta()
def remover_todas_frutas():
    fruta=input('Deseja remover todas as frutas: [s]im ou [n]ão')
    if fruta in 's':
        frutas.clear()
        print(frutas)
'''Peça ao usuário para digitar o nome de uma fruta a ser removida da lista

Use remove() para tentar excluir

Se a fruta não estiver na lista, mostre uma mensagem de erro

Ao final, exiba a lista atualizada'''

# ==============================================================================
# ORIGINAL: Exercicios/exercicio39.py
# ==============================================================================

import time
import os

menu=['Ver todas as tarefas','Adicionar nova tarefa', 'Remover tarefa']
    
tarefas=[]
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')
def menu_princinpal():
    print('=== MENU DO SISTEMA ===')
    for item, opcao in enumerate(menu,start=1):
        print(f'[{item}] {opcao}')
    print('[0] Sair')
def mostrar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada')
        return False
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'[{i}] {tarefa}')
        return True
def adicionar_tarefa():
    tarefa=input('Qual tarefa deseja adicionar: ').strip()
    tarefas.append(tarefa)
    return True 
def remover_tarefa():
    if not tarefas:
            return False
    mostrar_tarefas()
    try:
        escolha=int(input('Escolha uma tarefa: '))
        if 1<= escolha <=len(tarefas):
            tarefas.pop(escolha-1)
            return True
        else:
            return False
    except ValueError:
        return False
while True:
    menu_princinpal()
    try:
        decisao=int(input('Oque deseja fazer: '))
        if decisao==0:
            print('Saindo do programa!!')
            break
        elif decisao==1:
            if not tarefas:
                print('Não existe tarefa para listar!!')
                pausar_e_limpar()
                continue
            else:
                mostrar_tarefas()
        elif decisao==2:
            ok = adicionar_tarefa()
            if ok:
                print('Tarefa adicionada com sucesso!')
            else:
                print('Nenhuma tarefa foi adicionada.')
        elif decisao==3:
            remover=remover_tarefa()
            if remover:
                print('Tarefa foi removida com sucesso!')
            else:
                print('Nenhuma tarefa foi removida.')
        else:
            print('Opção inválida!!')
            pausar_e_limpar()
        pausar_e_limpar()
    except ValueError:
        print('Somente números inteiros permitidos!!!')
        pausar_e_limpar()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio40.py
# ==============================================================================

import os
import time
tarefas = [
    {"nome": "Estudar", "feito": False},
    {"nome": "Trabalhar", "feito": False},
]
menu=["Ver tarefas", 'Marcar tarefa como concluída', 'Desmarcar tarefa como concluída', ]
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')
def menu_principal():
    print('------------')
    for item, tarefa in enumerate(menu, start=1):
        print(f'[{item}] {tarefa}')
    print('[0] Para sair')

def executar_menu():
    menu_principal()
    try:
        numero=int(input('Qual opção deseja: '))
        if numero==0:
            return 'sair'
        if 1<= numero <=len(menu):
            if numero==1:
                mostrar_tarefa()
            elif numero==2:
                status = marcar_tarefa()
                mensagem=mensagem_status(status)
                return mensagem
            elif numero==3:
                status = desmarcar_tarefa()
                mensagem = mensagem_status(status)
                return mensagem
            else:
                return 'erro'
    except ValueError:
        return 'erro'       
def desmarcar_tarefa():
    if not tarefas:
        return 'vazio'
    mostrar_tarefa()
    try:
        escolha=int(input('Qual tarefa deseja desmarcar como concluida: '))
        if 1<=escolha<=len(tarefas):
            tarefas[escolha-1]['feito']=False
            return 'ok'
        return 'erro'
    except ValueError:
        return 'erro'
def mostrar_tarefa():
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["feito"] else "❌"
        print(f'{i} {tarefa['nome']} {status}')

def marcar_tarefa():
    if not tarefas: #primeiro verificar se a lista está vazia, se estiver dar o returno e polpa codigo
            return 'vazio'
    mostrar_tarefa() #mostra lista de tarefas numerada
    try:  #tratativa de errro
        escolha=int(input('Qual tarefa deseja marcar como concluida: '))#pede ao usuario para coloca a tarefa concluida
        if 1<=escolha<=len(tarefas):#verificador da escolha do usuario pra ver se esta no "range"
            tarefas[escolha-1]['feito'] = True #transforma a escolha do cliente en verdadeira, com isso mostrando que concluio
            return 'ok'#mostra que foi feito tudo ok com todo programa
        return 'erro'#como nao passo pelo if está fora do range e n é possivel fazer a escolha da tarefa
    except ValueError:
        return 'erro'#erro tratado
def mensagem_status(status):
    if status=='ok': return 'Sucesso!'
    if status=='vazio': return 'Lista vazia'
    if status=='erro': return 'Opção inválida / digite um número'
while True:
    verificar=executar_menu()
    if  verificar=='sair':
        print('Saindo')
        break
    if verificar:
        print(verificar)
    pausar_e_limpar()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio41.py
# ==============================================================================

def mostrar_menu(menu):
    print('------------')
    for i, item in enumerate(menu, 1):
        print(f'[{i}] {item}')
    print('[0] Para sair')

def mostrar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, 1):
        status = "✔" if tarefa["feito"] else "❌"
        print(f'{i}. {tarefa["nome"]} {status}')

def alterar_status_tarefa(tarefas, status_desejado):
    if not tarefas:
        raise ValueError("Lista de tarefas vazia")
    mostrar_tarefas(tarefas)
    try:
        escolha = int(input("Escolha uma tarefa: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["feito"] = status_desejado
        else:
            raise IndexError("Índice fora do intervalo")
    except ValueError:
        raise ValueError("Entrada inválida, digite um número")

def executar_programa():
    tarefas = [
        {"nome": "Estudar", "feito": False},
        {"nome": "Trabalhar", "feito": False},
    ]
    menu = ["Ver tarefas", "Marcar como concluída", "Desmarcar como concluída"]
    while True:
        mostrar_menu(menu)
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 0:
                print("Saindo...")
                break
            elif opcao == 1:
                mostrar_tarefas(tarefas)
            elif opcao == 2:
                alterar_status_tarefa(tarefas, True)
            elif opcao == 3:
                alterar_status_tarefa(tarefas, False)
            else:
                print("Opção inválida")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    executar_programa()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio42.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio44.py
# ==============================================================================

pessoas =[{'nome': 'Carlos', 'idade': 35, 'profissao': 'Médico'},]
def cadastra_pessoa():
    print('Para seguir com cadastro Porfavor forneça as informções!')
    nome=input('Informe o nome: ')
    try:
        idade=int(input('Informe a idade: '))
        profi=input('Informe a profissão: ')
        nova_pessoa={'nome': nome, 'idade': idade, 'profissao': profi}
        pessoas.append(nova_pessoa)
    except ValueError:
        print('A idade precisa ser um número inteiro!!')

def filtro_pessoas():
    profi=input('Qual profissão deseja filtrar: ').strip().lower()
    encontrado = False
    for pessoa in pessoas:
        if pessoa['profissao'].lower() == profi:
            print(f"{pessoa['nome']} {pessoa['idade']}")
            encontrado = True
    if not encontrado:
        print('Nenhuma pessoa com essa profissão foi encontrada.')

# ==============================================================================
# ORIGINAL: Exercicios/exercicio45.py
# ==============================================================================

menu=['Adicionar aluno em uma turma','Listar todos os alunos de uma turma','Listar todas as turmas existentes']
turmas = {
    "A": [{"nome": "Carlos", "idade": 15}, {"nome": "Ana", "idade": 14}],
    "B": [{"nome": "João", "idade": 13}]
}
def obter_opcao_menu():
    print('----MENU----')
    for i, opcao in enumerate(menu,1):
        print(f"[{i}] {opcao}")
    print('[0] Para sair do programa aperto')
    try:
        numero=int(input('Oque deseja: '))
        if 0<= numero<=len(menu):
            return numero
        return None
    except ValueError:
        return None
def adicionar_aluno():
    turma=input('Deseja adicionar o aluno em que turma: [A] ou [B]: ').upper()
    if turma not in turmas:
        return None
    nome=input('Informe o nome do aluno: ').capitalize()
    try:
        idade=int(input('Informe a idade do aluno: '))
        novo_aluno={"nome": nome, "idade": idade}
        turmas[turma].append(novo_aluno)
    except:
        return None
def listar_turma_especifica():
    turma=input('Deseja listar os alunos em que turma: [A] ou [B]: ').upper()
    if turma not in turmas:
        return None
    for aluno in turmas[turma]:
        print(f'Nome do aluno {aluno["nome"]} idade {aluno["idade"]}')
def listar_todas():
    for turma in turmas:
        for aluno in turmas[turma]:
            print(f'Nome do aluno {aluno["nome"]} tem {aluno["idade"]} anos')
def executar_sistema():
    while True:
        decisao=obter_opcao_menu()
        if decisao is None:
            print('Erro de entrada')
        if decisao ==0:
            print('Saindo do programa!')
            break
        elif decisao == 1:
            adicionar_aluno()
        elif decisao==2:
            listar_turma_especifica()
        else:
            listar_todas()
executar_sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio46.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio47.py
# ==============================================================================

produtos = [
    {"nome": "arroz", "preço": 3.50, "categoria": "mercado"},
    {"nome": "feijão", "preço": 5.20, "categoria": "mercado"},
    {"nome": "sabão", "preço": 2.00, "categoria": "limpeza"},
    {"nome": "detergente", "preço": 1.50, "categoria": "limpeza"},
    {"nome": "leite", "preço": 4.00, "categoria": "mercado"},
]
menu={1: "Cadastrar", 2: "Listar", 3: "Filtrar", 4: 'Qtd por Categoria', 0: "Sair"}
def menu_principal():
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")
def decisao_usuario():
    try:
        escolha=int(input('Qual opção deseja: '))
        if 0<= escolha<= len(menu):
            return escolha
        return None
    except ValueError:
        return None
def cadastrar_produto(listar_produtos):
    produto=input('Informe o nome do produto: ')
    try:
        preco=float(input('Informe o valor do produto: '))
        categoria=input('Informe a categoria: ')
        novo_produto={"nome": produto, "preço": preco, "categoria": categoria}
        listar_produtos.append(novo_produto)

    except ValueError:
        print('Erro de entrada!!')
def listar_produtos(lista_produtos):
    for produto in lista_produtos:
        print(f"O produto {produto['nome']} preço R${produto['preço']:.2f} categoria {produto['categoria']}")
def filtro_preço():
    try:
        if not produtos:
            return None
        valor=float(input('Gostaria de ver os itens com valor superior a R$: '))
        nova_lista=[]
        for produto in produtos:
            if produto['preço']>valor:
                nova_lista+=[produto]
        for produto in nova_lista:
            print(f"O produto {produto['nome']} preço R${produto['preço']:.2f} categoria {produto['categoria']}")
    except ValueError:
        print('Favor que o número inteiro')
def produto_categoria(produtos):
    categoria={}
    for produto in produtos:
        if produto['categoria'] in categoria:
            categoria[produto['categoria']]+=1
        else:
            categoria[produto['categoria']] = 1  
    for nome_categoria, quantidade in categoria.items():
        print(f"{nome_categoria}: {quantidade}")   
        
def executa_sistema():
    while True:
        menu_principal()
        decisao=decisao_usuario()
        if decisao is None:
            print('Erro de entrada!!')
            continue
        if decisao== 0:
            print('Saindo do programa!')
            break
        elif decisao==1:
            cadastrar_produto(produtos)
        elif decisao ==2:
            listar_produtos(produtos)
        elif decisao== 3:
            filtro_preço()
        elif decisao ==4:
            produto_categoria(produtos)
executa_sistema()
'''
Implemente a função para adicionar produtos.    

Implemente a função para listar todos.

Implemente a função para filtrar produtos com preço acima de X valor.
'''

# ==============================================================================
# ORIGINAL: Exercicios/exercicio48.py
# ==============================================================================

livros = [{
    "título": "",
    "autor": "",
    "gênero": ""}]
menu={1: "Cadastrar livros", 2: "Listar livros", 3: "Filtrar por gênero", 4: 'Qtd por autor', 0: "Sair"}
def menu_principal(menu):
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")
def decisao_usuario(menu):
    try:
        decisao=int(input("Informe oque deseja: "))
        if 0<= decisao<=len(menu):
            return decisao
        return None
    except ValueError:
        return None
def cadastra_livro(livros):
    titulo=input('Informe o título do livro: ')
    autor=input('Informe o autor do livro: ')
    genero=input('Informe o gênero do livro: ')
    novo_livro={"título": titulo, "autor": autor, "gênero": genero}
    if livros[0]['título'] =='' and livros[0]['autor']=='' and livros[0]['gênero']=='':
        livros[0] = novo_livro
    else:
        livros.append(novo_livro)
def listar_livros(livros):
    for livro in livros:
        print(f"Título:{livro['título']} Autor:{livro['autor']} Gênero{livro['gênero']}")
def buscar_genero(livros):
    busca=input('Qual gênero deseja buscar: ')
    nova_lista=[]
    for livro in livros:
        if livro['gênero'].lower() == busca.lower():
            nova_lista.append(livro)
    if not nova_lista:
        print("Nenhum livro encontrado para esse gênero.")
    for livro in nova_lista:
        print(f"Título: {livro['título']} | Autor: {livro['autor']} | Gênero: {livro['gênero']}")
def quantidade_autor(livros):
    lista_autor={}
    for livro in livros:
        if livro['autor'] in lista_autor:
            lista_autor[livro['autor']]+=1
        else:
            lista_autor[livro['autor']] = 1 
    for autor, quantidade in lista_autor.items():
        print(f'{autor}: {quantidade}')
def executar_sistema():
    while True:
        menu_principal(menu)
        decisao=decisao_usuario(menu)
        if decisao is None:
            print('Erro de entrada')
            continue
        elif decisao ==0:
            print("Saindo do programa!!")
            break
        elif decisao==1:
            cadastra_livro(livros)
        elif decisao ==2:
            listar_livros(livros)
        elif decisao==3:
            buscar_genero(livros)
        elif decisao==4:
            quantidade_autor(livros)
executar_sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio49.py
# ==============================================================================

livros = []

menu = {1:'Cadastrar livros', 2: 'Listar livros', 0: 'Sair'}

def menu_principal():
    for chave,valor in menu.items():
        print(f"[{chave}] {valor}")

def decisao_usuario():
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha >= 0 and escolha <= len(menu):
            return escolha
        print('Opção inválida!!')
    except ValueError:
        return None
def cadastrar_livro():
    titulo = input("Informe o nome do livro: ")
    autor = input("Informe o nome do autor: ")
    genero = input("Informe o gênero do livro: ")
    if not titulo or not autor or not genero:
        print("Todos os campos devem ser preenchidos.")
        return
    novo_livro = {'título':titulo, 'autor':autor, 'gênero': genero}
    livros.append(novo_livro)

def listar_livros():
    if livros == []:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"Título: {livro['título']} | Autor: {livro['autor']} | Gênero: {livro['gênero']}")

def executar_sistema():
    while True:
        menu_principal()
        decisao = decisao_usuario()
        if decisao == 0:
            print("Saindo...")
            break
        elif decisao == 1:
            cadastrar_livro()
        elif decisao == 2:
            listar_livros()
        else:
            print("Opção inválida.")

executar_sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio50.py
# ==============================================================================

filmes = {
    "Ação": [],
    "Drama": [],
    "Comédia": []
}

menu = {
    1: "Cadastrar filme",
    2: "Listar filmes por gênero",
    0: "Sair"
}

def menu_principal():
    for chave, valor in menu.items():
        print(f"[{chave}] {valor}")

def decisao_usuario():
    try:
        return int(input("Escolha uma opção: "))
    except:
        return None

def cadastrar_filme():
    genero = input("Informe o gênero (Ação, Drama, Comédia): ").capitalize()
    if genero not in filmes:
        print("Gênero inválido.")
        return
    titulo = input("Informe o título do filme: ").capitalize()
    filmes[genero] = titulo
    print("Filme cadastrado com sucesso!")

def listar_filmes_por_genero():
    genero = input("Qual gênero deseja listar? ").capitalize()
    if genero in filmes:
        if not filmes[genero]:
            print("Nenhum filme cadastrado nesse gênero.")
        else:
            for titulo in filmes[genero]:
                print(f"- {titulo}")
    else:
        print("Gênero inválido.")

def executar_sistema():
    while True:
        menu_principal()
        escolha = decisao_usuario()
        if escolha == 0:
            print("Saindo...")
            break
        elif escolha == 1:
            cadastrar_filme()
        elif escolha == 2:
            listar_filmes_por_genero()
        else:
            print("Opção inválida!")

executar_sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio51.py
# ==============================================================================

alunos=[]
def cadastrar_aluno(alunos):
    print('Cadastro de aluno!')
    aluno=input('Informe o nome do aluno: ').strip().capitalize()
    novo_aluno={"nome": aluno, "notas": []}
    alunos.append(novo_aluno)
def adicionar_nota(alunos):
    print('Adicionando nota para o aluno')
    aluno=input('Informe o aluno que deseja adiciona uma nota: ').strip().capitalize()
    encontrado = False
    try:
        nota=float(input('Informe a nota do aluno: '))
        if nota < 0 or nota > 10:
            print("Notas somente possíveis de 0 a 10")
            return
    except ValueError:
        print('Nota precisa ser um número') 
        return    
    for nome in alunos:
        if nome['nome'] == aluno:
            encontrado = True
            nome['notas'].append(nota) 
    if not encontrado:
        print("Aluno não cadastrado")
def media_aluno(alunos):
    aluno=input('Informe o nome do aluno: ')
    encontrado = False
    for nome in alunos:
        if aluno == nome['nome']:
            encontrado = True
        if len(nome['notas'])==0:
            print('Aluno não possui nota')
            return
        media=sum(nome['notas'])/len(nome['notas'])   
        print(f"A media do aluno é {media}")
        break
    if encontrado==False:
        print('Aluno não encontrado')
def aprovaos_reprovados(alunos):
    aprovados=[]
    reprovados=[]
    
    for aluno in alunos:
        if len(aluno['notas'])==0:
            continue
        media=sum(aluno['notas'])/len(aluno['notas'])
        aluno_com_media = aluno.copy()
        aluno_com_media['media'] = media
        if media >=7:
            aprovados.append(aluno_com_media)
        else:
            reprovados.append(aluno_com_media)
    print("\n--- Alunos Aprovados ---")
    for aprovado in aprovados:
        print(f"Nome do aluno:{aprovado['nome']} | média {aprovado['media']:.2f}")
    print("\n--- Alunos Reprovados ---")
    for reprovado in reprovados:
        print(f"Nome do aluno {reprovado['nome']} | média {reprovado['media']:.2f}")

# ==============================================================================
# ORIGINAL: Exercicios/exercicio52.py
# ==============================================================================

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

# ==============================================================================
# ORIGINAL: Exercicios/exercicio53.py
# ==============================================================================

import time
import os
menu={1: "Cadastrar funcionário", 2: "Listar funcionários", 3: "Buscar funcionário por cargo", 4: "Ver salário médio por cargo", 0: "Sair"}
funcionarios=[]
def opcoes_menu(menu):
    for chave,opcao in menu.items():
        print(f'[{chave}] {opcao}')
def escolha_usuario():
    try:
        escolha=int(input('Escolha uma opção: '))
        if 0<=escolha<=len(menu):
            return escolha
        return None
    except ValueError:
        return None
def nome_funcionario():
    nome=input('Informe o nome do funcionario: ').strip().lower()
    if nome:
        return nome
    return None
def cargo_funcionario():
    cargo=input('Informe o cargo do funcionario: ').strip().lower()
    if cargo:
        return cargo
    return None
def salario_funcionario():
    try:
        salario=float(input('Informe o salario do salário do funcionario: '))
        if salario <0:
            return None
        return salario
    except ValueError:
        return None
def cadastro_funcionario(nome, cargo, salario):
    novo_funcionario={"nome": nome, "cargo": cargo, 'salario': salario}
    funcionarios.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso!")
def listar_funcionario(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    for funcionario in funcionarios:
        print(f"Nome do funcionario {funcionario['nome']} função {funcionario['cargo']}")
def buscar_cargo(funcionarios):
    lista_nova=[]
    cargo=input('Informe o cargo que gostaria de pesquisa: ').strip().lower()
    if not cargo:
        print('Precisa preencher a informação necessaria')
    for funcionario in funcionarios:
        if funcionario['cargo'] == cargo:
            lista_nova.append(funcionario)
    if not lista_nova:
        print('Nenhum funcionário encontrado com esse cargo.')
    else:
        for pessoa in lista_nova:
            print(f'{pessoa['nome']} | {pessoa['cargo']}')
def media_salario_cargo(funcionarios):
    salarios=[]
    cargo=input('Informe o cargo que gostaria de pesquisa: ').strip().lower()
    for pessoa in funcionarios:
        if pessoa['cargo']== cargo:
            salarios.append(pessoa['salario'])
    if salarios:
        media=sum(salarios)/len(salarios)
        print(f'A media salarial do cargo {cargo} é de {media:.2f}')
    else:
        print('Nenhum funcionário encontrado com esse cargo.')
def pausar_e_limpar():
    time.sleep(2)
    os.system('cls')        
def executar_sistema():
    while True:
        opcoes_menu(menu)
        decisao=escolha_usuario()
        if decisao is None:
            print('Erro de entrada!')
            pausar_e_limpar()
            continue
        if decisao==0:
            print('Saindo do programa!')
            break
        if decisao==1:
            nome=nome_funcionario()
            salario=salario_funcionario()
            cargo=cargo_funcionario()
            if nome is None or salario is None or cargo is None:
                print('Erro de entrada: todos os campos devem ser preenchidos corretamente.')
                pausar_e_limpar()
                continue
            cadastro_funcionario(nome, cargo, salario)    
        elif decisao==2:
            listar_funcionario(funcionarios)
        elif decisao==3:
            buscar_cargo(funcionarios)
        elif decisao==4:
            media_salario_cargo(funcionarios)
        pausar_e_limpar()
executar_sistema()

# ==============================================================================
# ORIGINAL: Exercicios/exercicio6.py
# ==============================================================================

'''
Regras de Negócio (Requisitos):

    Peça ao usuário um Login e uma Senha.

    Validação do Login:

        Não pode conter espaços.

        Obrigatório começar com a letra 'a' (maiúscula ou minúscula).

        Se falhar, printe: "Erro: Login inválido (espaços ou inicial incorreta)".

    Validação da Senha:

        Use try/except para garantir que é um número inteiro.

        Precisa ter pelo menos 4 dígitos.

        Precisa ser ÍMPAR.

        Se falhar na conversão, printe: "Erro: A senha deve ser numérica".

        Se falhar nas regras (tamanho ou par/ímpar), printe: "Erro: Senha fraca (tamanho ou paridade)".

    Sucesso:

        Só exiba "Cadastro realizado com sucesso" se AMBOS (Login e Senha) passarem em todas as regras.'''

print('Realizando Cadastro!')
login = input('Informe um login: ')
senha = input('Informe uma senha: ')
tamanho = len(senha)
if login:
    validacao_login = ' ' not in login and (login[0] == 'a' or login[0] == 'A')
else:
    validacao_login = False
try:
    senha_int = int(senha)
    validacao_senha = tamanho >= 4 and senha_int % 2 != 0
    if validacao_login:
        if validacao_senha:
            print('Cadastro realizado com sucesso')
        else:
            print('Erro: Senha fraca (tamanho ou paridade)')
    else:
        print('Erro: Login inválido (espaços ou inicial incorreta)')
except:
        print('Erro: A senha deve ser númerica.')

# ==============================================================================
# ORIGINAL: Exercicios/lista_tarefas.py
# ==============================================================================

# PROJETO: Lista de Tarefas Simples
# Autor: [Eudes]
# Data: 16/12/2025
import os
import time
tarefas = []

while True:
    os.system('cls')
    print('\n--- MENU ---')
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Apagar uma tarefa')
    print('4. Sair')
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Você escolheu adicionar...')
        # Aqui vamos escrever a lógica de adicionar
        tarefa=input('Qual tarefa deseja adicionar: ')
        print("Tarefa adicionada!")
        time.sleep(2)
        tarefas.append(tarefa)
    elif opcao == '2':
        # Aqui vamos escrever a lógica de listar
            if len(tarefas) == 0:
                os.system('cls')
                print('Você não possui tarefas')   
            else:
                print('Suas tarefas são...')
                for item, topico in enumerate(tarefas):
                   print(f'[{item}] - {topico}')
    elif opcao == '3':
        if len(tarefas) == 0:
            print('Você não possui tarefas para apagar')
        else:
            print('\n--- LISTA PARA APAGAR ---')
            for indice, topico in enumerate(tarefas):
                print(f'[{indice}] - {topico}')
            try:
                apagar=int(input('Qual tarefa deseja apagar: '))
                del tarefas[apagar]
                print('Tarefa removida com sucesso!')
            except ValueError:
                print('Por favor, digite um número inteiro.')
            except IndexError:
                print('Índice não existe na lista.')
            except Exception:
                print('Erro desconhecido')

    elif opcao == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida!')
    input("\nPressione ENTER para continuar...")

# ==============================================================================
# ORIGINAL: Revisoes/estudos_teoricos/estudo_dict.py
# ==============================================================================

'''Sua Missão Agora:

    Copie, rode e entenda esse código.

    Desafio: Crie um dicionário chamado eu com seus dados: 'nome', 'idade', 'cargo' (pode por "Dev Python") e 'tecnologias' (aqui dentro coloque uma lista ['Python', 'Git']).

    Mande um print chamando seu nome e uma tecnologia.'''
# eu = {'Nome' : 'Eudes',
#       'Nome': 'Maria', 'idade': 50,
#       'Idade':  30,
#       'Cargo': 'Dev Python',
#       'Tecnologias': ['Python', 'Git']
# }

pessoas =[
     {'nome': 'Eudes', 'idade': 30},
     {'nome': 'Maria', 'idade': 55},
]
# pessoas.append({'nome': 'João', 'idade': 20})
# for pessoa in pessoas:
#     print(f"Seu nome é {pessoa['nome']} e idade {pessoa['idade']}")
import os
import time
while True:
    os.system('cls')
    print('\n--- Cadastro de Nova Pessoa ---')
    nome=input("Informe seu nome: ")
    try:
        idade=int(input("Informe sua idade: "))
    except ValueError:
        print('Erro: Somente números inteiros permitidos!')
        time.sleep(2)
        continue
    except Exception:
        print('Erro desconhecido reiniciando o programa')
        time.spleep(2)
        continue
    novo = {'nome': nome,'idade': idade}
    pessoas.append(novo)
    for pessoa in pessoas:
        print(f'Seu nome é {pessoa['nome']} e sua idade {pessoa['idade']}')
    sair = input("Deseja sair do programa: [s]im ou [n]ão")
    if sair.lower() == 's':
        break
    else:
        print('Continuando o programa!')
        time.sleep(2)

# ==============================================================================
# ORIGINAL: Revisoes/estudos_teoricos/sistema_pessoas.py
# ==============================================================================

import os
import time
#outro problema que eu vejo é o codigo todo em si, que eu entendo como ta funcionando as coisas, mas se colocasse pra eu fazer do zero, não sei colocar em codigo
def limpar_tela():
    os.system('cls')
def mostrar_lista(lista_de_pessoas):
    print('--- LISTA ATUAL DE PESSOAS ---')
    if not lista_de_pessoas:
        print(" (Nenhuma pessoa cadastrada ainda)")
    print(f"{'NOME':<20} | {'CARGO':<20} | IDADE")
    print('-' * 60)
    for pessoa in lista_de_pessoas:
        print(f"{pessoa['nome']:<20} | {pessoa['cargo']:<20} | {pessoa['idade']} anos")
def cadastrar_pessoas():
    print('\n--- NOVO CADASTRO ---')
    nome=input('Informe seu nome: ')
    cargo = input('Informe seu cargo: ')
    while True:
        try:
            idade = int(input('Informe a idade: '))
            return {'nome': nome, 'idade': idade, 'cargo': cargo}
        except ValueError:
            print('❌ Erro: Digite apenas números!')
def apagar_pessoas():
    # PASSO 1: MOSTRAR A LISTA COM OS IDS
    # Note que aqui eu NÃO pergunto nada, só mostro.
    print('--- ESCOLHA QUEM APAGAR ---')
    for id_da_lista, pessoa in enumerate(pessoas):
        # Corrigi as aspas: Usei aspas simples fora e DUPLAS dentro do dicionário
        print(f'ID: {id_da_lista} | Nome: {pessoa["nome"]} | Cargo: {pessoa["cargo"]}')
    print('-' * 60)

    # PASSO 2: PERGUNTAR (FORA DO LOOP)
    # Agora que a lista inteira já apareceu, a gente pergunta UMA vez só.
    try:
        apagar = int(input('Digite o número do ID para apagar: '))
        
        # O .pop() remove pelo índice e devolve quem foi apagado
        nome_removido = pessoas.pop(apagar) 
        
        print(f"✅ {nome_removido['nome']} foi removido com sucesso!")
        time.sleep(1)
        
    except IndexError:
        print('Erro: Esse ID não existe!')
        time.sleep(1)
    except ValueError:
        print('Erro: Digite apenas o número!')
        time.sleep(1)
pessoas = [
     {'nome': 'Eudes', 'idade': 30, 'cargo': 'Dev. Python'},
]
while True:
    limpar_tela()
    mostrar_lista(pessoas)
    print('\n[1] Cadastrar nova pessoa')
    print('[2] Apagar Cadastro')
    print('[3] Sair do sistema')
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        nova = cadastrar_pessoas()
        pessoas.append(nova)
        print('Salvo!')
        time.sleep(1)

    elif opcao == '2':
        apagar_pessoas()
    elif opcao =='3':
        print('Saindo')
        break
    else:
        print('Opção inválida!')
        time.sleep(1)

# ==============================================================================
# ORIGINAL: Revisoes/revisao16.py
# ==============================================================================

'''
if / elif       /else
se / se não se  / se não
'''
entrada = input('Você quer "entrar" ou "sair"? ')
while entrada == True:
    if entrada == 'entrar':
        print('Você entrou no sistema')
    elif entrada == 'sair':
        print('Você saiu do sistema')
    else:
        print('Você precisa digitar "entra" ou "sair"')

# ==============================================================================
# ORIGINAL: Revisoes/revisao2.py
# ==============================================================================

import re
clientes = []
produtos = [{"id": 1, "nome": "Mouse", "preço": 49.90, "estoque": 10}]
# ---------- Funções de entrada ----------
def input_texto(msg):
    texto = input(msg).strip()
    return texto if texto else None
def input_numero(msg, positivo=False):
    try:
        num = float(input(msg))
        if positivo and num < 0:
            print("Digite apenas números positivos.")
            return None
        return num
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return None
# ---------- Cadastro de Cliente ---------- 
def nome_cadastro():
    return input_texto("Informe o nome: ")
def cpf_cadastro():
    cpf_sujo = input_texto("Informe seu CPF: ")
    if not cpf_sujo:
        return None
    cpf_limpo = ''.join(filter(str.isdigit, cpf_sujo))
    return cpf_limpo if len(cpf_limpo) == 11 else None
def validar_cpf(cpf):
    if cpf == cpf[0] * len(cpf):
        print("CPF inválido (sequência repetida).")
        return None
    def calcular_digito(digs, peso):
        total = sum(int(d) * p for d, p in zip(digs, range(peso, 1, -1)))
        digito = (total * 10) % 11
        return 0 if digito > 9 else digito
    n1 = calcular_digito(cpf[:9], 10)
    n2 = calcular_digito(cpf[:9] + str(n1), 11)
    return cpf if cpf.endswith(f"{n1}{n2}") else None
def email_cadastro():
    email = input_texto("Informe o e-mail: ")
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao, email):
        return email
    print("E-mail inválido.")
    return None
def cadastro_completo():
    nome = nome_cadastro()
    cpf = validar_cpf(cpf_cadastro())
    email = email_cadastro()
    if None in (nome, cpf, email):
        print("Todos os dados devem ser preenchidos corretamente.")
        return
    clientes.append({'nome': nome, 'cpf': cpf, 'email': email})
    print("Cliente cadastrado com sucesso!")
# ---------- Cadastro de Produto ----------
def nome_produto():
    return input_texto("Informe o nome do produto: ")
def codigo_produto():
    return 1 if not produtos else max(p['id'] for p in produtos) + 1
def preco_produto():
    return input_numero("Informe o valor do produto: ", positivo=True)
def quantidade_estoque():
    return int(input_numero("Informe a quantidade em estoque: ", positivo=True) or 0)
def ajuste_estoque(estoque_atual):
    try:
        escolha = int(input("Deseja: [1] Adicionar ou [0] Remover do estoque? "))
        qtd = int(input("Informe a quantidade: "))
        if qtd < 0:
            print("A quantidade não pode ser negativa.")
            return None
        if escolha == 1:
            return qtd
        elif escolha == 0:
            if estoque_atual - qtd < 0:
                print("Estoque não pode ficar negativo.")
                return None
            return -qtd
        else:
            print("Opção inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None
def cadastro_produto():
    nome = nome_produto()
    preco = preco_produto()
    id = codigo_produto()
    quantidade = quantidade_estoque()
    if None in (nome, preco, id, quantidade):
        print("Erro no preenchimento dos dados.")
        return
    for produto in produtos:
        if produto["nome"] == nome and produto["preço"] == preco:
            ajuste = ajuste_estoque(produto["estoque"])
            if ajuste is not None:
                produto["estoque"] += ajuste
            return
    produtos.append({"id": id, "nome": nome, "preço": preco, "estoque": quantidade})
    print("Produto cadastrado com sucesso!")

