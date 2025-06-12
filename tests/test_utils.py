from utils.utils import get_csv_file, unify_items, validate_date, validate_date_range, get_items_in_date_range

mock_list = [{'produto': 'Camiseta', 'quantidade': '3', 'preco_unitario': '49.9'}, 
                              {'produto': 'Calça', 'quantidade': '2', 'preco_unitario': '99.9'}, 
                              {'produto': 'Camiseta', 'quantidade': '1', 'preco_unitario': '49.9'}, 
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9'}]

mock_list_with_date =  [{'produto': 'Camiseta', 'quantidade': '3', 'preco_unitario': '49.9', 'data':'2020-01-01'}, 
                              {'produto': 'Calça', 'quantidade': '2', 'preco_unitario': '99.9', 'data':'2021-01-01'}, 
                              {'produto': 'Camiseta', 'quantidade': '1', 'preco_unitario': '49.9', 'data':'2022-01-10'}, 
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2023-02-28'},
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2023-03-28'},
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2024-12-10'},
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2024-12-12'}]

mock_list_2021_2022 = [{'produto': 'Calça', 'quantidade': '2', 'preco_unitario': '99.9', 'data':'2021-01-01'}, 
                              {'produto': 'Camiseta', 'quantidade': '1', 'preco_unitario': '49.9', 'data':'2022-01-10'}]

mock_list_2023_02_2023_03 = [{'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2023-02-28'},
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2023-03-28'}]

mock_list_2024_12_10_2024_12_12 = [ {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2024-12-10'},
                              {'produto': 'Tênis', 'quantidade': '1', 'preco_unitario': '199.9', 'data':'2024-12-12'}]

unified_list =  [{'produto': 'Camiseta', 'quantidade': 4, 'preco_unitario': 49.9}, 
                              {'produto': 'Calça', 'quantidade': 2, 'preco_unitario': 99.9}, 
                              {'produto': 'Tênis', 'quantidade': 1, 'preco_unitario': 199.9}]


def test_start_must_be_bigger_than_end_right():
    assert validate_date_range('2025-06-12', '2025-06-13') == True


def test_start_must_be_bigger_than_end_wrong():
    assert validate_date_range('2025-06-14', '2025-06-13') == False

def test_range_date_by_year():
    assert get_items_in_date_range(mock_list_with_date, '2021-01-01','2022-12-31') == mock_list_2021_2022

def test_range_date_by_month():
    assert get_items_in_date_range(mock_list_with_date, '2023-02-01','2023-03-30') == mock_list_2023_02_2023_03


def test_range_date_by_day():
    assert get_items_in_date_range(mock_list_with_date, '2024-12-01','2024-12-31') == mock_list_2024_12_10_2024_12_12

def test_validate_date_right():
    assert validate_date("2025-06-12") == True

def test_validate_date_wrong_slash():
    assert validate_date("2025/06/12") == False

def test_validate_date_wrong_inverted():
    assert validate_date("12-06-2025") == False

def test_get_csv_file_correct_file():
    assert get_csv_file("vendasexemplo-python.csv") == mock_list

def test_get_csv_file_wrong_name():
    assert get_csv_file("foo.csv") == []

def test_unificar_items():
    assert unify_items(mock_list) == unified_list

def test_unificar_items_without_repetition():
    assert unify_items(unified_list) == unified_list