class Sessao:
    def __init__(self, nome, descricao=""):
        self.__nome = nome
        self.__descricao = descricao
        self.__produtos = []

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
        print(f"Produto '{produto.get_nome()}' adicionado à sessão '{self.__nome}'.")

    def remover_produto(self, codigo):
        for produto in self.__produtos:
            if produto.get_codigo() == codigo:
                self.__produtos.remove(produto)
                print(f"Produto '{produto.get_nome()}' removido da sessão '{self.__nome}'.")
                return
        print(f"Nenhum produto com código '{codigo}' encontrado na sessão '{self.__nome}'.")

    def listar_produtos(self):
        if not self.__produtos:
            print(f"A sessão '{self.__nome}' está vazia.")
            return
        print(f"\nProdutos na sessão '{self.__nome}':")
        for produto in self.__produtos:
            print(f"{produto.get_codigo()} - {produto.get_nome()} ({produto.get_quantidade()} unidades)")

