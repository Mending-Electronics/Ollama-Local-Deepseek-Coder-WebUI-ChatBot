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



## Overview of `deepseek-coder:1.3b-instruct-q2_K` model

Is a specialized AI model within the Deepseek family, designed specifically for tasks related to computer science, such as Data Structures and Algorithms (DSA), code generation, and code fixing.

- **deepseek-coder:** Deepseek AI model used specifically for computer science tasks, focusing on DSA, code generation, and code fixing.
- **1.3b:** The model contains 1.3 billion parameters, providing a high level of sophistication and capability.
- **instruct:** This version of the model is instruction-based, meaning it is designed to follow specific instructions rather than generating creative or unprompted content.
- **q2 and K:** Indicate that this is a compressed version of the model, optimized to use less RAM, making it more efficient in resource-constrained environments.

### Key Features

- **Specialized for Computer Science:** Optimized for activities related to Data Structures and Algorithms (DSA), code generation, and bug fixing.
- **High Parameter Count:** 1.3 billion parameters provide robust performance for intricate tasks.
- **Instruction-Based:** Designed to follow user instructions closely, ensuring precise and accurate output.
- **Compressed and Optimized:** The `q2` and `K` annotations denote a version that is compressed and optimized to use less RAM, offering efficient performance without compromising on capability.

## Personal Usage

I utilize `deepseek-coder:1.3b-instruct-q2_K` at home for personal use on the following setup:

- **Device:** HP Elitdesk 800 G3
- **Operating System:** Windows 11 Pro
- **Processor:** Intel i5-6500
- **RAM:** 16 GB
- **Graphics:** Intel UHD Graphics 530
- **Storage:** 250 GB SSD

Despite the relatively modest hardware specs, the compressed and optimized version of the model functions efficiently within these constraints, aiding in various personal computer science projects.

## Changing the Model

If you want to change the model, you can do so by editing the `app.py` file. Set the desired model in the `IAmodel` variable. 
For example: python IAmodel = "your-desired-model"
This allows for easy switching between different AI models based on your requirements.



## Result

![page](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture1.png?raw=true "page")

![chat](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture2.png?raw=true "chat")

![chat](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture3.png?raw=true "chat")

![copy](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture4.png?raw=true "copy")

![copycode](https://github.com/Mending-Electronics/Ollama-Local-Deepseek-Coder-WebUI-ChatBot/blob/main/.illustration/Capture5.png?raw=true "copycode")
