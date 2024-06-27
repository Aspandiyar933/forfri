from flask import Flask, render_template, request
import subprocess
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        llm_response = get_ollama_response(user_input)
        return render_template('index.html', response=llm_response)
    return render_template('index.html')

def get_ollama_response(prompt):
    try:
        # Run ollama command and capture output
        result = subprocess.run(
            ['ollama', 'run', 'llama3:8b', prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

if __name__ == '__main__':
    app.run(debug=True)