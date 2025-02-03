from flask import Flask, render_template, request, jsonify
import subprocess
from ollama import chat

app = Flask(__name__, template_folder='templates')

global IAmodel
IAmodel = "deepseek-coder:1.3b-instruct-q2_K"
# as default : deepseek-coder:1.3b-instruct-q2_K



# Initialize a persistent subprocess with a queue for communication
command = f"ollama run {IAmodel}"
proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

def run_ollama_chat(user_input):
    response = chat(model=IAmodel, messages=[{'role': 'user', 'content': user_input}])
    return response['message']['content']

@app.route('/')
def index():
    return render_template('index.html', IAmodel=IAmodel)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    result = run_ollama_chat(user_input)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)
