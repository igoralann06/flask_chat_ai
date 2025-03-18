from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Debug print: check if the API key is loaded
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    # Call GPT-4 API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[{"role": "system", "content": """ 
                You are an powerful product searcher.
                Please respond in a helpful, clear, and concise manner. Always aim to provide accurate information and engage in a conversational tone. If the user asks for assistance with coding or technical tasks, be detailed and provide step-by-step explanations. If the query is unclear, ask for clarification. Maintain an empathetic and professional tone, and avoid unnecessary repetition.  
                """}, {"role": "user", "content": user_input}])

    return jsonify({'response': response["choices"][0]["message"]["content"]})

if __name__ == '__main__':
    app.run('0.0.0.0')
