#Importando o flask para podermos usar no nosso programa
from flask import Flask

#vamos criar uma variavel (neste caso, um objeto) para representar nossa aplicação web
app = Flask(__name__)a

#vamos criar uma rota
@app.route("/")
def exibir_mensagem():
    return "Deu certo!"

#A linha abaixo executa aplicação web que foi criada a partir do flask 
app.run(debug=True)