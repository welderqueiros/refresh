from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Serviço está rodando"

@app.route('/run-script')
def run_script():
    try:
        # Executa o script em um novo processo
        result = subprocess.run(
            ['python', 'run_selenium.py'],
            capture_output=True,
            text=True
        )
        
        return jsonify({
            "success": True,
            "output": result.stdout,
            "error": result.stderr
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)