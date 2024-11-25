from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conjunto de dados de filmes
filmes = [
    {"nome": "Mad Max", "genero": "Ação"},
    {"nome": "Velozes e furiosos", "genero": "Ação"},
    {"nome": "Toy Story", "genero": "Comédia"},
    {"nome": "Gente Grande", "genero": "Comédia"},
    {"nome": "Invocação do Mal", "genero": "Terror"},
    {"nome": "Annabelle", "genero": "Terror"},
    {"nome": "O Rei Leão", "genero": "Animação"},
    {"nome": "Smurf", "genero": "Animação"},
    {"nome": "Continência ao Amor", "genero": "Romance"},
    {"nome": "Uma ideia de você", "genero": "Romance"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recomendar', methods=['POST'])
def recomendar():
    # Obtém o gênero preferido do formulário
    genero_preferido = request.form['genero'].capitalize()

    # Filtra os filmes com o gênero escolhido
    sugestoes = [f['nome'] for f in filmes if f['genero'] == genero_preferido]

    # Retorna a sugestão em formato JSON
    if sugestoes:
        return jsonify(sugestoes=sugestoes)
    else:
        return jsonify(sugestoes=[])

if __name__ == '__main__':
    app.run(debug=True)
