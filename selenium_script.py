from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os, time

load_dotenv()

login_email = os.getenv("EMAIL")
login_password = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

# Se o chromedriver foi instalado em /usr/bin/chromedriver (build.sh), usamos ele.
LOCAL_CHROMEDRIVER = "/usr/bin/chromedriver"
if os.path.exists(LOCAL_CHROMEDRIVER):
    service = Service(LOCAL_CHROMEDRIVER)
else:
    # fallback para webdriver_manager (vai baixar em runtime)
    service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30)

url = "https://app.powerbi.com/groups/a81161c5-3a80-4f12-bd87-177f52f58a52/datasets/7b7c51f4-4a24-4748-b278-6a321add552f/details?experience=power-bi"
print("Acessando o Power BI")
driver.get(url)
time.sleep(5)

# Seletors e fluxo (cópia do seu script)
email_xpath='//*[@id="email"]'
botao_enviar_xpath ='//*[@id="submitBtn"]'
senha_xpath='//*[@id="i0118"]'
botao_entrar_xpath='//*[@id="idSIButton9"]'
botao_sim_xpath='//*[@id="idSIButton9"]'
botao_atualizar_xpath='//*[@id="content"]/tri-shell/tri-item-renderer/tri-extension-page-outlet/div[2]/dataset-details-container/dataset-action-bar/action-bar/action-button[2]/button'
botao_atualizar_agora_xpath='//*[@id="mat-menu-panel-1"]/div/span[1]/button'

print("Preenchendo o email")
campo_email = wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
campo_email.clear()
campo_email.send_keys(login_email)
time.sleep(3)

print("Clicando no botão enviar")
campo_botao_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, botao_enviar_xpath)))
campo_botao_enviar.click()
time.sleep(3)

print("Preenchendo a senha")
campo_senha = wait.until(EC.presence_of_element_located((By.XPATH, senha_xpath)))
campo_senha.clear()
campo_senha.send_keys(login_password)
time.sleep(3)

print("Clicando no botão entrar")
campo_botao_entrar = wait.until(EC.element_to_be_clickable((By.XPATH, botao_entrar_xpath)))
campo_botao_entrar.click()
time.sleep(3)

print("Clicando no botão sim")
campo_botao_sim = wait.until(EC.element_to_be_clickable((By.XPATH, botao_sim_xpath)))
campo_botao_sim.click()
time.sleep(10)

print("Clicando no botão atualizar")
campo_botao_atualizar = wait.until(EC.element_to_be_clickable((By.XPATH, botao_atualizar_xpath)))
campo_botao_atualizar.click()
time.sleep(3)

print("Clicando no botão atualizar agora")
campo_botao_atualizar_agora = wait.until(EC.element_to_be_clickable((By.XPATH, botao_atualizar_agora_xpath)))
campo_botao_atualizar_agora.click()
time.sleep(3)

print("Atualização realizada com sucesso")
driver.quit()
