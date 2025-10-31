from flask import Flask, render_template
# para instalar o programa pip install flask

# Criando do app Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Olá Mundo</h1><br><a href='/sobre'>Pagina Sobre'</a>"

@app.route('/sobre')
def sobre():
    return "<h3>Feito por Seu Nome</h3><br><a href='/'>Pagina Inicial</a>"

@app.route('/nome/<nome>')
def saudacao(nome):
    return f"<h1>Olá, {nome}!</h1>"


# Iniciar o Servidor
if __name__ == '__main__':
   app.run(debug=True)