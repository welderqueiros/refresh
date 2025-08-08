from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

app = Flask(__name__)

def run_selenium_script():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        return {"success": True, "result": f"Título: {title}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/run-script')
def execute_script():
    result = run_selenium_script()
    if result['success']:
        return jsonify(result)
    else:
        return jsonify(result), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)