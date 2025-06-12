from typing import List, Dict, Tuple

def get_total_sales(data: List[Dict[str,str]]) -> Tuple[List[Dict[str,str]], List[int], float]:
    mais_vendido = []
    soma_do_total_de_vendas = 0.0

    quantidade_do_mais_vendido = max(item['quantidade'] for item in data)

    for d in data:
        d["total_em_vendas"] = d['quantidade']*d['preco_unitario']
        soma_do_total_de_vendas += d['total_em_vendas']

        if d['quantidade'] == quantidade_do_mais_vendido:
            mais_vendido.append(d['produto'])

    return data, mais_vendido, soma_do_total_de_vendas