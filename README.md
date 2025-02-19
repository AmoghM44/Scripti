# **PowerScript Enhancer**

![Flask](https://img.shields.io/badge/Framework-Flask-blue)
![Python](https://img.shields.io/badge/Language-Python-green)
![Gemini API](https://img.shields.io/badge/API-Gemini-orange)

PowerScript Enhancer is a Flask-based web application that takes PowerShell scripts as input and returns an enhanced version of the script. The enhanced script includes best practices, proper naming conventions, inline comments, and a synopsis at the top for better readability and understanding. The application integrates with the **Gemini API** to generate the enhanced scripts.
---
## **Setup and Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/powerscript-enhancer.git
   cd powerscript-enhancer
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory:
     ```bash
     touch .env
     ```
   - Add your Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:5000`.

---

## **How to Use**

1. **Enter Your Script**:
   - Paste your PowerShell script into the text area on the homepage.

2. **Enhance the Script**:
   - Click the "Enhance Script" button to submit the script.

3. **View the Enhanced Script**:
   - The enhanced script will be displayed below the input area.
---
---

## **Features**

- **Script Enhancement**:
  - Adds a synopsis describing the script's purpose, parameters, and usage.
  - Follows PowerShell best practices for naming conventions and structure.
  - Includes inline comments to explain the logic.

- **Gemini API Integration**:
  - Uses the Gemini API to process and enhance PowerShell scripts.

- **User-Friendly Interface**:
  - Simple web interface for inputting scripts and viewing enhanced results.

- **Secure**:
  - API keys are stored in a `.env` file and excluded from version control.

---

## **Prerequisites**

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- A Gemini API key (get it from [Gemini API](https://ai.google.dev/))

---

---

## **Example**

### Input:
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

### Output:
```powershell
<#
.SYNOPSIS
    Retrieves the top 5 processes consuming the most CPU and displays their details.

.DESCRIPTION
    This script retrieves all running processes, sorts them by CPU usage in descending order,
    and selects the top 5 processes for display.

.EXAMPLE
    .\Get-TopProcesses.ps1
#>

Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

---

## **Project Structure**

```
powerscript-enhancer/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not tracked by Git)
├── .gitignore              # Files to ignore in Git
├── templates/              # HTML templates
│   └── index.html          # Homepage template
└── README.md               # Project documentation
```

---

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.
---

## **Acknowledgments**

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Gemini API](https://ai.google.dev/) - The AI API used for script enhancement.
- [python-dotenv](https://pypi.org/project/python-dotenv/) - For managing environment variables.

---

## **Contact**

For questions or feedback, feel free to reach out:

- **Amogh M**  
- **Email**: amoghm44@gmail.com

---

Enjoy enhancing your PowerShell scripts with **PowerScript Enhancer**! 🚀

---
