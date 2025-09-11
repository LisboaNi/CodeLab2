from flask import Flask
from controllers.controller import listar, cadastrar, adicionar, logar, autenticar, logout

app = Flask(__name__)

app.secret_key = 'secretkey'

# Aqui associamos a rota com a função
# app.add_url_rule('/', view_func=lista)

@app.route('/')
def index():
    return listar()

app.add_url_rule('/cadastrar', view_func=cadastrar)
app.add_url_rule('/adicionar', view_func=adicionar, methods=['POST'])
app.add_url_rule('/login', view_func=logar)
app.add_url_rule('/autenticar', view_func=autenticar, methods=['POST'])
app.add_url_rule('/logout', view_func=logout)


app.run(debug=True)