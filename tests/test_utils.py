from utils.utils import get_csv_file, unify_items

mock_list = [{'produto': 'Camiseta', 'quantidade': '3', 'preco_unitario': '49.9'}, 
                              {'produto': 'Calça', 'quantidade': '2', 'preco_unitario': '99.9'}, 
                              {'produto': 'Camiseta', 'quantidade': '1', 'preco_unitario': '49.9'}, 
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9'}]

unified_list =  [{'produto': 'Camiseta', 'quantidade': 4, 'preco_unitario': 49.9}, 
                              {'produto': 'Calça', 'quantidade': 2, 'preco_unitario': 99.9}, 
                              {'produto': 'Tênis', 'quantidade': 1, 'preco_unitario': 199.9}]

def test_get_csv_file_correct_file():
    assert get_csv_file("vendasexemplo-python.csv") == mock_list

def test_get_csv_file_wrong_name():
    assert get_csv_file("foo.csv") == []

def test_unificar_items():
    assert unify_items(mock_list) == unified_list

def test_unificar_items_without_repetition():
    assert unify_items(unified_list) == unified_list