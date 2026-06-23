import sqlite3
from tarefas import Tarefa
def salvar_tarefas(tarefa):
    conexao = sqlite3.connect("tarefas.db")
    item = conexao.cursor()
    item.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    tarefa TEXT,
    status INTEGER
    ) """)
    item.execute("INSERT INTO tarefas (id, tarefa, status) VALUES (? ,?, ?)", (tarefa.id ,tarefa.tarefa,tarefa.status))
    conexao.commit()
def carregar_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    item = conexao.cursor()
    item.execute("SELECT * FROM tarefas")
    receber=item.fetchall()
    lista=[]
    for d in receber:
        lista.append(Tarefa(d[0], d[1], d[2]))
    return lista
