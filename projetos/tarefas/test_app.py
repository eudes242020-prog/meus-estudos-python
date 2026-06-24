from app import app

cliente = app.test_client()
def test_listar_tarefas():
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
def test_marcar_id_inexistente():
    resposta=cliente.put('/tarefas/99')
    assert resposta.status_code == 404