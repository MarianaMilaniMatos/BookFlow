from datetime import datetime, timedelta

# Superclasse (Generalização)
class ItemBiblioteca:
    def __init__(self, nome, autor, edicao, categoria):
        self.nome = nome
        self.autor = autor
        self.edicao = edicao
        self.categoria = categoria
        self.data_devolucao = None # none = disponível, em caso de emprestado, guarda a data de devolução

    def emprestar(self, dias=7): #dias=7 é o padrão
        self.data_devolucao = datetime.now() + timedelta(days=dias) # define a data de devolução (hoje + dias)

    def devolver(self):
        self.data_devolucao = None # marca como disponível

    def esta_emprestado(self):
        return self.data_devolucao is not None # return self.data_devolucao is not None= verifica se está emprestado

    # Polimorfismo → será sobrescrito nas subclasses
    def descricao(self):
        return f"{self.nome} ({self.categoria}) - {self.autor}, Edição {self.edicao}"


# Subclasses (Especificação)
class Livro(ItemBiblioteca):
    def __init__(self, nome, autor, edicao):
        super().__init__(nome, autor, edicao, "Livro") # super() chama o construtor da superclasse, (nome, autor, edicao, "Livro") são os parâmetros

    def descricao(self):
        return f"📖 Livro: {self.nome} - {self.autor} ( {self.edicao} Edição )"


class Manga(ItemBiblioteca):
    def __init__(self, nome, autor, edicao):
        super().__init__(nome, autor, edicao, "Mangá")

    def descricao(self):
        return f"🍥 Mangá: {self.nome} - {self.autor} (Vol. {self.edicao})"


class Quadrinho(ItemBiblioteca):
    def __init__(self, nome, autor, edicao):
        super().__init__(nome, autor, edicao, "Quadrinho")

    def descricao(self):
        return f"🦸 Quadrinho: {self.nome} - {self.autor} (Edição {self.edicao})"


# Modelo principal de armazenamento dos itens
class BibliotecaModel:
    def __init__(self):
        self.itens_disponiveis = [] # lista de itens disponíveis
        self.itens_emprestados = [] # lista de itens emprestados

    def adicionar_item(self, categoria, nome, autor, edicao):
        if categoria == "Livro":
            novo_item = Livro(nome, autor, edicao) #cria um objeto da classe Livro
        elif categoria == "Mangá":
            novo_item = Manga(nome, autor, edicao)
        elif categoria == "Quadrinho":
            novo_item = Quadrinho(nome, autor, edicao)
        else:
            raise ValueError("Categoria inválida")

        self.itens_disponiveis.append(novo_item) # adiciona o novo item à lista de disponíveis

    def listar_disponiveis(self):
        return self.itens_disponiveis

    def listar_emprestados(self):
        return self.itens_emprestados

    def remover_item(self, indice): # indice é a posição do item na lista (indice=0 é o primeiro item)
        if 0 <= indice < len(self.itens_disponiveis): #se o indice for maior ou igual a 0 e menor que o tamanho da lista de disponíveis, remove o item da lista
            self.itens_disponiveis.pop(indice) # pop() remove o item da lista pelo índice

    def emprestar_item(self, indice, dias=7):
        if 0 <= indice < len(self.itens_disponiveis):
            item = self.itens_disponiveis.pop(indice) # remove o item da lista de disponíveis e guarda na variável item
            item.emprestar(dias) # marca o item como emprestado
            self.itens_emprestados.append(item) # adiciona o item à lista de emprestados

    def devolver_item(self, indice):
        if 0 <= indice < len(self.itens_emprestados):
            item = self.itens_emprestados.pop(indice) # remove o item da lista de emprestados e guarda na variável item
            item.devolver() #marca o item como disponível
            self.itens_disponiveis.append(item) # adiciona o item à lista de disponíveis

class UsuarioModel:
    def __init__(self):
        # Usuário e senha fixos para exemplo
        self.usuario = 'admin'
        self.senha = '1234'

    def autenticar(self, usuario, senha):
        return usuario == self.usuario and senha == self.senha