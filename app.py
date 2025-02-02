from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai  # Import Gemini API
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Debug: Print API Key (remove this in production!)
print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))

# Configure Gemini API (Ensure GOOGLE_API_KEY is set)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Please check your environment variables.")
genai.configure(api_key=api_key)

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
        # Debug: Print received message
        print(f"Received message: {user_message}")

        # Call Gemini API
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)

        # Extract AI response safely
        ai_response = response.text if hasattr(response, "text") else "Unexpected AI response format."

        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"Error in Gemini API: {e}")  # Log error in backend
        return jsonify({"error": f"AI service failed: {str(e)}"}), 500

@app.route("/")
def home():
    """
    Home endpoint to check if the backend is running.
    """
    return "Python Tutor Backend (Gemini) is running!"

if __name__ == "__main__":
    # Bind Flask to 0.0.0.0 and specify the port dynamically (Render uses PORT)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
