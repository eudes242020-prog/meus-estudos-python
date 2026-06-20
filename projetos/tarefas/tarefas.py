class Tarefa():
    def __init__(self, tarefa, status=False):
        self.tarefa=tarefa
        self.status=status
    def marcar_concluida(self):
        self.status=True
def entrada_usuario():
    while True:
        tarefa=input('Digite uma terefa: ').strip()
        if tarefa.isdigit() or not tarefa:
            print('Tarefa não pode ser apenas números')
            continue
        return tarefa
def adicionar_tarefa(lista, tarefa):
    lista.append(Tarefa(tarefa))

def remover_tarefa (lista, remocao):  
    for item in lista:
        if item.tarefa == remocao:
            lista.remove(item)
            break
    else:
        return "Não existe essa tarefa"    
def marcar_concluida(lista, tarefa):
    for item in lista:
        if item.tarefa == tarefa:
            item.marcar_concluida()
            break
    else:
        return 'Não existe essa tarefa'        
# def pegar_nome_tarefa():
#     tarefa=input('Informe uma tarefa: ')
#     return tarefa
# def validar_nome_tarefa(tarefa):
#     if tarefa and len(tarefa.strip()) >=2 and not tarefa.isdigit() :
#         return tarefa
#     else:
#         return None
