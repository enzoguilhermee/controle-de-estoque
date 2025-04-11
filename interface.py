import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog, messagebox
from produto import Produto
from estoque import Estoque
from caixa import Caixa
from fornecedor import Fornecedor
from datetime import datetime

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas - Tkinter Estilizado")
        self.root.geometry("650x600")

        # Simulação de usuários
        self.usuarios = {"admin": "1234"}

        # Dados
        self.estoque = Estoque()
        self.caixa = Caixa(self.estoque)
        self.fornecedores = []
        self.tela_login()

    def tela_login(self):
        self.clear_window()

        # Frame centralizado
        login_frame = ttk.Frame(self.root)
        login_frame.pack(expand=True)

        ttk.Label(login_frame, text="Login", font=("Arial", 20)).pack(pady=20)

        self.user_entry = ttk.Entry(login_frame, width=30)
        self.user_entry.pack(pady=10)
        self.user_entry.insert(0, "admin")

        self.pass_entry = ttk.Entry(login_frame, width=30, show="*")
        self.pass_entry.pack(pady=5)

        ttk.Button(login_frame, text="Entrar", bootstyle="primary", width=20, command=self.verificar_login).pack(pady=20)


    def verificar_login(self):
        user = self.user_entry.get()
        senha = self.pass_entry.get()
        if self.usuarios.get(user) == senha:
            self.tela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def tela_principal(self):
        self.clear_window()
    
        # Criar frame central para os elementos
        frame_principal = ttk.Frame(self.root)
        frame_principal.pack(expand=True)
    
        ttk.Label(frame_principal, text="Painel Principal", font=("Arial", 18)).pack(pady=10)
    
        botoes = [
            ("Abrir Caixa", self.abrir_caixa, "success"),
            ("Fechar Caixa", self.fechar_caixa, "danger"),
            ("Adicionar Produto", self.adicionar_produto, "info"),
            ("Listar Estoque", self.listar_estoque, "light"),
            ("Filtrar por Sessão", self.filtrar_por_sessao, "light"),
            ("Filtrar por Validade", self.filtrar_por_validade, "light"),
            ("Realizar Venda", self.realizar_venda, "warning"),
            ("Resumo de Vendas", self.resumo_vendas, "secondary"),
            ("Cadastrar Fornecedor", self.cadastrar_fornecedor, "info"),
            ("Listar Fornecedores", self.listar_fornecedores, "light"),
            ("Sair", self.tela_login, "dark")
        ]
    
        for texto, comando, estilo in botoes:
            ttk.Button(frame_principal, text=texto, bootstyle=estilo, width=30, command=comando).pack(pady=4)


    def abrir_caixa(self):
        self.caixa.abrir_caixa()
        return messagebox.showinfo("Seja bem-vindo(a)!", "Caixa aberto com sucesso!")
    def fechar_caixa(self):
        self.caixa.fechar_caixa()
        return messagebox.showinfo("Volte sempre!", "Caixa fechado com sucesso!")
    def adicionar_produto(self):
        try:
            nome = simpledialog.askstring("Produto", "Nome do produto:")
            preco = float(simpledialog.askstring("Produto", "Preço:"))
            quantidade = int(simpledialog.askstring("Produto", "Quantidade:"))
            validade = simpledialog.askstring("Produto", "Validade (YYYY-MM-DD):")
            sessao = simpledialog.askstring("Produto", "Sessão (ex: Laticínios, Grãos):")

            produto = Produto(nome, preco, quantidade, validade, sessao)
            self.estoque.adicionar_produto(produto)
            messagebox.showinfo("Sucesso", f"Produto {nome} adicionado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar_estoque(self):
        produtos = self.estoque.listar_produtos()
        info = "\n".join([
            f"{p.get_codigo()} - {p.get_nome()} - {p.get_sessao()} - {p.get_validade()} ({p.get_quantidade()} un.)"
            for p in produtos.values()
        ])
        messagebox.showinfo("Estoque", info or "Nenhum produto cadastrado.")

    def filtrar_por_sessao(self):
        sessao = simpledialog.askstring("Filtro", "Digite o nome da sessão:")
        filtrados = [
            p for p in self.estoque.listar_produtos().values()
            if p.get_sessao().lower() == sessao.lower()
        ]
        info = "\n".join([f"{p.get_codigo()} - {p.get_nome()} ({p.get_quantidade()} un.)" for p in filtrados]) or "Nenhum produto encontrado."
        messagebox.showinfo("Filtro por Sessão", info)

    def filtrar_por_validade(self):
        data_str = simpledialog.askstring("Filtro", "Exibir produtos com validade antes de (YYYY-MM-DD):")
        try:
            limite = datetime.strptime(data_str, "%Y-%m-%d").date()
            filtrados = [
                p for p in self.estoque.listar_produtos().values()
                if datetime.strptime(p.get_validade(), "%Y-%m-%d").date() < limite
            ]
            info = "\n".join([f"{p.get_codigo()} - {p.get_nome()} (Val: {p.get_validade()})" for p in filtrados]) or "Nenhum produto encontrado."
            messagebox.showinfo("Filtro por Validade", info)
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use YYYY-MM-DD.")

    def realizar_venda(self):
        codigos = simpledialog.askstring("Venda", "Digite os códigos dos produtos (ex: LAT0001,GRA0003):")
        quantidades = simpledialog.askstring("Venda", "Digite as quantidades (ex: 2,1):")

        try:
            lista_codigos = codigos.split(",")
            lista_quantidades = list(map(int, quantidades.split(",")))
            itens = list(zip(lista_codigos, lista_quantidades))
            self.caixa.realizar_venda(itens, self.estoque)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def resumo_vendas(self):
        vendas = self.caixa._Caixa__vendas_dia
        if not vendas:
            messagebox.showinfo("Vendas", "Nenhuma venda registrada hoje.")
            return

        texto = ""
        for venda in vendas:
            hora = venda["data"].strftime("%H:%M:%S")
            total = venda["total"]
            texto += f"Venda às {hora} - Total: R${total:.2f}\n"

        messagebox.showinfo("Resumo de Vendas", texto)

    def cadastrar_fornecedor(self):
        nome = simpledialog.askstring("Fornecedor", "Nome do fornecedor:")
        cnpj = simpledialog.askstring("Fornecedor", "CNPJ do fornecedor:")
        if nome and cnpj:
            fornecedor = Fornecedor(nome, cnpj)
            self.fornecedores.append(fornecedor)
            messagebox.showinfo("Sucesso", "Fornecedor cadastrado.")
        else:
            messagebox.showerror("Erro", "Nome e CNPJ são obrigatórios.")

    def listar_fornecedores(self):
        if not self.fornecedores:
            messagebox.showinfo("Fornecedores", "Nenhum fornecedor cadastrado.")
            return

        info = "\n".join([
            f"{f.get_nome()} - CNPJ: {f.get_cnpj()}" for f in self.fornecedores
        ])
        messagebox.showinfo("Fornecedores", info)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Execução
if __name__ == "__main__":
    app = ttk.Window(themename="darkly")  # Você pode trocar o tema aqui (cosmo, darkly, flatly, etc)
    Aplicacao(app)
    app.mainloop()
