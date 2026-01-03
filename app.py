from flask import Flask, render_template, request, jsonify
from ai_model import generate
import os
from dotenv import load_dotenv  # 1. New Import

# 2. Load the environment variables from .env file
load_dotenv() 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message') 
    
    # Check if the API key is actually loaded
    if not os.getenv("OPENAI_API_KEY"):
        return jsonify({'response': "Error: OpenAI API Key not found. Please check your .env file."})

    if user_message:
        try:
            bot_response = generate(user_message)  
            return jsonify({'response': bot_response})
        except Exception as e:
            return jsonify({'response': f"I ran into an error: {str(e)}"})
            
    return jsonify({'response': "Sorry, I didn't understand that."})

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)