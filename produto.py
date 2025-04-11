class Produto:
    def __init__(self, nome, quantidade, preco, validade, sessao, codigo):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco
        self.__validade = validade
        self.__sessao = sessao
        self.__codigo = codigo

# os atributos estão encapsulados com __, pois não poderão ser acessados diretamente de fora da classe, além de que a adição do parâmetro de código será necessário para definir a categoria do produto, sessão e ordem de cadastro. 

#métodos getters e setters
    #nome 
    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    #quantidade
    def get_quantidade(self):
        return self.__quantidade
    
    def set_quantidade(self,nova_quantidade): #tratamento de erro de quantidade com raise no método setter da quantidade
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            raise ValueError("Quantidade não pode ser negativa.")

    #preco
    def get_preco(self):
        return self.__preco
    
    def set_preco(self,novo_preco): #tratamento de erro de preço com raise no método setter do preço
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            raise ValueError("Preço não pode ser negativo.")
        
    #validade    
    def get_validade(self):
        return self.__validade
    
    def set_validade(self, nova_validade):
        self.__validade = nova_validade

    #sessao
    def get_sessao(self):
        return self.__sessao
    
    def set_sessao(self, nova_sessao):
        self.__sessao = nova_sessao

    #código
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    def exibir_dados(self):
        print(f"{self.__codigo} - {self.__nome}")
        print(f"Quantidade: {self.__quantidade}")
        print(f"Preço: R${self.__preco:.2f}")
        print(f"Validade: {self.__validade}")
        print(f"Seção: {self.__sessao}")
        print()



    
        
