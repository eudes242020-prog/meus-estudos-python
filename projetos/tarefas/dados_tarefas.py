import json
from tarefas import Tarefa
def salvar_tarefas(tarefas):
   with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        lista=[]
        for t in tarefas: 
            lista.append({"tarefa" : t.tarefa, "status" : t.status})
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)
       
def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            tarefas_carregadas = json.load(arquivo)
            lista=[]
            for d in tarefas_carregadas:
                lista.append(Tarefa(d["tarefa"], d["status"]))
        return lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []