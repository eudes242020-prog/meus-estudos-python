import copy

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos=copy.deepcopy(produtos)
def aumento_preço(produtos):
    for produto in produtos:
        produto['preco'] *= 1.1
aumento_preço(novos_produtos)

for produto in novos_produtos:
    print(f'{produto["nome"]}: {produto["preco"]:.2f}')

print()
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos), 
    key=lambda p: p['nome'], 
    reverse=True
)
for produto in produtos_ordenados_por_nome:
    print(f'{produto["nome"]}: {produto["preco"]:.2f}')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print()
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos), 
    key=lambda p: p['preco']
)
for produto in produtos_ordenados_por_preco:
    print(f'{produto["nome"]}: {produto["preco"]:.2f}')