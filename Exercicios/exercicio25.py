# Código do Estagiário (Perigo!)
# Ele cria uma lista GIGANTE na memória só para pegar o primeiro item depois.

import sys # Biblioteca para ver o tamanho das coisas

# 1. LISTA (Usa colchetes [])
# O Python cria TODOS os números e salva na memória agora.
lista = [n for n in range(1000000)]
print(f"Tamanho da Lista na RAM: {sys.getsizeof(lista)} bytes")

# 2. GERADOR (Usa parênteses ())
# O Python NÃO cria os números. Ele só guarda a "receita".
gerador = (n for n in range(1000000))
print(f"Tamanho do Gerador na RAM: {sys.getsizeof(gerador)} bytes")