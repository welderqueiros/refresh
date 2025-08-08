from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar")
def executar():
    try:
        # Inicia o script em background numa nova sessão para não ser morto pelo pai
        subprocess.Popen(
            ["python3", "selenium_script.py"],
            start_new_session=True
        )
        return "Script iniciado com sucesso!"
    except Exception as e:
        return f"Erro ao iniciar script: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
