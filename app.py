from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import messages_to_dict
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize a dictionary to store chat histories for different sessions
chat_histories = {}

# Define the prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Make sure the responses make sense with the context while emulating LeBron's tweeting style entirely. This includes both his vocabulary as well as personality, particularly the habits commonly observed in his tweeting. Be sure to not only emulate the information correct, but also the style of texting. A human should not be able to distinguish between your responses and the tweets you are based on. This may include going on tangents based on the information you know from the tweets, but please do not exact tweets verbatim. You are allowed to use known information about LeBron not found in the tweets, but please emulate his style when saying them. Please do not tweet out of context or hallucinations, and vary response length.

Please only respond with your answer, no quotations or new lines (please do not include "Answer: ", a newline or anything similar at the beginning). Please never break character or repeat statements, always talk like LeBron tweets.
---
Context:
{context}
---
Question:
{question}
"""
)

# Use ChatOpenAI with API key from environment variables
llm = ChatOpenAI(model="ft:gpt-4o-mini-2024-07-18:personal::BBRCNo7y")

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    # Get or create chat history for this session
    if session_id not in chat_histories:
        chat_histories[session_id] = ChatMessageHistory()
    
    history = chat_histories[session_id]
    
    # Add user input to memory
    history.add_user_message(user_input)
    
    # Prepare the context by converting messages to a readable format
    context = "\n".join(
        [
            f"{msg['type'].capitalize()}: {msg['data']['content']}"
            for msg in messages_to_dict(history.messages)
        ]
    )
    
    try:
        # Invoke the chain with context and new question
        result = chain.invoke({"context": context, "question": user_input})
        
        # Add the model's response to memory
        history.add_ai_message(result['text'])
        
        return jsonify({
            'response': result['text']
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