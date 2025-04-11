from produto import Produto

class Caixa:
    def __init__(self, estoque):
        self.__estoque = estoque
        self.__caixa_aberto = False
        self.__vendas = []

    def abrir_caixa(self):
        if self.__caixa_aberto:
            print("O caixa já está aberto.")
            return
        self.__caixa_aberto = True
        self.__vendas = []
        print("Caixa aberto com sucesso.")

    def fechar_caixa(self):
        if not self.__caixa_aberto:
            print("O caixa já está fechado.")
            return
        
        self.__caixa_aberto = False
        resumo = self.__gerar_resumo_vendas()
        print("\n--- Resumo de Vendas do Dia ---")
        print(f"Total de itens vendidos: {resumo['total_itens']}")
        print(f"Valor total: R${resumo['total_valor']:.2f}")
        print("-------------------------------")
        self.__vendas = []
        return resumo

    def finalizar_compra(self, itens):
        if not self.__caixa_aberto:
            raise Exception("Erro: Caixa fechado. Abra o caixa para finalizar compras.")
        
        venda = {
            'itens': [],
            'total': 0
        }

        for item in itens:
            codigo = item['codigo']
            quantidade = item['quantidade']
            
            produto = self.__buscar_produto_por_codigo(codigo)
            if not produto:
                print(f"Produto com código {codigo} não encontrado. Item ignorado.")
                continue

            if produto.get_quantidade() < quantidade:
                print(f"Estoque insuficiente para {produto.get_nome()}. Item ignorado.")
                continue

            # Atualiza estoque
            nova_quantidade = produto.get_quantidade() - quantidade
            produto.set_quantidade(nova_quantidade)

            # Verifica alerta
            if nova_quantidade <= 10:
                print(f"ALERTA: {produto.get_nome()} está com apenas {nova_quantidade} unidades em estoque!")

            # Registra item na venda
            total_item = quantidade * produto.get_preco()
            venda_item = {
                'codigo': codigo,
                'nome': produto.get_nome(),
                'quantidade': quantidade,
                'preco_unitario': produto.get_preco(),
                'total': total_item
            }
            venda['itens'].append(venda_item)
            venda['total'] += total_item

        if venda['itens']:
            self.__vendas.append(venda)
            print("Compra finalizada com sucesso!")
        else:
            print("Nenhum item válido para finalizar a compra.")

    def __buscar_produto_por_codigo(self, codigo):
        for produto in self.__estoque.get_produtos():
            if produto.get_codigo() == codigo:
                return produto
        return None

    def __gerar_resumo_vendas(self):
        total_itens = sum(sum(item['quantidade'] for item in venda['itens']) for venda in self.__vendas)
        total_valor = sum(venda['total'] for venda in self.__vendas)
        return {
            'total_itens': total_itens,
            'total_valor': total_valor,
            'vendas': self.__vendas.copy()
        }

    def emitir_alerta_estoque_baixo(self):
        alertas = []
        for produto in self.__estoque.get_produtos():
            if produto.get_quantidade() <= 10:
                alertas.append(produto)
        
        if alertas:
            print("\n--- Alertas de Estoque Baixo ---")
            for produto in alertas:
                print(f"{produto.get_codigo()} - {produto.get_nome()} ({produto.get_quantidade()} unidades)")
            print("-------------------------------")
        else:
            print("Nenhum alerta de estoque baixo.")
