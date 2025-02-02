from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai  # Import Gemini API
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API (Ensure GOOGLE_API_KEY is used)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle chat requests from the frontend.
    Sends the user's message to Google Gemini and returns the AI's response.
    """
    data = request.json
    user_message = data.get("message")

    try:
        # Call Gemini API
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)

        # Extract AI response
        ai_response = response.text if response.text else "Sorry, I couldn't understand that."
        return jsonify({"response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    """
    Home endpoint to check if the backend is running.
    """
    return "Python Tutor Backend (Gemini) is running!"

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
