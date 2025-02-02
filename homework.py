from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Helper function to generate a random challenge based on the user's question
def generate_homework_challenge(question):
    if "add" in question.lower():
        return """
        # Write a Python function to add two numbers
        def add(a, b):
            # Your code here
            return a + b
        """
    elif "multiply" in question.lower():
        return """
        # Write a Python function to multiply two numbers
        def multiply(a, b):
            # Your code here
            return a * b
        """
    elif "subtract" in question.lower():
        return """
        # Write a Python function to subtract two numbers
        def subtract(a, b):
            # Your code here
            return a - b
        """
    elif "divide" in question.lower():
        return """
        # Write a Python function to divide two numbers
        def divide(a, b):
            # Your code here
            return a / b
        """
    else:
        return "Sorry, I couldn't understand the question. Please ask about mathematical operations like addition, multiplication, etc."

@app.route('/homework', methods=['POST'])
def get_homework():
    data = request.json
    user_question = data.get('question', '')  # Extract the user question from the request

    if not user_question:
        return jsonify({'error': 'No question provided'}), 400
    
    # Generate the challenge based on the user's question
    homework_challenge = generate_homework_challenge(user_question)
    return jsonify({'challenge': homework_challenge})

if __name__ == "__main__":
    app.run(debug=True)
