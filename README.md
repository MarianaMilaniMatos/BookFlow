# 📚 BookFlow

> Sistema para catalogar, gerenciar e acompanhar seus livros de forma organizada, utilizando MVC e Programação Orientada a Objetos.

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/flask-microframework-brightgreen)](https://flask.palletsprojects.com/)  
[![HTML5](https://img.shields.io/badge/html5-orange)](https://developer.mozilla.org/pt-BR/docs/Web/HTML)  
[![CSS3](https://img.shields.io/badge/css3-blue)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🎯 Sobre

BookFlow é uma aplicação web desenvolvida com **Python/Flask** que permite:

- 📚 Cadastrar livros com informações como título, autor, gênero e categoria.  
- 🔍 Listar todos os livros cadastrados.  
- ✏️ Editar dados de livros existentes.  
- 🗑 Remover livros indesejados.  
- 📚 Emprestar livros e calcular data de devolução

O objetivo é proporcionar uma interface simples, organizada e código bem estruturado, de fácil manutenção.

---

## 🧰 Tecnologias

| Tecnologia        | Finalidade                                 |
|-------------------|---------------------------------------------|
| Python            | Lógica de backend, manipulação de dados     |
| Flask             | Framework web para rotas, APIs e views      |
| HTML, CSS         | Interface, templates, estilo visual         |

---

## 🏛 Arquitetura MVC & POO

### MVC

- **Model**: Representam entidades como *Livro*, suas propriedades (ex: título, autor, status) e métodos relacionados (CRUD, validações).  
- **View**: Templates HTML (via Jinja2) exibindo páginas como lista de livros, formulário de cadastro/edição, detalhes etc.  
- **Controller**: Funções/rotas que recebem requisições, interagem com models, processam lógica de negócio, escolhem qual view renderizar ou redirecionar.

### Programação Orientada a Objetos (POO)

- **Classes** para representar entidades do domínio (ex: `Livro`).  
- Encapsulamento: atributos privados ou protegidos, uso de getters/setters se necessário.  
- Métodos nas classes para operações (ex: validar dados, representar estado, conversões se houver).  
- Possível reutilização / composição: se há código comum entre partes, abstrações.

---

## 📂 Estrutura do Projeto

```text
BookFlow/
├── biblioteca_flask/           # Código fonte da aplicação Flask
│   ├── models/                
│   │   └── livro.py           
│   │
│   ├── controllers/            
│   │   ├── livro_controller.py 
│   │   └── ...                 
│   │
│   ├── templates/              
│   │   ├── index.html          
│   │   ├── add_book.html       
│   │   ├── edit_book.html      
│   │   └── ...                  
│   │
│   ├── static/                 
│   │   └── style.css         
│   │
│   ├── app.py                  
│   └── config.py (se houver)     
│
├── requirements.txt            
├── LICENSE                     
└── README.md

# **⚙️ Instalação**

# 1. Clone o repositório
git clone https://github.com/MarianaMilaniMatos/BookFlow.git
cd BookFlow

# 2. Crie ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# ou
venv\Scripts\activate      # Windows

# 3. Instale dependências
pip install -r requirements.txt

#**🚀 Rodando Localmente**     
# Com o ambiente virtual ativado
flask run
Depois, abra no navegador:
http://127.0.0.1:5000

#**📖 Funcionalidades**  

✅ Adicionar novo livro com título, autor, gênero e status de leitura
🔍 Ver todos os livros cadastrados
✏️ Editar livro existente
❌ Remover livro
💬 Possível feedback visual / mensagens de sucesso ou erro
🎨 Interface com estilo básico (CSS) e navegação simples

Feito com ❤️ por Mariana Milani Matos
