# TESTE DE MEMÓRIA: LISTA vs GERADOR
# Aprendizado do dia: Listas carregam tudo na RAM de uma vez.
# Geradores (usando parênteses) criam sob demanda (Lazy Evaluation).
#
# Ruim para memória pois útiliza uma quantidade muito alta (List Comprehension [])
# ainda não me aprofudei nesse assunto mais em breve voltaria para dizer que entendi tudo em 100%
# lista_pesada = [x for x in range(10000000)]

# 2. GERADOR (Usa parênteses ())
# O Python NÃO cria os números. Ele só guarda a "receita".
import sys
gerador = (n for n in range(1000000))
print(f"Tamanho do Gerador na RAM: {sys.getsizeof(gerador)} bytes")