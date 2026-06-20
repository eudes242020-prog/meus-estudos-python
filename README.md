# Meus Estudos em Python

Repositório de aprendizado em **Python** com foco em **desenvolvimento backend**. Construído a partir de trilha de estudos progressiva e projetos práticos reais desenvolvidos do zero.

## Stack e Conceitos

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Em%20andamento-orange)
![JSON](https://img.shields.io/badge/Persistência-JSON-yellow)
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
- **Orientação a Objetos:** classes, `__init__`, atributos, métodos de instância, serialização

## Projetos

### Sistema de Controle de Tarefas (CLI + POO + Persistência)

Projeto construído do zero ao longo de múltiplas sessões práticas. Evoluiu de funções simples para uma arquitetura orientada a objetos com persistência real em disco.

```
sistema_tarefas/
├── tarefas.py          # Classe Tarefa + operações (adicionar, remover, marcar)
├── dados_tarefas.py    # Persistência JSON: serialização objeto→dict e dict→objeto
├── mostrar_tarefas.py  # Exibição formatada das tarefas
└── main_tarefas.py     # Menu CLI com validação de input
```

**Destaques técnicos:**
- Classe `Tarefa` com atributos `tarefa` e `status`, método `marcar_concluida(self)`
- Serialização/deserialização manual: `objeto → dict` para salvar, `dict → Tarefa` ao carregar
- Tratamento de múltiplos erros de arquivo: `FileNotFoundError` e `json.JSONDecodeError`
- Validação de input com princípio DRY: funções separadas para coletar, validar e orquestrar
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
    ├── sistema_tarefas/     # Projeto POO com persistência JSON
    └── sistema_gestao/      # Sistema CLI com múltiplos módulos
```

## Como executar

**Pré-requisitos:** Python 3.10+

```bash
# Clonar o repositório
git clone https://github.com/eudes242020/meus-estudos-python.git
cd meus-estudos-python

# Sistema de Tarefas
cd projetos/sistema_tarefas
python main_tarefas.py

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
| Orientação a Objetos (classes, métodos, atributos) | 🔄 Em andamento |
| Banco de dados (SQLite → SQL) | ⏳ Próximo |
| APIs REST (Flask / FastAPI) | ⏳ Planejado |

---

*Foco: Backend Development*
> "O teto que importa não é talento, é frequência."
