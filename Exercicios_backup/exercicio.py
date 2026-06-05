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