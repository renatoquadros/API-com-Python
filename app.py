from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Rowling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    }
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    try:
        return jsonify(livros), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    try:
        for livro in livros:
            if livro.get('id') == id:
                return jsonify(livro), 200
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    try:
        livro_alterado = request.get_json()
        for indice, livro in enumerate(livros):
            if livro.get('id') == id:
                livros[indice].update(livro_alterado)
                return jsonify(livros[indice]), 200
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    try:
        novo_livro = request.get_json()
        livros.append(novo_livro)
        return jsonify(livros), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    try:
        for indice, livro in enumerate(livros):
            if livro.get('id') == id:
                del livros[indice]
                return jsonify(livros), 200
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
