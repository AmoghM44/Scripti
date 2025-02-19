from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv  # Import the load_dotenv function

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the Gemini API key from the environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the PowerShell script from the form
        powershell_script = request.form.get("script")

        # Call the Gemini API to enhance the script
        enhanced_script = enhance_script_with_gemini(powershell_script)

        # Render the result page with the enhanced script
        return render_template("index.html", original_script=powershell_script, enhanced_script=enhanced_script)

    # Render the input form for GET requests
    return render_template("index.html")

def enhance_script_with_gemini(script):
    """
    Sends the PowerShell script to the Gemini API for enhancement.
    """
    headers = {
        "Content-Type": "application/json"
    }

    # Refined prompt to ensure only the enhanced script is returned
    prompt = f"""
    Enhance the following PowerShell script strictly following these rules:
    1. Add a synopsis at the top of the script describing its purpose, parameters, and usage.
    2. Follow PowerShell best practices for naming conventions, indentation, and structure.
    3. Add inline comments to explain the logic where necessary.
    4. Return ONLY the enhanced script. Do NOT include any additional explanations, notes, or text outside the script.

    Here is the script:
    {script}
    """

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        # Parse the response to extract the enhanced script
        response_data = response.json()
        enhanced_script = response_data["candidates"][0]["content"]["parts"][0]["text"]

        # Remove any extra text or explanations from the response
        # Ensure only the script is returned
        enhanced_script = enhanced_script.strip()  # Remove leading/trailing whitespace
        if "```" in enhanced_script:  # Handle markdown code blocks
            enhanced_script = enhanced_script.split("```")[1].strip()  # Extract the script inside the code block
    except requests.exceptions.RequestException as e:
        enhanced_script = f"Error: {str(e)}"
    except KeyError:
        enhanced_script = "Error: Unable to parse the response from Gemini API."

    return enhanced_script

if __name__ == "__main__":
    app.run(debug=True)