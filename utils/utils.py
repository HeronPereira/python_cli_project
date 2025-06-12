import csv
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_csv_file(filename: str) -> List[Dict[str,str]]:
    try:  
        with open(file=filename, newline='') as f:
            dict_reader = csv.DictReader(f)
            list_data = list(dict_reader)
            return list_data
    except Exception as e:
        logging.error("File not found!")
        return []

def unify_items(data: List[Dict[str,str]]) -> List[Dict[str,str]]:
    unified_items = {}
    for d in data:
        if d['produto'] not in unified_items:
            unified_items[d['produto']] = {
                'produto': d['produto'],
                'quantidade': int(d['quantidade']),
                'preco_unitario': float(d['preco_unitario'])
            }
        else:
            unified_items[d['produto']]['quantidade'] += int(d['quantidade'])
    unified_items_list = list(unified_items.values())
    
    return unified_items_list