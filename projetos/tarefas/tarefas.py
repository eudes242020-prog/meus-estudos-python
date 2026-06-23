import sqlite3
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
    novo=Tarefa(tarefa)
    return novo
def concluir_tarefa(numero):
        conexao = sqlite3.connect("tarefas.db")
        item = conexao.cursor()
        item.execute("UPDATE tarefas SET status = ? WHERE id = ?", (True,numero))
        conexao.commit()
        verificar=item.rowcount
        if verificar==0:
            return 'Não existe esse id'
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
def remover_tarefa(numero):
        conexao = sqlite3.connect("tarefas.db")
        item = conexao.cursor()
        item.execute("DELETE FROM tarefas WHERE id = ?", (numero,))
        conexao.commit()
        verificar=item.rowcount
        if verificar==0:
            return 'Não existe esse id'