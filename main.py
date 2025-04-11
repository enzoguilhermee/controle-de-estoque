from produto import Produto

def main():
    # Criando dois produtos
    produto1 = Produto("Manteiga", 50, 7.99, "2025-07-15", "Laticínios", "LAT0001")
    produto2 = Produto("Arroz", 120, 4.49, "2026-01-01", "Grãos", "GRA0001")

    # Exibindo dados dos produtos
    print("== PRODUTOS CADASTRADOS ==")
    produto1.exibir_dados()
    produto2.exibir_dados()

    # Modificando dados
    produto1.set_quantidade(45)
    produto1.set_preco(8.29)
    print("== PRODUTO 1 ATUALIZADO ==")
    produto1.exibir_dados()

    # Testando tratamento de erro
    try:
        produto2.set_quantidade(-10)
    except ValueError as e:
        print(f"Erro ao atualizar quantidade: {e}")

    # Verificando getters
    print(f"Nome do produto 2: {produto2.get_nome()}")
    print(f"Código do produto 2: {produto2.get_codigo()}")

if __name__ == "__main__":
    main()
