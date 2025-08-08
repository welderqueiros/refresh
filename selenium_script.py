from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from dotenv import load_dotenv
import os
import time

load_dotenv()

login_email = os.getenv("EMAIL")
login_password = os.getenv("PASSWORD")

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Configuração específica para o Render
    chrome_options.binary_location = "/usr/bin/google-chrome" if os.path.exists("/usr/bin/google-chrome") else None
    
    try:
        # Usando ChromeDriverManager para gerenciar o driver
        service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Erro ao iniciar o WebDriver: {str(e)}")
        raise

def main():
    try:
        driver = setup_driver()
        wait = WebDriverWait(driver, 30)

        url = "https://app.powerbi.com/groups/a81161c5-3a80-4f12-bd87-177f52f58a52/datasets/7b7c51f4-4a24-4748-b278-6a321add552f/details?experience=power-bi"
        print("Acessando o Power BI")
        driver.get(url)
        time.sleep(5)

        # Elementos e interações
        print("Preenchendo o email")
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys(login_email)
        time.sleep(3)

        print("Clicando no botão enviar")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitBtn"]'))).click()
        time.sleep(3)

        print("Preenchendo a senha")
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))).send_keys(login_password)
        time.sleep(3)

        print("Clicando no botão entrar")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()
        time.sleep(3)

        print("Clicando no botão sim")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()
        time.sleep(10)

        print("Clicando no botão atualizar")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/dataset-details-container/dataset-action-bar/action-bar/action-button[2]/button'))).click()
        time.sleep(3)

        print("Clicando no botão atualizar agora")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-menu-panel-1"]/div/span[1]/button'))).click()
        time.sleep(3)

        print("Atualização realizada com sucesso")
        
    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()