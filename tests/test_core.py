from core import get_total_sales

mock_unified_list =  [{'produto': 'Camiseta', 'quantidade': 4, 'preco_unitario': 49.9}, 
                              {'produto': 'Calça', 'quantidade': 2, 'preco_unitario': 99.9}, 
                              {'produto': 'Tênis', 'quantidade': 1, 'preco_unitario': 199.9}]

mock_total_sales_list = [{'produto': 'Camiseta', 'quantidade': 4, 'preco_unitario': 49.9, 'total_em_vendas': 199.6}, 
                              {'produto': 'Calça', 'quantidade': 2, 'preco_unitario': 99.9, 'total_em_vendas': 199.8}, 
                              {'produto': 'Tênis', 'quantidade': 1, 'preco_unitario': 199.9, 'total_em_vendas': 199.9}]

mock_total_sales_two_equal_quantity =  [{'produto': 'Camiseta', 'quantidade': 2, 'preco_unitario': 49.9, 'total_em_vendas': 199.6}, 
                              {'produto': 'Calça', 'quantidade': 2, 'preco_unitario': 99.9, 'total_em_vendas': 199.8}, 
                              {'produto': 'Tênis', 'quantidade': 1, 'preco_unitario': 199.9, 'total_em_vendas': 199.9}]

mock_total_sales_all_equal_quantity =  [{'produto': 'Camiseta', 'quantidade': 2, 'preco_unitario': 49.9, 'total_em_vendas': 99.8}, 
                              {'produto': 'Calça', 'quantidade': 2, 'preco_unitario': 99.9, 'total_em_vendas': 199.8}, 
                              {'produto': 'Tênis', 'quantidade': 2, 'preco_unitario': 199.9, 'total_em_vendas': 399.8}]

# Total de vendas de produto
data_list, produto, soma_do_total_de_vendas = get_total_sales(mock_unified_list)
_, produto_two_equal_quantity, _ = get_total_sales(mock_total_sales_two_equal_quantity)
_, produto_all_equal_quantity, _ = get_total_sales(mock_total_sales_all_equal_quantity)

def test_get_total_sales_value():
    assert data_list == mock_total_sales_list

def test_get_total_sales_most_selled_product():
    assert produto == ['Camiseta']

def test_get_total_sales_two_equal_quantity():
    assert produto_two_equal_quantity == ['Camiseta', 'Calça']

def test_get_total_sales_all_equal_quantity():
    assert produto_all_equal_quantity == ['Camiseta', 'Calça', 'Tênis']

def test_get_total_sales_sum_of_total_sales():
    assert soma_do_total_de_vendas == 599.3
