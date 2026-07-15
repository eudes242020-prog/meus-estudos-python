# Meus Estudos em Python

Repositório de aprendizado em **Python** com foco em **desenvolvimento backend**. 

[**live demo**](https://meus-estudos-python.onrender.com/) - Sistema de Controle de Tarefas - _cold start (de 30 a 50 segundos para inicializar)_

Construído a partir de trilha de estudos progressiva e projetos práticos reais desenvolvidos do zero.

## Stack e Conceitos

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/POO-Concluído-brightgreen)
![SQLite](https://img.shields.io/badge/SQLite-CRUD%20completo-brightgreen?logo=sqlite&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Queries%20parametrizadas-blue)
![Flask](https://img.shields.io/badge/Flask-API%20REST%20(GET%2FPOST)-brightgreen?logo=flask&logoColor=white)
![REST](https://img.shields.io/badge/API-REST%20%2B%20JSON-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)

**Fundamentos cobertos:**
- Variáveis, tipos de dados e operadores
- Estruturas de controle (if/elif/else, while, for, for/else)
- Estruturas de dados: listas, tuplas, dicionários, sets
- Funções, escopo, *args, **kwargs, lambda
- Módulos, importações e separação de responsabilidades
- List/Dict comprehensions
- Geradores e iteradores
- Tratamento de exceções (`try/except` múltiplo, erros específicos)
- Decoradores
- Programação funcional (map, filter, reduce)
- **Orientação a Objetos:** classes, `__init__`, atributos, métodos de instância, `__str__`, métodos que alteram estado
- **Banco de dados SQLite:** `CREATE TABLE`, CRUD completo (`INSERT`/`SELECT`/`UPDATE`/`DELETE`), seleção por `id` com `WHERE`, queries parametrizadas (`?`) como defesa contra SQL injection, `fetchall`, `rowcount`
- **APIs REST com Flask:** servidor HTTP, rotas (`@app.route`), métodos GET e POST, leitura do corpo da requisição (`request.get_json()`), serialização de objetos para JSON (`jsonify`), setup de banco no arranque da aplicação
- **Gerenciamento de dependências:** instalação de pacotes externos (`pip install`), ambiente e ferramentas de teste de API (Thunder Client)

## Projetos

### Sistema de Controle de Tarefas (API REST + POO + SQLite)

Projeto construído do zero ao longo de múltiplas sessões práticas. Evoluiu de funções simples para uma arquitetura orientada a objetos, migrou a persistência de JSON para um banco de dados SQLite com **CRUD completo** e, na fase atual, ganhou uma **API REST em Flask** que expõe o mesmo CRUD pela rede — reutilizando as funções de dados já existentes (sem reescrever lógica).

```
projetos/tarefas/
├── app.py              # API REST (Flask): rotas GET/POST/PUT/DELETE + serialização para JSON
├── tarefas.py          # Classe Tarefa + operações de CRUD (INSERT/UPDATE/DELETE)
├── dados_tarefas.py    # Camada de dados SQLite: CREATE TABLE, INSERT, SELECT
├── mostrar_tarefas.py  # Exibição formatada das tarefas (via __str__)
├── main_tarefas.py     # Menu CLI com validação de input
├── test_app.py         # Testes automatizados com tratamento de erros
├── requirements.txt    # Lista de dependências necessárias para o projeto
└── templates           # Interface web que consome a API Flask.
```

**Destaques técnicos:**
- **API REST com Flask:** rota `GET /tarefas` (lista em JSON) e `POST /tarefas` (cria a partir do corpo da requisição), plugadas direto no CRUD SQLite já existente
- Serialização objeto → JSON: função `transporte_api` converte a lista de objetos `Tarefa` em lista de dicts antes do `jsonify` (a web só fala tipos básicos)
- Leitura do payload da requisição com `request.get_json()`, substituindo o `input()` do CLI
- Setup do banco no arranque da aplicação (`fazer_tabela()` chamada uma vez antes do `app.run`) com `CREATE TABLE IF NOT EXISTS` idempotente
- **Reuso real (DRY):** a API não duplica regra de negócio — chama `carregar_tarefas` e `salvar_tarefas`, as mesmas funções do CLI
- Classe `Tarefa` com `__init__`, `__str__` e método `marcar_concluida(self)` que altera estado
- **CRUD completo em SQLite por `id`:** criar (`INSERT`), listar (`SELECT` + `fetchall`), marcar (`UPDATE`) e remover (`DELETE`), cada operação mirando a linha certa com `WHERE id = ?`
- **Queries parametrizadas (`?`)** em vez de concatenação de strings — defesa contra SQL injection
- Tratamento de falha silenciosa: usa `cursor.rowcount` para detectar operação sobre `id` inexistente (que não lança exceção em SQL)
- Decisão de arquitetura consciente: **banco como fonte única da verdade** (toda leitura re-consulta o SQLite, sem cópia paralela em memória)
- Ponte linha↔objeto: tupla `(id, tarefa, status)` reconstruída em `Tarefa` ao carregar
- Arquitetura modular com responsabilidades bem definidas por arquivo

### Sistema de Gestão (CLI)

Sistema de linha de comando com dois perfis de acesso (Administrador e Cliente), cadastro de clientes com persistência em JSON, controle de estoque, registro de vendas e relatórios.

```
projetos/sistema_gestao/
├── main.py               # Menus e fluxo principal
├── banco_dados.py        # Dados iniciais
├── cadastro_clientes.py  # Cadastro e validação (CPF único)
├── compras.py            # Registro de compras e estoque
├── produtos.py           # Cadastro e exibição de produtos
├── relatorios.py         # Relatórios de vendas
└── utils.py              # Funções utilitárias
```

Veja mais detalhes em [projetos/sistema_gestao/README.md](projetos/sistema_gestao/README.md).

## Estrutura do Repositório

```
meus-estudos-python/
├── Trilha_Estudos/          # 21 tópicos estudados progressivamente
├── Exercicios_backup/       # 57+ exercícios de lógica e estruturas de dados
├── Revisoes_backup/         # Revisões e estudos teóricos
└── projetos/
    ├── tarefas/             # Projeto POO + CRUD SQLite + API REST (Flask)
    └── sistema_gestao/      # Sistema CLI com múltiplos módulos
```

## Como executar

**Pré-requisitos:** Python 3.10+

```bash
# Clonar o repositório
git clone https://github.com/eudes242020-prog/meus-estudos-python.git
cd meus-estudos-python

# Sistema de Tarefas (CLI)
cd projetos/tarefas
python main_tarefas.py

# API REST do Sistema de Tarefas (Flask)
cd projetos/tarefas
pip install -r requirements.txt
python app.py
# Servidor em http://127.0.0.1:5000
#   GET  /tarefas        -> lista as tarefas em JSON
#   POST /tarefas        -> cria tarefa; corpo JSON: {"tarefa": "estudar API"}

# Sistema de Gestão
cd projetos/sistema_gestao
python main.py
```

## Progresso

| Fase | Status |
|------|--------|
| Fundamentos (variáveis, operadores, condicionais, loops) | ✅ Concluído |
| Estruturas de dados (listas, tuplas, dicts, sets) | ✅ Concluído |
| Funções, módulos e escopo | ✅ Concluído |
| Comprehensions, geradores, decoradores | ✅ Concluído |
| Programação funcional | ✅ Concluído |
| Orientação a Objetos (classes, métodos, atributos, `__str__`) | ✅ Concluído |
| Banco de dados SQLite (CRUD completo por `id`, queries parametrizadas) | ✅ Concluído |
| APIs REST com Flask (rotas GET/POST, PUT/DELETE por `id` com tratamento de erros HTTP) |✅ Concluído|
| Testes automatizados - (rotas get/post - criar tarefa/remover/marcar e listar, erros tratados- pytest fixture arrumar banco)| ✅ Concluído |
| Front consumindo a API usando HTML e JS (fetch e DOM) | ✅ Concluído |
| Deploy integrando front e back via Render (Gunicorn + `requirements.txt`) | ✅ Concluído |
---

*Foco: Backend Development*
> "O teto que importa não é talento, é frequência."
