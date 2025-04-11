from produto import Produto

class Estoque:
    def __init__(self):
        self.__produtos = []


    #getter e setters
    #produtos
    def get_produtos(self):
        return self.__produtos 
    
    def set_produtos(self, nova_lista):
        if isinstance(nova_lista, list):
            self.__produtos = nova_lista
        else:
            raise TypeError("A nova lista de produtos deve ser uma lista válida.")
        
    def adicionar_produto(self,produto):
        if isinstance(produto, Produto):
            self.__produtos.append(produto)
            print(f"Produto {produto.get_nome()} adicionado ao estoque com sucesso!")
        else:
            raise TypeError("O item adicionado deve ser uma instância da classe Produto.")
        

    # Usa get_codigo() para comparar, se o produto for encontrado e tiver estoque suficiente, reduz, Caso contrário levanta erro com raise.
    def remover_produto_por_codigo(self, codigo: str, quantidade: int):
        for produto in self.__produtos:
            if produto.get_codigo() == codigo:
                if produto.get_quantidade() >= quantidade:
                    produto.set_quantidade(produto.get_quantidade() - quantidade)
                    print(f"{quantidade} unidades do produto {codigo} removidas do estoque.")
                    return
                else:
                    raise ValueError(f"Estoque insuficiente para o produto {codigo}. Quantidade disponível: {produto.get_quantidade()}")
        raise ValueError(f"Produto com código {codigo} não encontrado.")


    # Usa o método anterior (remover_produto_por_codigo) para cada item. Trata exceções caso haja erro em algum item da venda.
    def baixar_estoque_por_venda(self, vendas: list):
        for codigo, quantidade in vendas:
            try:
                self.remover_produto_por_codigo(codigo, quantidade)
            except ValueError as e:
                print(f"Erro ao baixar estoque: {e}")

    #Usa apenas os getters e um for simples para mostrar tudo.
    def resumo_estoque(self):
        print("\n=== RESUMO DO ESTOQUE ===")
        for produto in self.__produtos:
            print(f"{produto.get_nome()} ({produto.get_codigo()}): {produto.get_quantidade()} unidades")


    #Simples if para checar o estoque de cada item, exibe apenas os que estão com estoque crítico (≤10).
    def verificar_alerta_estoque_baixo(self):
        print("\n=== ALERTAS DE ESTOQUE BAIXO ===")
        for produto in self.__produtos:
            if produto.get_quantidade() <= 10:
                print(f"ALERTA: {produto.get_nome()} ({produto.get_codigo()}) está com baixo estoque: {produto.get_quantidade()} unidades")

    def listar_produtos(self):
        if not self.__produtos:
            print("Estoque vazio.")
            return
        for produto in self.__produtos:
            print(f"Produto: {produto.get_nome()}")
            print(f"  Código: {produto.get_codigo()}")
            print(f"  Quantidade: {produto.get_quantidade()}")
            print(f"  Preço: R${produto.get_preco():.2f}")
            print(f"  Validade: {produto.get_validade()}")
            print(f"  Sessão: {produto.get_sessao()}")
            print("-" * 30)
