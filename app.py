from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure ton API key OpenAI
openai.api_key = os.getenv('REDACTED')

@app.route('/')
def home():
    return "Bienvenue sur le Chatbot !"

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_input = data.get('message')
    
    # Utiliser GPT-3 pour générer une réponse
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50
    )
    
    generated_text = response.choices[0].text.strip()
    
    return jsonify({"response": generated_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


