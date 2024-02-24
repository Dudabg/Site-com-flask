from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homePage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_de_usuario>")
def usuarios(nome_de_usuario):
    return render_template("usuarios.html", nome_de_usuario = nome_de_usuario)








#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

