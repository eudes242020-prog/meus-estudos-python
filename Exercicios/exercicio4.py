'''Exercício 3: Cálculo de Média Final com Bônus

Crie um programa que calcule a média ponderada de um aluno e decida sua aprovação, incorporando um fator bônus.

    Colete via input() as notas de três provas (P1, P2, P3).

    Colete um valor de "Bônus" que será somado à nota final (pode ser 0).

    Garanta que todas as entradas sejam tratadas como números de ponto flutuante (float).

    Calcule a Média Ponderada das três provas com os seguintes pesos:
    Média=10(P1x2)+(P2 x 3)+(P3 x 5)

    Calcule a Nota Final somando a Média ao Bônus.

    Use a lógica condicional para determinar o status do aluno (use if/elif/else):

        Se a Nota Final for maior ou igual a 7.0: APROVADO com nota {Nota Final}.

        Se a Nota Final for maior ou igual a 5.0 e menor que 7.0: RECUPERAÇÃO com nota {Nota Final}.

        Se a Nota Final for menor que 5.0: REPROVADO com nota {Nota Final}.

    Use f-strings para exibir a Nota Final com duas casas decimais.'''
nota1 = input('Informe sua primeira nota: ')
nota2 = input('Informe sua segunda nota: ')
nota3 = input('Informe sua Terceira nota: ')
nota1_float=float(nota1)
nota2_float=float(nota2)
nota3_float=float(nota3)
media = ((nota1_float*2)+ (nota2_float * 3)+ (nota3_float * 5)) / 10
b = input('Tem ponto por trabalho? "sim" ou "não" ')
if b == 'sim':
    valor = input('Informe sua pontuação bonus: ')
    valor_float = float(valor)
    media_final= valor_float + media
    if media_final >=7:
        print(f'APROVADO com nota {media_final}')
    elif media_final >=5 and media_final <7:
        print(f'RECUPERAÇÃO com nota {media_final}')
    elif media_final <5:
        print(f'REPROVADO com nota final {media_final}')
if b == 'não':
    if media >=7:
        print(f'APROVADO com nota {media}')
    elif media >=5 and media <7:
        print(f'RECUPERAÇÃO com nota {media}')
    elif media <5:
        print(f'REPROVADO com nota {media}')
else:
        print('Necessario responder "sim" ou "não"')       