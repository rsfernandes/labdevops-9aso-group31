from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "FIAP9ASO-31 - BOTA FE"

if __name__ == '__main__':
    app.run()