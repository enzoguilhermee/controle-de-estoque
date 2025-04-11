from produto import Produto
from fornecedor import Fornecedor
from estoque import Estoque

# Criando fornecedores
fornecedor1 = Fornecedor("Fornecedor A", "12345678000101", "fornecedorA@email.com", "899999999")
fornecedor2 = Fornecedor("Fornecedor B", "98765432000199", "fornecedorB@email.com", "999999999")

# Criando produtos
produto1 = Produto("Notebook", 15, 3500.00, "2025-12-31", "ELE", "ELE0001")
produto2 = Produto("Mouse", 25, 80.00, "2026-06-15", "INF", "INF0002")
produto3 = Produto("Teclado Mecânico", 10, 280, "2027-06-15", "INF", "INF0003")

# Criando o estoque
estoque = Estoque()

# Adicionando produtos ao estoque
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.adicionar_produto(produto3)

# Listando produtos no estoque
estoque.listar_produtos()

# Simulando uma venda
vendas = [
    (produto1.get_codigo(), 5),   # Vendendo 5 notebooks
    (produto2.get_codigo(), 12), # Vendendo 12 mouses
    (produto3.get_codigo(), 2)   # Vendendo 2 teclados mecânicos
]

print("\n==> Baixando estoque por venda...")
estoque.baixar_estoque_por_venda(vendas)

# Mostrando resumo do estoque
estoque.resumo_estoque()

# Verificando produtos com estoque baixo
estoque.verificar_alerta_estoque_baixo()
