from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os

# load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Flask application
app = Flask(__name__)

# Define the POST route
@app.route('/chat', methods=['POST'])
def chat():
    # Get the message of the POST request
    message = request.json['message']
    
    # Use the ChatGPT API to generate a response message
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    # Send the response message back to the client
    return jsonify(response.choices[0].text.strip())
