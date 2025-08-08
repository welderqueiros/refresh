import os
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Caminho absoluto para o script
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'run_selenium.py')

@app.route('/run-script')
def run_script():
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(SCRIPT_PATH):
            return jsonify({
                "success": False,
                "error": f"Arquivo não encontrado: {SCRIPT_PATH}",
                "output": ""
            }), 404

        result = subprocess.run(
            ['python', SCRIPT_PATH],
            capture_output=True,
            text=True
        )
        
        return jsonify({
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "output": ""
        }), 500