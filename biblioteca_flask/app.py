from flask import Flask, render_template, request, redirect, url_for, session, flash
from controller import BibliotecaController

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para sessões
controller = BibliotecaController()

# Usuário e senha fixos para exemplo
USUARIO = 'admin'
SENHA = '1234'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if controller.autenticar_usuario(usuario, senha):
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route("/")
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    disponiveis = controller.obter_disponiveis()
    emprestados = controller.obter_emprestados()
    return render_template("index.html", disponiveis=disponiveis, emprestados=emprestados)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    nome = request.form["nome"]
    autor = request.form["autor"]
    edicao = request.form["edicao"]
    categoria = request.form["categoria"]
    controller.adicionar_item(categoria, nome, autor, edicao)
    return redirect(url_for("index"))

@app.route("/remover/<int:indice>", methods=["POST"])
def remover(indice):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    controller.remover_item(indice)
    return redirect(url_for("index"))

@app.route("/emprestar/<int:indice>", methods=["POST"])
def emprestar(indice):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    dias = int(request.form.get("dias", 7))
    controller.emprestar_item(indice, dias)
    return redirect(url_for("index"))

@app.route("/devolver/<int:indice>", methods=["POST"])
def devolver(indice):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    controller.devolver_item(indice)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)