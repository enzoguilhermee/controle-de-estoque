from produto import Produto
from fornecedor import Fornecedor
from estoque import Estoque
from caixa import Caixa

# Criando fornecedores
fornecedor1 = Fornecedor("Fornecedor A", "12345678000101", "fornecedorA@email.com", "899999999")
fornecedor2 = Fornecedor("Fornecedor B", "98765432000199", "fornecedorB@email.com", "999999999")

# Criando produtos
produto1 = Produto("Notebook", 15, 3500.00, "2025-12-31", "ELE", "ELE0001")
produto2 = Produto("Mouse", 25, 80.00, "2026-06-15", "INF", "INF0002")
produto3 = Produto("Teclado Mecânico", 10, 280.00, "2027-06-15", "INF", "INF0003")

# Criando e configurando estoque
estoque = Estoque()
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.adicionar_produto(produto3)

# Criando e configurando caixa
caixa = Caixa(estoque)

# Listando produtos no estoque
print("\n=== ESTOQUE INICIAL ===")
for p in estoque.get_produtos():
    if isinstance(p, Produto):  # Garantindo que é um Produto
        p.exibir_dados()

# Abrindo o caixa e processando vendas
print("\n==> ABRINDO CAIXA E PROCESSANDO VENDAS...")
caixa.abrir_caixa()

vendas = [
    {'codigo': 'ELE0001', 'quantidade': 5},
    {'codigo': 'INF0002', 'quantidade': 12},
    {'codigo': 'INF0003', 'quantidade': 2}
]

caixa.finalizar_compra(vendas)

# Fechando caixa e exibindo resumo
print("\n==> FECHANDO CAIXA...")
resumo = caixa.fechar_caixa()

# Exibindo estoque atualizado
print("\n=== ESTOQUE APÓS VENDAS ===")
for p in estoque.get_produtos():
    if isinstance(p, Produto):  # Garantindo que é um Produto
        p.exibir_dados()

# Exibindo alertas de estoque baixo
print("\n=== ALERTAS DE ESTOQUE ===")
caixa.emitir_alerta_estoque_baixo()

# Exibindo resumo financeiro
print("\n=== RESUMO FINANCEIRO ===")
print(f"Total de itens vendidos: {resumo['total_itens']}")
print(f"Valor total vendido: R${resumo['total_valor']:.2f}")
print("Detalhes das vendas:")
for i, venda in enumerate(resumo['vendas'], 1):
    print(f"\nVenda {i}:")
    for item in venda['itens']:
        print(f" - {item['nome']} ({item['codigo']}): {item['quantidade']}x R${item['preco_unitario']:.2f} = R${item['total']:.2f}")

