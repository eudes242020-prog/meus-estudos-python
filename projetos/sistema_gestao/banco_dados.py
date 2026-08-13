lista_para_exibir = [
    {'nome': 'João Silva', 'cpf': '12345678900', 'email': 'joao@email.com'},
    {'nome': 'Maria Souza', 'cpf': '98765432100', 'email': 'maria@email.com'}
]
produtos = []
vendas = []
admins=[]

# --- Produtos de teste ---
# Ficam fixos aqui pra nascerem prontos a cada boot (assim você não precisa
# recadastrar a cada teste). Como não há persistência de produto, o estoque
# volta a estes valores toda vez que o programa reinicia — bom pra testar do zero.
#
# O import vem AQUI no fim de propósito: a classe Produto vive em produtos.py,
# que importa 'produtos' deste arquivo. Importar em cima = import circular.
# Usamos .extend (mutar a lista existente), não '=' (reatribuir quebraria a
# referência que produtos.py já pegou).
from produtos import Produto
produtos.extend([
    Produto(id=1, nome='Teclado',  preco=99.90,  estoque=10),
    Produto(id=2, nome='Mouse',    preco=49.90,  estoque=15),
    Produto(id=3, nome='Monitor',  preco=599.90, estoque=5),
    Produto(id=4, nome='Cabo HDMI', preco=19.90, estoque=30),
    Produto(id=5, nome='Webcam',   preco=149.90, estoque=8),
])