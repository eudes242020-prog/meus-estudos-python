import sqlite3
from tarefas import Tarefa
banco_atual = "tarefas.db"
def salvar_tarefas(tarefa):
    conectar=conexao_api()
    item = conectar.cursor()
    item.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    tarefa TEXT,
    status INTEGER
    ) """)
    item.execute("INSERT INTO tarefas (tarefa, status) VALUES (?, ?)", (tarefa.tarefa,tarefa.status))
    conectar.commit()
    conectar.close()
def carregar_tarefas():
    conectar = conexao_api()
    item = conectar.cursor()
    item.execute("SELECT * FROM tarefas")
    receber=item.fetchall()
    conectar.close()
    lista=[]
    for d in receber:
        lista.append(Tarefa(d[0], d[1], d[2]))
    return lista
def conexao_api():
    criar=sqlite3.connect(banco_atual)
    return criar
def remover_tarefa(numero):
    try:
        conexao = conexao_api()
        item = conexao.cursor()
        item.execute("DELETE FROM tarefas WHERE id = ?", (numero,))
        verificar=item.rowcount
        if verificar==0:
            return 'Não existe esse id'
        conexao.commit()
        return "Tarefa removida"
    finally:
        conexao.close()   
def concluir_tarefa(numero):
    try:     
        conexao = conexao_api()
        item = conexao.cursor()
        item.execute("UPDATE tarefas SET status = ? WHERE id = ?", (True,numero))
        verificar = item.rowcount    
        if verificar == 0:
            return 'Não existe esse id'
        conexao.commit()             
        return 'Tarefa feita!'
    finally:
        conexao.close()