from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Charger le modèle de NLP
nlp_model = pipeline('conversational', model="facebook/blenderbot-400M-distill")

@app.route('/')
def home():
    return "Bienvenue sur le Chatbot !"

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_input = data.get('message')
    
    # Générer une réponse à partir du modèle NLP
    conversation = nlp_model(user_input)
    response = conversation[0]['generated_responses'][0]
    
    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)