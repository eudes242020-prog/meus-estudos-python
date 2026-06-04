import os
import re
import shutil

origens = ['Exercicios', 'Revisoes']
destino = 'Trilha_Estudos'

categorias = {
    '21_miniprojetos_e_sistemas.py': [r'(?i)sistema', r'(?i)cadastro', r'(?i)caixa eletr', r'(?i)lista de tarefas', r'(?i)projeto', r'(?i)cine python'],
    '20_programacao_funcional_map_filter_reduce.py': [r'\bmap\(', r'\bfilter\(', r'\breduce\(', r'\bitertools\b', r'\bpartial\b'],
    '19_decoradores.py': [r'@\w+', r'(?i)decorador'],
    '18_tratamento_de_excecoes_try_except.py': [r'\btry:', r'\bexcept\b', r'\bfinally:', r'\braise\b'],
    '17_geradores_e_iteradores.py': [r'\byield\b', r'(?i)generator', r'\biter\('],
    '16_list_e_dict_comprehensions.py': [r'\[.+for.+in.+\]', r'\{.+for.+in.+\}', r'(?i)comprehension'],
    '15_modulos_e_importacoes.py': [r'\b__main__\b', r'\bsys\.path\b', r'(?i)módulo padrão'],
    '14_funcoes_lambda_e_primeira_classe.py': [r'\blambda\b', r'(?i)primeira classe', r'(?i)higher order'],
    '13_funcoes_args_kwargs_e_escopo.py': [r'\*args', r'\*\*kwargs', r'\bglobal\b', r'\bnonlocal\b'],
    '12_funcoes_basicas_e_retornos.py': [r'\bdef \w+\(', r'\breturn\b'],
    '11_sets_e_conjuntos.py': [r'\bset\(', r'\.union\(', r'\.intersection\('],
    '10_dicionarios.py': [r'\.keys\(', r'\.values\(', r'\.items\(', r'(?i)dicionário', r'(?i)dict'],
    '09_tuplas_estruturas_imutaveis.py': [r'(?i)tupla', r'(?i)tuple'],
    '08_listas_e_mutabilidade.py': [r'\.append\(', r'\.pop\(', r'\.insert\(', r'(?i)lista '],
    '07_lacos_de_repeticao_for.py': [r'\bfor .* in \b'],
    '06_lacos_de_repeticao_while.py': [r'\bwhile\b'],
    '05_condicionais_if_elif_else.py': [r'\bif\b', r'\belif\b', r'\belse:\b'],
    '04_manipulacao_de_strings_e_fatiamento.py': [r'\.split\(', r'\.join\(', r'\.upper\(', r'\.lower\(', r'\[::-1\]', r'(?i)fatiamento'],
    '03_operadores_logicos_e_relacionais.py': [r'\band\b', r'\bor\b', r'\bnot\b', r'==', r'>=', r'<='],
    '02_operadores_aritmeticos.py': [r'\+', r'-', r'\*', r'/', r'//', r'%'],
    '01_variaveis_e_tipos_de_dados.py': [r'.*'] # Fallback
}

if not os.path.exists(destino):
    os.makedirs(destino)

# Dicionario para armazenar o conteudo por categoria
conteudo_por_categoria = {cat: [] for cat in categorias.keys()}

# Processar arquivos
for pasta in origens:
    if not os.path.exists(pasta):
        continue
    for root, dirs, files in os.walk(pasta):
        for file in files:
            if not file.endswith('.py'):
                continue
            
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                
            # Identificar categoria
            categoria_escolhida = '01_variaveis_e_tipos_de_dados.py'
            for cat, regexes in categorias.items():
                match = False
                for padrao in regexes:
                    if re.search(padrao, conteudo):
                        categoria_escolhida = cat
                        match = True
                        break
                if match:
                    break
            
            # Formatar bloco
            bloco = f"# ==============================================================================\n"
            bloco += f"# ORIGINAL: {os.path.relpath(filepath).replace(os.sep, '/')}\n"
            bloco += f"# ==============================================================================\n\n"
            bloco += conteudo.strip() + "\n\n"
            
            conteudo_por_categoria[categoria_escolhida].append((filepath, bloco))

# Escrever nos novos arquivos
for cat, blocos in conteudo_por_categoria.items():
    if not blocos:
        continue
    
    # Ordenar por nome do arquivo original para manter alguma coesão
    blocos.sort(key=lambda x: x[0])
    
    dest_path = os.path.join(destino, cat)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(f"# TÓPICO: {cat.replace('.py', '').replace('_', ' ').title()}\n\n")
        for _, bloco in blocos:
            f.write(bloco)

print("Organização concluída!")

# Renomear pastas originais para backup
for pasta in origens:
    if os.path.exists(pasta):
        backup_name = f"{pasta}_backup"
        if os.path.exists(backup_name):
            shutil.rmtree(backup_name)
        os.rename(pasta, backup_name)
        print(f"Pasta {pasta} renomeada para {backup_name}")

