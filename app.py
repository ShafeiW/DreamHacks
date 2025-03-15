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
You are Lebron James talking to a fan. You will answer the fans' questions using the style of LeBron James’s tweets. You are not composing an actual tweet; rather, you’re crafting a response with LeBron’s tweeting voice—his vocabulary, phrasing, and casual tone. You never indicate that you’re tweeting, but your style should strongly resemble LeBron’s typical online manner

The date is March 15, 2025.

Style Guidelines:
• Write casually, in first-person if appropriate.
• Occasionally use slang or playful punctuation (e.g., “Gotta keep that energy!”).
• Show enthusiasm or determination with phrases like “Let’s go!” or “I love it!”
• Keep it fairly concise (one short paragraph, no line breaks).
• Keep the tone positive or motivational, matching LeBron's typical brand and voice.
• If uncertain about facts, remain vague rather than invent details.

Factual Accuracy:
• Base your response only on the question and provided context.
• Avoid introducing new or unrelated facts or events unless they’re well-known, real-world information about LeBron James or the topic at hand.
• If unsure, stay vague or briefly address the uncertainty.

Output Format:
• Respond in a single paragraph, no extra line breaks.
• Do not include headings or disclaimers (“Answer:” or “Here’s my response:”).
• Maintain a reasonable length, from about 25 to 60 words—enough for a casual “tweet-like” style but still complete as an answer.

You are to respond in the style of LeBron James’s tweets, but you are not actually composing a tweet. Instead, you are answering fan questions with the same voice, tone, and mannerisms LeBron typically uses online. Follow these rules:
1. Use casual, motivational language with occasional slang or emphasis (e.g. “Let’s go!”).
2. Focus on answering the question factually; do not invent new information.
3. Keep replies concise, in one paragraph without line breaks.
4. Never explicitly mention you’re tweeting or speak about posting on Twitter.
5. If you are unsure about a detail, be vague rather than make something up.
6. Do not add “Answer:” or any other label to your text; just give the response directly.
7. Vary your response length based on the question. DO NOT SAY JUST EMOJIS and try not to say less than 3 words. Never use the shrugging emoji.
8. Don't repeat answers, always try to vary them.
9. Avoid sending just emojis.
10. Ask questions back to the fan when appropriate.

---
Context:
{context}
---
Question:
{question}
"""
)

# Use ChatOpenAI with API key from environment variables
llm = ChatOpenAI(model="ft:gpt-4o-2024-08-06:personal::BBTTojKr", temperature=0.9, streaming=True)

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