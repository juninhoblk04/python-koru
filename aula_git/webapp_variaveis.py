#vamos criar um dicionariorio com duas chaves e retornar seus datos pela rota
dicionario = {
    "nome":"juninho",
    "nascimento":1987
}





from flask import Flask
app = Flask(__name__)
@app.route("/teste")
def mostra_dicionario():
    return "teste"


@app.route("/")
def dados_usuario():
    return f"O usuario {dicionario['nome']} nasceu em {dicionario['nascimento']}"

app.run(debug=True)