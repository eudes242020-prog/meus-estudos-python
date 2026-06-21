class Tarefa:
    def __init__(self, tarefa, status=False):
        self.tarefa=tarefa
        self.status=status
    def marcar_concluida(self):
        self.status=True
    def __str__(self):
        if self.status:
            return f'{self.tarefa} está concluida'
        return f'{self.tarefa} não está concluida'
def entrada_usuario():
    while True:
        tarefa=input('Digite uma tarefa: ').strip()
        if tarefa.isdigit():
            print('Tarefa não pode ser apenas números')
            continue
        if not tarefa:
            print('Algo precisa ser digitado')
            continue    
        return tarefa
def adicionar_tarefa(lista, tarefa):
    lista.append(Tarefa(tarefa))   
def concluir_tarefa(lista, numero):
    try:
        variavel = lista[numero-1]
        variavel.marcar_concluida()
    except IndexError:
        return 'Não existe essa tarefa'        
def entrada_numero():
    while True:
        try:
            numero=int(input('Número da tarefa: '))
            if numero > 0:
                return numero
            print('Número precisa ser maior que zero ')
        except ValueError:
            print('Precisa ser um número inteiro')
            continue
def remover_tarefa(lista, numero):
    try:
        variavel=lista[numero-1]
        lista.remove(variavel)
    except ValueError:
        return  'Precisa ser um número'
    except IndexError:
        return 'Não existe essa tarefa' 