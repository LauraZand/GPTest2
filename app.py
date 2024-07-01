from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Charger le modèle de NLP
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="princeton-nlp/Llama-3-Instruct-8B-SimPO")
pipe(messages)

@app.route('/')
def home():
    return "Bienvenue sur le Chatbot !"

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_input = data.get('message')
    
    # Générer une réponse à partir du modèle NLP
    response = pipe(user_input, max_length=50, num_return_sequences=1)
    generated_text = response[0]['generated_text']
    
    return jsonify({"response": generated_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
