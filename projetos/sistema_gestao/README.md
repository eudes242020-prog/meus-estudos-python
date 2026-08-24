# Sistema de Gestão

Sistema de linha de comando (CLI) em Python para gerenciar clientes, produtos, vendas e relatórios, com dois perfis de acesso protegidos por login: **Administrador** e **Cliente**.

Projeto construído do zero, sem framework — só a biblioteca padrão (`sqlite3`, `json`, `datetime`). Começou com dicionários soltos e foi migrando para classes e banco de dados conforme fui estudando, então cada parte do código mostra uma etapa da evolução.

## Funcionalidades

**Administrador** (acesso com nome e senha)
- Criar outros administradores — o primeiro é criado na abertura, quando ainda não existe nenhum
- Cadastrar produto (nome, preço e estoque), com `id` gerado automaticamente
- Ver produtos cadastrados
- Gerenciar produto: ajustar estoque (entrada ou saída) ou remover do banco
- Ver clientes cadastrados
- Relatório de vendas (itens, quantidade, preço unitário e total)
- Vendas por cliente, buscando pelo CPF
- Total gasto por cliente
- Clientes que nunca compraram

**Cliente**
- Cadastro com nome, CPF, senha e e-mail — cada campo validado antes de ser aceito
- Login com CPF e senha
- Compra: escolhe o produto pelo nome ou pelo `id`, informa a quantidade, pode adicionar mais itens e fecha com o total
- O estoque é atualizado no banco no momento da compra, e a compra é bloqueada se deixar o estoque negativo

## Onde os dados ficam

| Dado | Persistência |
|------|--------------|
| Produtos | SQLite (`banco_sistema_gestao.db`) |
| Clientes | JSON (`config.json`, criado na primeira execução e fora do versionamento) |
| Vendas | Memória — os relatórios funcionam enquanto o programa está aberto |
| Administradores | Memória |

## Estrutura dos módulos

| Arquivo | Responsabilidade |
|---------|-----------------|
| `main.py` | Menus e fluxo principal da aplicação |
| `banco_dados.py` | Conexão com o SQLite, criação da tabela e operações de produto no banco (salvar, carregar, baixar estoque, ajustar, apagar) |
| `produtos.py` | Classe `Produto` + validações de nome, preço e quantidade + cadastro, ajuste e remoção |
| `cadastro_clientes.py` | Classe `Cliente` com validação de CPF, e-mail e senha + salvar/carregar em JSON |
| `admin.py` | Classe `Admin` + criação e validação de administradores |
| `login.py` | Login do administrador (nome + senha) e do cliente (CPF + senha) |
| `compras.py` | Classe `Venda` + seleção de produto, quantidade e fechamento da compra |
| `relatorios.py` | Relatórios de vendas por diferentes critérios |
| `utils.py` | Funções utilitárias (pausar e limpar a tela) |

## Como executar

**Pré-requisitos:** Python 3.10+ (não precisa instalar nenhuma dependência externa)

```bash
git clone https://github.com/eudes242020-prog/meus-estudos-python.git
cd meus-estudos-python/projetos/sistema_gestao
python main.py
```

Na primeira execução o banco e a tabela de produtos são criados sozinhos, e o programa pede o cadastro do primeiro administrador.

## Demonstração

```
Você é:
[1] Administrador
[2] Cliente
[0] Sair
```

Entrando como **Administrador**, é preciso logar antes de chegar no menu de produtos, clientes e relatórios. Entrando como **Cliente**, dá para se cadastrar e, depois de logar com CPF e senha, realizar a compra.

## Conceitos aplicados

- **Orientação a Objetos:** quatro classes (`Produto`, `Cliente`, `Admin`, `Venda`) com `__init__`, `__str__` e métodos que alteram estado — como `ajuste(self, ajustar)`, que bloqueia estoque negativo
- **Encapsulamento com `@property` e setters:** o `Cliente` valida dentro do próprio setter, então um dado inválido nunca chega a virar atributo válido
- **Validação de CPF pelos dígitos verificadores** (cálculo dos dois dígitos e rejeição de sequências repetidas), não só a contagem de caracteres — e limpeza da entrada, aceitando CPF com ponto e traço
- **SQLite:** `CREATE TABLE IF NOT EXISTS`, `INSERT`, `SELECT`, `UPDATE` e `DELETE` mirando a linha certa com `WHERE id = ?`
- **Queries parametrizadas (`?`)** em vez de concatenar string — defesa contra SQL injection
- **`cursor.rowcount`** para detectar operação sobre `id` que não existe, já que SQL não levanta exceção nesse caso
- **Ponte linha ↔ objeto:** o `SELECT` devolve tupla e o `carregar_produtos` remonta cada uma como `Produto`; no JSON dos clientes acontece o mesmo caminho entre objeto e dicionário
- **`try/finally`** para garantir que a conexão com o banco feche mesmo se a operação falhar
- **Cópia do dado na venda:** o item guarda nome e preço copiados do produto, então apagar um produto depois não quebra o relatório antigo
- Separação de responsabilidades em módulos, tratamento de exceções e laços de validação que repetem até a entrada ser válida

## Próximos passos

- Persistir as vendas no SQLite, em duas tabelas (`vendas` e `itens_venda`) ligadas por chave estrangeira — hoje o estoque baixa no banco, mas o registro da venda some ao fechar o programa
- Migrar os clientes do JSON para o banco
- Persistir os administradores
- Guardar as senhas com hash em vez de texto puro
- Testes automatizados com `pytest`
