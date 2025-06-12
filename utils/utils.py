import csv
import logging
from typing import List, Dict
from datetime import datetime

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

def validate_date(date: str) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_date_range(start: str, end: str) -> bool:
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    if start_date < end_date:
        return True
    else:
        return False


def get_items_in_date_range(data: List[Dict[str,str]], start, end) -> List[Dict[str,str]]:
    
    selected_items = []
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d") 
    for d in data:
        d_date = datetime.strptime(d['data'], '%Y-%m-%d')

        if d_date >= start_date and d_date <= end_date:
            selected_items.append(d)

    return selected_items


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