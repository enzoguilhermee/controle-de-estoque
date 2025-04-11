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