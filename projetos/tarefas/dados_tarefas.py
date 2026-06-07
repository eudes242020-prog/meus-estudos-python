import json
def salvar_tarefas(tarefas):
   with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
       json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)
       
def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            tarefas_carregadas = json.load(arquivo)
        return tarefas_carregadas
    except FileNotFoundError:
        return []
    