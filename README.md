# Local-Deepseek-Coder-WebUI-ChatBot

A Python Flask-based web application that interacts with LLM models using the Ollama serve feature. This project leverages Vue.js and Bootstrap for a responsive and interactive front-end experience.

## Features

- User-friendly interface for interacting with the chatbot.
- Responsive design using Bootstrap 5 and Vue.js 3.
- Flask backend for handling requests and responses.
- Markdown rendering using Marked.js.
- Code highlighting with Prism.js.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.11
- Flask framework
- Ollama (for running the DeepSeek-Coder locally)
- DeepSeek-Coder Model (deepseek-coder:1.3b-instruct-q2_K)
- Text Editor/IDE (like VSCode, PyCharm, or Sublime Text)

## Installation

1. **Download Ollama**

   **For Windows:**
   Visit the official Ollama website https://ollama.com/download and download the Windows installer.

   After installation, verify it by running the following command in PowerShell:
   
   ```bash
   ollama --version

2. **Pulling and Running the deepseek-coder:1.3b-instruct-q2_K**

   With Ollama installed, it's time to pull the DeepSeek-r1:1.5b model and run it locally. </br>
   How to Pull the DeepSeek Model
   - Open your terminal or command prompt.
   - Type the following command to pull the model:
   ```
    ollama pull deepseek-coder:1.3b-instruct-q2_K
   ```
   This command will download the model, which may take some time depending on your internet speed and system resources.
   
4. **Checking Available Models Using ollama list**
   ```
   ollama list
   ```
   This will display all the models you have pulled and installed, including their version numbers. You can use this to verify that DeepSeek-r1:1.5b is available and ready to be used.

5. **Clone the repository**:
   ```bash
   git clone https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot.git
   cd Ollama-Local-Deepseek-Coder-WebUI-ChatBot
   
6. **Set up a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   
7. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
   
8. **Run the Flask application:**
   ```
   python app.py
   ```
   
9. **Access the application:**

   Open your browser and go to
   ```
   http://127.0.0.1:5000.
   ```

## Result

![page](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture1.png?raw=true "page")

![chat](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture2.png?raw=true "chat")

![chat](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture3.png?raw=true "chat")

![copy](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture4.png?raw=true "copy")

![copycode](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture5.png?raw=true "copycode")
