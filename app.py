from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar")
def executar():
    subprocess.Popen(["python", "script.py"])
    return "Script iniciado!"

if __name__ == "__main__":
    app.run(debug=True)