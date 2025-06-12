# python_cli_project

Aplicação CLI de relatório de vendas. Detalhes sobre o desafio descritos no item Referência

## Sumário
- [Requisitos](#requisitos)
- [Rodando a aplicação](#rodando-a-aplicação)
- [Referência](#referência)

## Requisitos

As seguintes bibliotecas foram utilizadas:

- colorama==0.4.6
- iniconfig==2.1.0
- numpy==2.3.0
- packaging==25.0
- pluggy==1.6.0
- Pygments==2.19.1
- pytest==8.4.0
- python-cli==0
- python-dateutil==2.9.0.post0
- pytz==2025.2
- six==1.17.0
- tzdata==2025.2

Uma vez você tendo o pip em sua máquina realize o seguinte comando:

```bash
pip install -r requirements.txt
```

## Rodando a aplicação

Uma vez realizado a instalação dos pacotes para rodar o código realize os seguintes commandos:

```bash
pip install .
```

Se quiser ter uma informação de que comandos pode realizar faça  o comando:

```bash
vendas-cli -h
```

Você receberá as opções de execução


### usage: 
vendas-cli [-h] [--start START] [--end END] [--format {text,json}] filename

### positional arguments:
  filename              Nome do arquivo a ser lido

### options:
 -  -h, --help            show this help message and exit
 -  --start START         Intervalo de início da data de filtro, formato: YYYY-MM-DD
 - --end END             Intervalo de final da data de filtro, formato: YYYY-MM-DD
 - --format {text,json}  Seleção do formato de saída

Sabendo disso você pode executar comando como:

```bash
vendas-cli vendasexemplo-python.csv --format text
```
para obter os dados em tabela no terminal. Ou:

```bash
vendas-cli vendasexemplo-python.csv --format json
```

para obter os resultados em json.

## Referência

Desafio Python Sênior – Gerador de Relatório de Vendas Avançado

Descrição

Crie uma CLI em Python que processe um arquivo CSV de vendas e gere relatórios ricos, com foco
em qualidade de código, testes e boas práticas.

Funcionalidades obrigatórias
1. Leitura de CSV usando bibliotecas padrão (csv, argparse, logging).
 • Aceitar caminho do arquivo por parâmetro de linha de comando.
2. Cálculos principais:
 • Total de vendas por produto.
 • Valor total de todas as vendas.
 • Produto mais vendido.
3. Filtros e formatos de saída:
 • Parâmetros opcionais para filtrar por data de venda (intervalo).
 • Saída em texto formatado (tabela) ou JSON (--format text|json).

Requisitos de qualidade
• Tipagem estática com typing.
• Estrutura modular (mínimo 2–3 módulos: parser, core, output).
• Tratamento de erros e logs claros (logging).
• CLI instalável via setup.py ou pyproject.toml (comando vendas-cli).
• Testes unitários (pytest) cobrindo ao menos 80% do código.

Exemplo de uso
$ pip install .
$ vendas-cli vendas.csv --format text
$ vendas-cli vendas.csv --format json --start 2025-01-01 --end 2025-03-31

Entrega
• Repositório público no GitHub com código-fonte organizado.
• README.md com instruções de instalação e uso.
• Arquivo de configuração de testes (pytest.ini ou similar)
• Tempo estimado: até 2 horas.



Precisa Rodar n vezes para registrar
Precisa garantir que registro de data seja no formato especificado.
