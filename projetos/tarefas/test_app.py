import pytest
from app import app, fazer_tabela
from dados_tarefas import conexao_api, salvar_tarefas
from tarefas import Tarefa
import dados_tarefas
cliente = app.test_client()
def test_listar_tarefas(arrumar_banco):
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
def test_marcar_id_inexistente(arrumar_banco):
    resposta=cliente.put('/tarefas/99')
    assert resposta.status_code == 404
def test_marcar_id_existente(arrumar_banco):
    salvar_tarefas((Tarefa(None,'varrer casa')))
    resposta = cliente.put("/tarefas/1")
    assert resposta.status_code == 200
def test_criar_tarefa(arrumar_banco):
    resposta=cliente.post('/tarefas', json={'tarefa':'tarefa'})
    assert resposta.status_code== 200
    ver=cliente.get('/tarefas')
    coisa=ver.get_data(as_text=True)
    assert "tarefa" in coisa
def test_remover_tarefa(arrumar_banco):
    cliente.post('/tarefas', json={'tarefa':'tarefa'})
    resposta=cliente.delete('/tarefas/1')
    assert resposta.status_code== 200
    ver=cliente.get('/tarefas/1')
    coisa=ver.get_data(as_text=True)
    assert "tarefa" not in coisa
def test_remover_tarefa_inexistente(arrumar_banco):
    resposta=cliente.delete('/tarefas/99')
    assert resposta.status_code== 404
def test_criar_vazia(arrumar_banco):
    resposta=cliente.post('/tarefas', json={})
    assert resposta.status_code== 400
@pytest.fixture
def arrumar_banco():
    dados_tarefas.banco_atual = "teste.db"
    conexao=conexao_api()
    conexao.execute('DROP TABLE IF EXISTS tarefas')
    fazer_tabela(conexao)
    conexao.commit()