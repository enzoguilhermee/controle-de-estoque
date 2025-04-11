class Fornecedor:

    def __init__(self, nome, cnpj, email, telefone):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__email = email
        self.__telefone = telefone
        self.__produtos_fornecidos = [] #os produtos fornecidos serão armazenados numa lista


        #tratando possíveis riscos no formato da entrada de dados do fornecedor
        if not nome:
            raise ValueError("Nome do fornecedor não pode ser vazio.")
        if not cnpj or len(cnpj)<10:
            raise ValueError("CPNJ inválido, tente novamente!")
        if not telefone:
            raise ValueError("Telefone não pode ser vazio.")
        
    #getters e setters
    #nome 
    def get_nome(self):
        return self.__nome 
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    #cnpj
    def get_cnpj(self):
        return self.__cnpj

    def set_cnpj(self, cnpj): #tratamento de erro com raise para possível modificação de CPNJ inválido
        if not cnpj or len(cnpj) < 10:
            raise ValueError("CNPJ inválido.")
        self.__cnpj = cnpj

    #email
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    #telefone
    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, telefone):
        if not telefone:
            raise ValueError("Telefone não pode ser vazio.")
        self.__telefone = telefone

    #produtos fornecidos
    def get_produtos_fornecidos(self):
        return self.__produtos_fornecidos
    
    #Adiciona produto ao fornecedor
    def adicionar_produto(self, produto):
        if produto not in self.__produtos_fornecidos:
            self.__produtos_fornecidos.append(produto)

    #Exibe dados do fornecedor
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"CNPJ: {self.__cnpj}")
        print(f"Email: {self.__email}")
        print(f"Telefone: {self.__telefone}")
        print(f"Produtos fornecidos: {self.__produtos_fornecidos}")
        print("-" * 30)