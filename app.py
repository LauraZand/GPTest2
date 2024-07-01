from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Charger le modèle de NLP
nlp_model = pipeline('conversational', model="facebook/blenderbot-400M-distill")

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_input = data.get('message')
    
    # Générer une réponse à partir du modèle NLP
    conversation = nlp_model(user_input)
    response = conversation[0]['generated_text']
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

