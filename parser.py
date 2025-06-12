
import argparse

def set_parser_arg():

    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="Nome do arquivo a ser lido")
    parser.add_argument("--start",type=str, help="Intervalo de início da data de filtro, formato: YYYY-MM-DD", default=None)
    parser.add_argument("--end", type=str, help="Intervalo de final da data de filtro, formato: YYYY-MM-DD", default=None)
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Seleção do formato de saída")
    args = parser.parse_args()

    return args