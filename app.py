from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message")
    # Implémente la logique du chatbot ici
    response = generate_response(user_input)
    return jsonify({"response": response})

def generate_response(user_input):
    # Exemple de réponse simple
    return "Ceci est une réponse générée par le chatbot."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
