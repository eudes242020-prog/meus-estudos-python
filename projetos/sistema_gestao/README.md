# Sistema de Gestão

Sistema de linha de comando (CLI) em Python para gerenciamento de clientes, produtos e vendas.

## Funcionalidades

**Perfil Administrador**
- Cadastrar e visualizar produtos com estoque
- Listar clientes cadastrados
- Relatório geral de vendas
- Vendas filtradas por cliente (CPF)
- Total gasto por cliente

**Perfil Cliente**
- Cadastro com nome, CPF e e-mail (com validação de CPF único)
- Realizar compras com seleção de produto e quantidade
- Dados persistidos em arquivo JSON

## Estrutura dos Módulos

| Arquivo | Responsabilidade |
|---------|-----------------|
| `main.py` | Menus e fluxo principal da aplicação |
| `banco_dados.py` | Dados iniciais de clientes, produtos e vendas |
| `cadastro_clientes.py` | Cadastro, validação e persistência de clientes |
| `produtos.py` | Cadastro e exibição de produtos |
| `compras.py` | Registro de compras e atualização de estoque |
| `relatorios.py` | Relatórios de vendas por diferentes critérios |
| `utils.py` | Funções utilitárias (limpar tela, pausar) |

## Como executar

```bash
cd projetos/sistema_gestao
python main.py
```

## Demonstração

```
Você é:
[1] Administrador
[2] Cliente
[0] Sair
```

Ao selecionar **Cliente**, é possível se cadastrar e realizar compras. Ao selecionar **Administrador**, são exibidos relatórios e controle de produtos.

## Conceitos aplicados

- Separação de responsabilidades em múltiplos módulos
- Persistência de dados com JSON (`json.load` / `json.dump`)
- Estruturas de dados: listas de dicionários
- Tratamento de exceções (`try/except`)
- Funções com parâmetros e retornos
- Menus interativos via `input()`
