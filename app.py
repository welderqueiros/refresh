from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import os

app = Flask(__name__)

def run_selenium():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        # Configuração especial para o Render
        service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Seu código Selenium aqui
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        return {"success": True, "title": title}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/run-script')
def execute_script():
    result = run_selenium()
    return jsonify(result), 200 if result['success'] else 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)