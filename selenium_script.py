from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

print("Iniciando script Selenium...")

try:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    print("Navegador iniciado com sucesso!")
    driver.get("https://www.google.com")
    print(f"Título da página: {driver.title}")
    
    time.sleep(2)
    driver.quit()
    print("Script executado com sucesso!")
    
except Exception as e:
    print(f"ERRO: {str(e)}")
    raise