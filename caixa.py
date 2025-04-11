class Caixa:
    def __init__(self, estoque):
        self.__estoque = estoque
        self.__caixa_aberto = False
        self.__vendas = []


    def is_caixa_aberto(self):
        return self.__caixa_aberto

    
    def abrir_caixa(self):
        if self.__caixa_aberto:
            print("O caixa já está aberto.")
            return False
        self.__caixa_aberto = True
        self.__vendas = []
        print("Caixa aberto com sucesso.")
        return True
    
    def fechar_caixa(self):
        if not self.__caixa_aberto:
            print("O caixa já está fechado.")
            return
        
        self.__caixa_aberto = False
        resumo = self.__gerar_resumo_vendas()
        self.__exibir_resumo_vendas(resumo)
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

            estoque_atual = produto.get_quantidade()
            nome = produto.get_nome()
            preco = produto.get_preco()

            if estoque_atual < quantidade:
                print(f"Estoque insuficiente para {nome}. Item ignorado.")
                continue

            # Atualiza estoque
            nova_quantidade = estoque_atual - quantidade
            produto.set_quantidade(nova_quantidade)

            if nova_quantidade <= 10:
                print(f"ALERTA: {nome} está com apenas {nova_quantidade} unidades em estoque!")

            total_item = quantidade * preco
            venda['itens'].append({
                'codigo': codigo,
                'nome': nome,
                'quantidade': quantidade,
                'preco_unitario': preco,
                'total': total_item
            })
            venda['total'] += total_item

        if venda['itens']:
            self.__vendas.append(venda)
            print("Compra finalizada com sucesso!")
            return venda  # opcional: retorna a venda feita
        else:
            print("Nenhum item válido para finalizar a compra.")
            return None

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

    def __exibir_resumo_vendas(self, resumo):
        print("\n--- Resumo de Vendas do Dia ---")
        print(f"Total de itens vendidos: {resumo['total_itens']}")
        print(f"Valor total: R${resumo['total_valor']:.2f}")
        print("-------------------------------")

    def emitir_alerta_estoque_baixo(self):
        alertas = [
            produto for produto in self.__estoque.get_produtos()
            if produto.get_quantidade() <= 10
        ]
        
        if alertas:
            print("\n--- Alertas de Estoque Baixo ---")
            for produto in alertas:
                print(f"{produto.get_codigo()} - {produto.get_nome()} ({produto.get_quantidade()} unidades)")
            print("-------------------------------")
        else:
            print("Nenhum alerta de estoque baixo.")

    def desfazer_ultima_venda(self):
        if not self.__vendas:
            print("Nenhuma venda para desfazer.")
            return

        ultima_venda = self.__vendas.pop()
        for item in ultima_venda['itens']:
            produto = self.__buscar_produto_por_codigo(item['codigo'])
            if produto:
                produto.set_quantidade(produto.get_quantidade() + item['quantidade'])
        print("Última venda desfeita com sucesso.")
