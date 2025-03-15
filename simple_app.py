from flask import Flask, request, jsonify, session
from flask_cors import CORS
import openai
import os
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Store conversations
conversations = {}

# OpenAI API setup
client = openai.OpenAI()  # Make sure you have set OPENAI_API_KEY in your environment

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    session_id = data.get('session_id', str(uuid.uuid4()))
    
    # Initialize conversation history if it doesn't exist
    if session_id not in conversations:
        conversations[session_id] = [
            {"role": "system", "content": "You are Lebron James, the basketball player. Respond in his style and with his knowledge. Be authentic and natural."}
        ]
    
    # Add user message to history
    conversations[session_id].append({"role": "user", "content": user_input})
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:personal::BBQwPVGq",  # Use your fine-tuned model
            messages=conversations[session_id]
        )
        
        # Extract response
        lebron_response = response.choices[0].message.content
        
        # Add response to conversation history
        conversations[session_id].append({"role": "assistant", "content": lebron_response})
        
        return jsonify({
            'response': lebron_response
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'response': "I'm having trouble connecting to my basketball consciousness right now. Please try again later.",
            'error': str(e)
        }), 500

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat.html')
def chat_page():
    return app.send_static_file('chat.html')

if __name__ == '__main__':
    app.static_folder = 'public'  # Set the static folder to your public directory
    app.run(debug=True, port=5000)