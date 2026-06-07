def adicionar_tarefa(lista, tarefa):
    lista.append({'nome': tarefa, 'status': False})
def remover_tarefa (lista, remocao):  
    for item in lista:
        if item['nome'] == remocao:
            lista.remove(item)
            break
    else:
        return "Não existe essa tarefa"    
def marcar_concluida(lista, tarefa):
    for item in lista:
        if item['nome'] == tarefa:
            item['status']=True
            break
    else:
        return 'Não existe essa tarefa'        
def pegar_nome_tarefa():
    tarefa=input('Informe uma tarefa: ')
    return tarefa
def validar_nome_tarefa(tarefa):
    if tarefa and len(tarefa.strip()) >=2 and not tarefa.isdigit() :
        return tarefa
    else:
        return None
