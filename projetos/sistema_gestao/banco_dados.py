import sqlite3
from produtos import Produto
lista_para_exibir = [
    {'nome': 'João Silva', 'cpf': '12345678900', 'email': 'joao@email.com'},
    {'nome': 'Maria Souza', 'cpf': '98765432100', 'email': 'maria@email.com'}
]
vendas = []
admins=[]
def conexao_api():
    criar=sqlite3.connect('banco_sistema_gestao.db')
    return criar
def criar_tabela():
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute("""CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY,
    produto TEXT,
    preco INTEGER,
    estoque INTEGER
    )""")
    conexao.commit()
    conexao.close()
def salvar_produtos(produto):
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute('INSERT INTO produtos (produto, preco, estoque) VALUES(?, ?, ?)',(produto.nome, produto.preco, produto.estoque,))
    conexao.commit()
    conexao.close()
def carregar_produtos():
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute("SELECT * FROM produtos")
    receber=item.fetchall()
    conexao.close()
    lista=[]
    for produto in receber:
        lista.append(Produto(produto[0],produto[1],produto[2],produto[3]))
    return lista
def compras_produtos(id ,compra):
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute("UPDATE produtos SET estoque = estoque - ? WHERE id = ?", (compra,id,))
    verificar = item.rowcount
    if verificar == 0:
        conexao.close()
        return 'Não existe esse id'
    conexao.commit()
    conexao.close()