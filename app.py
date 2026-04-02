from flask import Flask 

app = Flask (__name__)

@app.route('/')
def home():
    return "🏉Site de Rugby🏉"

@app.route('/rugbyDoAno') 
def Rugby():
    return "World cup Rugby🏉🏉"

@app.route('/JogoDaSemana')
def New():
    return "Domingo teve jogo das Yaras"

@app.route('/brasilAvançaParaSevens')
def Noticia():
    return "Yaras ganham e avaçam para a copa Sevens"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
