'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é nosso escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
'''
def escopo():
    x = 1
    print(x)
    #codigo dentro da função não pode ser usado fora do escopo
    #tem maneiras de dribla isso porem não é uma boa pratica
escopo()