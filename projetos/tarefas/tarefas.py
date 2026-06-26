class Tarefa:
    def __init__(self,id ,tarefa, status=False):
        self.id=id
        self.tarefa=tarefa
        self.status=status
    def marcar_concluida(self):
        self.status=True
    def __str__(self):
        if self.status:
            return f'{self.tarefa} está concluída'
        return f'{self.tarefa} não está concluída'
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
def adicionar_tarefa(tarefa):
    novo=Tarefa(None,tarefa)
    return novo
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