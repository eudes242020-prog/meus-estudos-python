import sqlite3
from produtos import Produto
from compras import Venda
lista_para_exibir = [
    {'nome': 'João Silva', 'cpf': '12345678900', 'email': 'joao@email.com'},
    {'nome': 'Maria Souza', 'cpf': '98765432100', 'email': 'maria@email.com'}
]
vendas = []
admins=[]
def conexao_api():
    criar=sqlite3.connect('banco_sistema_gestao.db')
    return criar
# tabela produtos
def criar_tabela_produto():
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
def criar_tabela_venda():
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute('''CREATE TABLE IF NOT EXISTS vendas(
    id INTEGER PRIMARY KEY,
    cpf TEXT,
    valor_total INTEGER,
    data TEXT
    )''')
    conexao.commit()
    conexao.close()
def criar_tabela_itens():
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute('''CREATE TABLE IF NOT EXISTS itens_vendas(
    id INTEGER PRIMARY KEY,
    venda_id INTEGER,
    produto TEXT,
    preco INTEGER,
    quantidade INTEGER
    )''')
    conexao.commit()
    conexao.close()
#faz parte da tabela produtos
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
def ajuste_de_estoque(produto):
    try:
        conexao=conexao_api()
        item=conexao.cursor()
        item.execute('UPDATE produtos SET estoque = ? WHERE id = ?', (produto.estoque,produto.id,))
        verificar=item.rowcount
        if verificar == 0:
            return 'Não existe esse id'
        conexao.commit()
        return 'Estoque ajustado'
    finally:
        conexao.close()
def apagar_produto(produto):
    try:
        conexao=conexao_api()
        item=conexao.cursor()
        item.execute('DELETE FROM produtos WHERE id = ?',(produto.id,))
        verificar=item.rowcount
        if verificar == 0:
            return 'Não existe esse id'
        conexao.commit()
        return 'Produto removido'
    finally:
        conexao.close()
#faz parte da tabela venda
def salvar_venda(venda):
    try:
        conexao=conexao_api()
        item=conexao.cursor()
        item.execute('INSERT INTO vendas (cpf, valor_total, data) VALUES (?, ?, ?)', (venda.cliente.cpf, venda.valor_total, str(venda.data)))
        identificar=item.lastrowid
        conexao.commit()
        return identificar
    finally:
        conexao.close()
def carregar_venda(clientes):
    conexao=conexao_api()
    item=conexao.cursor()
    item.execute('SELECT * FROM vendas')
    vendas=item.fetchall()
    conexao.close()
    lista=[]
    for venda in vendas:
        for cliente in clientes:
            if venda[1]==cliente.cpf:
                lista.append(Venda(cliente,))
    
#faz parte da tabela itens_venda
def salvar_itens_venda(produto,ident):
    conexao=conexao_api()
    item=conexao.cursor()
    for cada in produto.produtos:
        item.execute('INSERT INTO itens_vendas (venda_id, produto, preco, quantidade) VALUES (?, ?, ?, ?)',(ident,cada['produto'],cada["preço unitario"], cada['quantidade']))
    conexao.commit()
    conexao.close()