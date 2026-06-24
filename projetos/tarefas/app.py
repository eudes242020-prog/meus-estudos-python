import sqlite3
from flask import Flask, jsonify, request
from dados_tarefas import carregar_tarefas, salvar_tarefas
from tarefas import adicionar_tarefa, concluir_tarefa,remover_tarefa
app=Flask(__name__)
@app.route("/tarefas")
def listar_tarefas():
    return jsonify(transporte_api(carregar_tarefas()))
@app.route("/tarefas", methods=["POST"])
def adicionar():
    try:
        dados=request.get_json()
        texto=dados["tarefa"]
        salvar_tarefas(adicionar_tarefa(texto))
        return jsonify({"mensagem": "tarefa criada"})
    except KeyError:
        return "Tarefa precisa ser preenchida", 400
@app.route("/tarefas/<int:id>", methods=['PUT'])
def marcar(id):
    item=concluir_tarefa(id)
    if item == 'Não existe esse id':
        return "Esse ID não existe no banco", 404
    return jsonify(item)
@app.route("/tarefas/<int:id>", methods=['DELETE'])
def tirar_tarefa(id):
    remover=remover_tarefa(id)
    if remover == 'Não existe esse id':
        return "Esse ID não existe no banco", 404
    return jsonify(remover)
def transporte_api(tarefas):
    lista=[]
    for item in tarefas:
        tarefa={"id" : item.id, "tarefa" : item.tarefa, "status": item.status}
        lista.append(tarefa)
    return lista
def fazer_tabela():
    criar=sqlite3.connect('tarefas.db')
    criar.execute("CREATE TABLE IF NOT EXISTS tarefas(id INTEGER PRIMARY KEY, tarefa TEXT, status INTEGER)")
    criar.commit()
if __name__== "__main__":
    fazer_tabela()
    app.run(debug=True)