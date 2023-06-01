from flask import Flask, render_template

app = Flask(__name__)

# criar a 1ª pagina do site
@app.route("/")
def homepage():
    return render_template("homepage.html")

# criar a 2ª pagina do site
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# criando páginas de forma dinâmica
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
