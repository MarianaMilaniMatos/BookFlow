from model import BibliotecaModel, UsuarioModel

#O controller vai utilizar os métodos do model para manipular os dados e fornecer à view (app.py)
class BibliotecaController: 
    def __init__(self): 
        self.model = BibliotecaModel() # self.model é um atributo, BibliotecaModel() é a classe do model.py
        self.usuario_model = UsuarioModel()
        # Quando atribuímos uma classe a um atributo, o atributo possui todos os métodos e atributos da classe

    # Adiciona um item ao modelo
    def adicionar_item(self, categoria, nome, autor, edicao): 
        self.model.adicionar_item(categoria, nome, autor, edicao) # chama o método adicionar_item da classe BibliotecaModel

    # Retorna os itens disponíveis
    def obter_disponiveis(self):
        return self.model.listar_disponiveis() # aqui estamos chamando o método listar_disponiveis da classe BibliotecaModel

    # Retorna os itens emprestados
    def obter_emprestados(self):
        return self.model.listar_emprestados()

    # Remove um item pelo índice
    def remover_item(self, indice):
        self.model.remover_item(indice)

    # Empresta um item pelo índice
    def emprestar_item(self, indice, dias=7):
        self.model.emprestar_item(indice, dias)

    # Devolve um item pelo índice
    def devolver_item(self, indice):
        self.model.devolver_item(indice)
    
    # Autentica um usuário
    def autenticar_usuario(self, usuario, senha):
        return self.usuario_model.autenticar(usuario, senha)
        


