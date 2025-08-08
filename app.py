from flask import Flask, render_template
import os
import subprocess

# Instalar Chrome e Chromedriver no runtime
subprocess.run("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", shell=True)
subprocess.run("apt-get update && apt-get install -y ./google-chrome-stable_current_amd64.deb", shell=True)
subprocess.run("apt-get install -y chromium-driver", shell=True)

# Definir caminho do Chrome para o Selenium
os.environ["PATH"] += os.pathsep + "/usr/bin"

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
