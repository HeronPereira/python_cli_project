import json
import logging
from typing import List, Dict, Tuple, Any



def get_table(data: List[Dict[str, Any]], mais_vendido: List[str], total_em_vendas: float):
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    logging.info('------------------------------------Relatório de vendas-------------------------------------')
    logging.info('--------------------------------------------------------------------------------------------')
    for d in data:
        logging.info('| produto : ' + str(d['produto']) + 
                     ' | quantidade : ' + str(d['quantidade']) + 
                     ' | preço unitário : ' + str(d['preco_unitario']) + 
                     ' | total de vendas : ' + str(d['total_em_vendas']) + ' |')
        
        logging.info('--------------------------------------------------------------------------------------------')
    
    logging.info('--------------------------------------------------------------------------------------------')
    logging.info('--------------------------------------------------------------------------------------------')
    logging.info('| ITEM MAIS VENDIDO (R$) : ' + str(mais_vendido) + '|')
    logging.info('| SOMATÓRIO DO TOTAL EM VENDAS (R$) : ' + str(total_em_vendas) + '|') 
    logging.info('--------------------------------------------------------------------------------------------')

def get_json(data: List[Dict[str, Any]], mais_vendido: List[str], total_em_vendas: float):
    data_completed = {}

    data_completed['items'] = data
    data_completed['item_mais_vendido'] = mais_vendido
    data_completed['soma_total_de_vendas'] = total_em_vendas

    return json.dumps(data_completed)