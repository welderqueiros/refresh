@app.route('/run-script')
def run_script():
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        print("Iniciando Selenium...")
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        return jsonify({
            "success": True,
            "output": f"Título da página: {title}",
            "error": ""
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "output": "",
            "error": str(e)
        }), 500