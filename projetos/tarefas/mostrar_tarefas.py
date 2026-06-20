def ver_tarefas(lista):
    for item in lista:
        if item.status:
            print(f"Tarefa: {item.tarefa} está concluida")
        else:
            print(f"Tarefa: {item.tarefa} está pendente")